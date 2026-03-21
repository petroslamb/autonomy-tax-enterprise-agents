#!/usr/bin/env python3

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


LABEL_PATTERN = re.compile(r"^(\d\.\d)\s+(.+?):")

LABEL_STATS_COLUMNS = [
    "mast_label",
    "mast_name",
    "control_family",
    "trace_count",
    "trace_share_all",
    "trace_share_failing",
]

PAIR_STATS_COLUMNS = [
    "label_a",
    "label_b",
    "pair_count",
    "pair_share_failing",
    "family_a",
    "family_b",
    "enterprise_interpretation",
]

BENCHMARK_STATS_COLUMNS = [
    "benchmark_name",
    "total_traces",
    "failing_traces",
    "failure_rate",
    "avg_active_labels_in_failing_traces",
    "enterprise_relevance",
    "notes",
]

SYSTEM_STATS_COLUMNS = [
    "mas_name",
    "total_traces",
    "failing_traces",
    "failure_rate",
    "avg_active_labels_in_failing_traces",
    "notes",
]

BENCHMARK_RELEVANCE = {
    "ProgramDev": "high",
    "GAIA": "medium",
    "SWE-Bench-Lite": "high",
    "Test-C": "medium",
    "GSM": "low",
    "MMLU": "low",
    "Olympiad": "low",
}

BENCHMARK_NOTES = {
    "ProgramDev": "Best enterprise proxy in MAST; software-building workflows expose coordination, termination, and verification burden.",
    "GAIA": "Mixed task environment; useful for bounded workflow mechanics and tool-use coordination, but broader than enterprise operations.",
    "SWE-Bench-Lite": "Small but enterprise-relevant code-change sample; useful for verifiable action and verification failures.",
    "Test-C": "Small controlled tool-use sample; useful for checking task-spec adherence and verification behavior.",
    "GSM": "Reasoning-heavy benchmark; useful for coordination and control motifs, not enterprise deployment economics.",
    "MMLU": "Knowledge and reasoning benchmark; supports control-layer claims, not enterprise operating-cost calibration.",
    "Olympiad": "Hard reasoning benchmark; supports compounding failure mechanics, not enterprise deployment economics.",
}

SAME_FAMILY_INTERPRETATIONS = {
    "clarification_and_handoff": "Communication breakdowns compound into missing-info exceptions, rework, and queue churn.",
    "context_continuity": "Context resets compound into reconciliation work and repeated handoff recovery.",
    "loop_and_termination": "State-tracking and stop-condition failures compound into stuck runs and reviewer babysitting.",
    "plan_action_verification": "Reasoning, execution, and checking failures compound into escaped bad actions.",
    "role_and_authority": "Authority confusion compounds into ambiguous ownership and unsafe privilege use.",
}

FAMILY_PAIR_INTERPRETATIONS = {
    ("clarification_and_handoff", "context_continuity"): "Lost context and weak handoffs force re-explanation, reconciliation, and exception queues.",
    ("clarification_and_handoff", "loop_and_termination"): "Missing clarification plus weak stop logic create retries, stalls, and reviewer babysitting.",
    ("clarification_and_handoff", "plan_action_verification"): "Poor handoffs raise the odds that wrong reasoning or unchecked actions escape.",
    ("clarification_and_handoff", "role_and_authority"): "Unclear authority worsens handoff quality and who must clarify or approve.",
    ("context_continuity", "loop_and_termination"): "State loss and weak stopping rules create repeated work and stuck recovery loops.",
    ("context_continuity", "plan_action_verification"): "Lost state makes reasoning-to-action translation and verification less reliable.",
    ("context_continuity", "role_and_authority"): "Authority confusion makes context ownership and recovery paths unclear.",
    ("loop_and_termination", "plan_action_verification"): "Looping or stalled workflows raise the chance of unchecked or misaligned actions reaching execution.",
    ("loop_and_termination", "role_and_authority"): "Unclear authority makes termination decisions and recovery ownership ambiguous.",
    ("plan_action_verification", "role_and_authority"): "Weak authority design makes verification gates and action ownership harder to enforce.",
}


