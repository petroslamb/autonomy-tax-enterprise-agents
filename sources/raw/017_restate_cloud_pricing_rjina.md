Title: Restate Cloud | Restate

URL Source: http://www.restate.dev/cloud/

Markdown Content:
Restate Cloud | Restate
===============

[](http://www.restate.dev/)

3.5k

[Cloud Login](https://cloud.restate.dev/)[Get Started](https://docs.restate.dev/quickstart)

[Docs](https://docs.restate.dev/)[Use Cases](http://www.restate.dev/use-cases)[Restate Cloud](http://www.restate.dev/cloud)

Company

[Blog](http://www.restate.dev/blog)

3.5k

[Cloud Login](https://cloud.restate.dev/)[Get Started](https://docs.restate.dev/quickstart)

Build innately resilient distributed apps — without the complexity tax.

© 2026 Restate. All rights reserved.

Product

*   [Documentation](https://docs.restate.dev/)
*   [Restate Cloud](http://www.restate.dev/cloud)
*   [Pricing](http://www.restate.dev/cloud#pricing)
*   [What is durable execution?](http://www.restate.dev/what-is-durable-execution)

Company

*   [Team](http://www.restate.dev/team)
*   [Careers](http://www.restate.dev/careers)
*   [Contact](http://www.restate.dev/contact)

Legal

*   [Terms](http://www.restate.dev/terms-and-conditions)
*   [Privacy](http://www.restate.dev/privacy)
*   [Imprint](http://www.restate.dev/imprint)

[](https://github.com/restatedev/restate)[](https://x.com/restatedev)[](https://www.linkedin.com/company/restatedev/)[](https://discord.restate.dev/)[](https://slack.restate.dev/)

Restate Cloud
=============

Rapidly build agents, workflows, event pipelines, and stateful serverless orchestration.

Keep deploying your code the same way you used to.

Restate Cloud handles resilience, observability, and scalability for your code, with no additional infra.

[Get started for free](https://cloud.restate.dev/)[See Pricing](http://www.restate.dev/cloud/#pricing)

Run your code as Serverless Functions...

AWS Lambda

Cloudflare Workers

Vercel Functions

Deno Deploy

... or as containers

Kubernetes

AWS ECS / Fargate

Google Cloud Run

KNative

Observe everything
------------------

See **status**, **failures**,**intermediate steps**, **state**, and**timelines**.

Inspect workflows, find root cause errors, see who waits for whom.

![Image 1: Overview of invocations](http://www.restate.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcloud_ui.dad97c4e.png&w=3840&q=100)

Transactional, Resilient, Secure
--------------------------------

### Built for resilience and correctness

Restate's runtime powers use cases from AI agents to financial transactions.

[learn more →](http://www.restate.dev/use-cases)

### Compliance

We maintain strong security controls and processes to keep applications safe and running.

[learn more →](https://trust.restate.dev/)

### Client-side encryption

Optionally encrypting data client-side means Restate Cloud can never see your data. Deploy a secure endpoint to support observability and debugging via the UI.

[learn more →](https://github.com/restatedev/journal-encryption)

Stellar Local Dev Experience
----------------------------

Terminal

❯restate cloud login

❯restate cloud env configure neil/my-env

❯restate cloud env tunnel

❯_

**Single binary**

Full-fledged local runtime for development.

**Cloud tunneling**

Develop and debug easily by connecting code on your laptop directly to Restate Cloud.

**Just plain code**

Develop, run, and debug with the same tools you are used to.

Pricing
-------

| Plan | ### Free Free [Get Started](https://cloud.restate.dev/) | ### Starter $75 per month [Get Started](https://cloud.restate.dev/) | ### Business $300 per month [Get Started](https://cloud.restate.dev/) | ### Premium $1000 per month [Get Started](https://cloud.restate.dev/) | ### Enterprise Custom [Contact Sales](https://cal.com/team/restate/team) |
| --- | --- | --- | --- | --- | --- |
| Included Actions | 50k actions | 5m actions | 20m actions | 50m actions | Custom |
| Additional Actions | 25$ / million | 25$ / million | 25$ / million | 25$ / million _(with volume discounts)_ | Custom _(with volume discounts)_ |
| Throughput _(Burst)_ | 5 actions/sec _(50 actions/sec)_ | 5 actions/sec _(50 actions/sec)_ | 20 actions/sec _(150 actions/sec)_ | 50 actions/sec _(500 actions/sec)_ | Up to 100,000s actions/sec |
| Included Storage (for Virtual Objects) | 1 GB | 5 GB | 20 GB | 50 GB | Custom |
| Retention time | 1 day | 1 day | 3 days | 7 days | Custom |
| Support | Community _(Discord / Slack)_ | Community _(Discord / Slack)_ | Email _(Business Hours)_ | Dedicated Slack Channel _(Business hours, 2h response time)_ | Enterprise Support _P0 24/7 30 min response_ |
| SLAs | best effort | 99.9% | 99.9% | 99.9% _(99.99% multi-AZ)_ | 99.99% |
| Client-side Encryption available | ✓ | ✓ | ✓ | ✓ | ✓ |
| HIPAA BAA available |  |  | + $300 | + $300 | ✓ |
| Multi-AZ redundancy |  |  | + $200 | + $500 | ✓ |
| OTEL exports (Datadog, etc.) _(coming up...)_ |  |  | ✓ | ✓ | ✓ |
| SAML SSO _(coming up...)_ |  |  |  | ✓ | ✓ |
| Security review, MSA, legal redlining |  |  |  |  | ✓ |
|  | [Get Started](https://cloud.restate.dev/) | [Get Started](https://cloud.restate.dev/) | [Get Started](https://cloud.restate.dev/) | [Get Started](https://cloud.restate.dev/) | [Contact Sales](https://cal.com/team/restate/team) |

### Actions

#### What is an action?

**Durable actions** are the basic unit of accounting in Restate Cloud:

*   •Function invocation
*   •Intermediate step (`ctx.run(...)`)
*   •Awaiting event (`ctx.awakeable()`or`ctx.promise()`)
*   •Durable sleep (`ctx.sleep()`)
*   •RPC (`ctx.serviceClient(...).run(...)`)
*   •Function completion

State access and updates (`ctx.get(...)`/`ctx.set(...)`) are not measured actions.

#### Additional action prices

up to 50m:included in Premium Plan

50m - 100m:15$ / 1m actions

100m - 200m:10$ / 1m actions

200m+:Contact us

Contact Sales
-------------

Want to talk to a human instead? Excited about Restate Cloud, but none of the tiers quite match? Looking for an enterprise plan?

Reach out to us and we are happy to discuss your needs.

[Contact us](https://cal.com/team/restate/team)

Ready to get started?
---------------------

Create your first Restate environment and start building innately resilient apps.

[Get Started for Free](https://cloud.restate.dev/)[Signup for Updates](http://www.restate.dev/newsletter-signup)

×

### Contact Us

Fill out the form below and our team will get in touch with you.

Loading contact form...

Note: this form might not show in Firefox. If that happens, please try another browser.