def label_sort_key(label: str) -> tuple[int, int]:
    major, minor = label.split(".")
    return (int(major), int(minor))


def format_share(value: float) -> str:
    return f"{value:.4f}"


def format_average(value: float) -> str:
    return f"{value:.3f}"


def parse_definitions(definitions_path: Path) -> dict[str, str]:
    labels: dict[str, str] = {}
    for line in definitions_path.read_text().splitlines():
        match = LABEL_PATTERN.match(line.strip())
        if match:
            labels[match.group(1)] = match.group(2).strip()
    if len(labels) != 14:
        raise ValueError(
            f"Expected 14 MAST labels in {definitions_path}, found {len(labels)}."
        )
    return labels


def read_crosswalk(crosswalk_path: Path) -> list[dict[str, str]]:
    with crosswalk_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not rows:
        raise ValueError(f"Crosswalk {crosswalk_path} is empty.")
    return rows


def validate_crosswalk(
    crosswalk_rows: list[dict[str, str]],
    definitions: dict[str, str],
    dataset_labels: set[str],
) -> None:
    crosswalk_labels = [row["mast_label"] for row in crosswalk_rows]
    duplicates = [label for label, count in Counter(crosswalk_labels).items() if count > 1]
    if duplicates:
        raise ValueError(f"Duplicate MAST labels in crosswalk: {duplicates}")

    crosswalk_set = set(crosswalk_labels)
    missing = sorted(dataset_labels - crosswalk_set, key=label_sort_key)
    if missing:
        raise ValueError(f"Missing MAST labels in crosswalk: {missing}")

    unexpected = sorted(crosswalk_set - dataset_labels, key=label_sort_key)
    if unexpected:
        raise ValueError(f"Unexpected MAST labels in crosswalk: {unexpected}")

    if set(definitions) != dataset_labels:
        raise ValueError(
            "Definitions file labels do not match dataset labels: "
            f"definitions={sorted(definitions, key=label_sort_key)} "
            f"dataset={sorted(dataset_labels, key=label_sort_key)}"
        )


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def pair_enterprise_interpretation(family_a: str, family_b: str) -> str:
    if family_a == family_b:
        return SAME_FAMILY_INTERPRETATIONS[family_a]

    key = tuple(sorted((family_a, family_b)))
    return FAMILY_PAIR_INTERPRETATIONS.get(
        key,
        "Multiple control-family failures compound into higher review load and weaker containment.",
    )


def load_dataset(dataset_path: Path) -> list[dict]:
    data = json.loads(dataset_path.read_text())
    if not isinstance(data, list) or not data:
        raise ValueError(f"Dataset {dataset_path} is empty or malformed.")
    return data


def build_label_stats(
    data: list[dict],
    definitions: dict[str, str],
    crosswalk_by_label: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    total_traces = len(data)
    failing_traces = sum(
        1 for row in data if any(row["mast_annotation"].values())
    )
    label_counts = Counter()

    for row in data:
        for label, is_active in row["mast_annotation"].items():
            if is_active:
                label_counts[label] += 1

    rows = []
    for label in sorted(definitions, key=label_sort_key):
        count = label_counts[label]
        rows.append(
            {
                "mast_label": label,
                "mast_name": definitions[label],
                "control_family": crosswalk_by_label[label]["control_family"],
                "trace_count": str(count),
                "trace_share_all": format_share(count / total_traces),
                "trace_share_failing": format_share(
                    count / failing_traces if failing_traces else 0.0
                ),
            }
        )
    return rows


def build_pair_stats(
    data: list[dict],
    crosswalk_by_label: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    failing_traces = sum(
        1 for row in data if any(row["mast_annotation"].values())
    )
    pair_counts = Counter()

    for row in data:
        active = sorted(
            [label for label, is_active in row["mast_annotation"].items() if is_active],
            key=label_sort_key,
        )
        for label_a, label_b in combinations(active, 2):
            pair_counts[(label_a, label_b)] += 1

    rows = []
    for (label_a, label_b), count in sorted(
        pair_counts.items(),
        key=lambda item: (-item[1], label_sort_key(item[0][0]), label_sort_key(item[0][1])),
    ):
        family_a = crosswalk_by_label[label_a]["control_family"]
        family_b = crosswalk_by_label[label_b]["control_family"]
        rows.append(
            {
                "label_a": label_a,
                "label_b": label_b,
                "pair_count": str(count),
                "pair_share_failing": format_share(
                    count / failing_traces if failing_traces else 0.0
                ),
                "family_a": family_a,
                "family_b": family_b,
                "enterprise_interpretation": pair_enterprise_interpretation(
                    family_a, family_b
                ),
            }
        )
    return rows


def build_benchmark_stats(data: list[dict]) -> list[dict[str, str]]:
    totals = Counter()
    failing = Counter()
    label_sums = Counter()

    for row in data:
        benchmark = row["benchmark_name"]
        active_labels = [label for label, is_active in row["mast_annotation"].items() if is_active]
        totals[benchmark] += 1
        if active_labels:
            failing[benchmark] += 1
            label_sums[benchmark] += len(active_labels)

    rows = []
    for benchmark in sorted(totals):
        failing_count = failing[benchmark]
        rows.append(
            {
                "benchmark_name": benchmark,
                "total_traces": str(totals[benchmark]),
                "failing_traces": str(failing_count),
                "failure_rate": format_share(failing_count / totals[benchmark]),
                "avg_active_labels_in_failing_traces": format_average(
                    label_sums[benchmark] / failing_count if failing_count else 0.0
                ),
                "enterprise_relevance": BENCHMARK_RELEVANCE[benchmark],
                "notes": BENCHMARK_NOTES[benchmark],
            }
        )
    return rows


def build_system_stats(
    data: list[dict],
    definitions: dict[str, str],
) -> list[dict[str, str]]:
    totals = Counter()
    failing = Counter()
    label_sums = Counter()
    labels_by_system = defaultdict(Counter)

    for row in data:
        system = row["mas_name"]
        active_labels = [label for label, is_active in row["mast_annotation"].items() if is_active]
        totals[system] += 1
        if active_labels:
            failing[system] += 1
            label_sums[system] += len(active_labels)
            for label in active_labels:
                labels_by_system[system][label] += 1

    rows = []
    for system in sorted(totals):
        top_labels = ", ".join(
            f"{label} {definitions[label]}"
            for label, _ in labels_by_system[system].most_common(3)
        )
        rows.append(
            {
                "mas_name": system,
                "total_traces": str(totals[system]),
                "failing_traces": str(failing[system]),
                "failure_rate": format_share(failing[system] / totals[system]),
                "avg_active_labels_in_failing_traces": format_average(
                    label_sums[system] / failing[system] if failing[system] else 0.0
                ),
                "notes": f"Top labels: {top_labels}.",
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Derive tracked MAST statistics from the local ignored raw dataset."
    )
    parser.add_argument("--dataset", required=True, type=Path)
    parser.add_argument("--definitions", required=True, type=Path)
    parser.add_argument("--crosswalk", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    data = load_dataset(args.dataset)
    dataset_labels = set(data[0]["mast_annotation"])
    definitions = parse_definitions(args.definitions)
    crosswalk_rows = read_crosswalk(args.crosswalk)
    validate_crosswalk(crosswalk_rows, definitions, dataset_labels)
    crosswalk_by_label = {row["mast_label"]: row for row in crosswalk_rows}

    args.output_dir.mkdir(parents=True, exist_ok=True)

    write_tsv(
        args.output_dir / "mast_label_stats.tsv",
        LABEL_STATS_COLUMNS,
        build_label_stats(data, definitions, crosswalk_by_label),
    )
    write_tsv(
        args.output_dir / "mast_pair_stats.tsv",
        PAIR_STATS_COLUMNS,
        build_pair_stats(data, crosswalk_by_label),
    )
    write_tsv(
        args.output_dir / "mast_benchmark_stats.tsv",
        BENCHMARK_STATS_COLUMNS,
        build_benchmark_stats(data),
    )
    write_tsv(
        args.output_dir / "mast_system_stats.tsv",
        SYSTEM_STATS_COLUMNS,
        build_system_stats(data, definitions),
    )


if __name__ == "__main__":
    main()
