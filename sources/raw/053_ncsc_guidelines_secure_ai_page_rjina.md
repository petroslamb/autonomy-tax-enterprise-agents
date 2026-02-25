Title: Guidelines for secure AI system development

URL Source: http://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development

Published Time: Invalid DateTime

Markdown Content:
Guidelines for secure AI system development - NCSC.GOV.UK
===============

Cookies on this site
--------------------

We use some essential cookies to make this website work.

We’d like to set additional cookies to understand how you use our website so we can improve our services.

Accept optional cookies

Reject optional cookies

[Manage Cookies (opens in a new tab)](http://www.ncsc.gov.uk/section/about-this-website/cookie-policy)

![Image 1](blob:http://localhost/64e53101f33ddad63dfc824f30c60d73)

Written for
-----------

This section shows the list of targeted audiences that the article is written for

Close

[Skip to main content](http://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development#main)[![Image 2: National Cyber Security Centre - Home](https://www.ncsc.gov.uk/images/library/Primary%20Logo.svg)](http://www.ncsc.gov.uk/)

*   [ABOUT NCSC](http://www.ncsc.gov.uk/section/about-ncsc/what-we-do)
*   [REPORT AN INCIDENT](https://report.ncsc.gov.uk/)
*   [CONTACT US](http://www.ncsc.gov.uk/section/about-this-website/contact-us)

Menu

[Home](http://www.ncsc.gov.uk/)[Advice & guidance](http://www.ncsc.gov.uk/section/advice-guidance/you-your-family)[Respond to a cyber attack](http://www.ncsc.gov.uk/section/respond-recover/you)[Find a product or service](http://www.ncsc.gov.uk/section/products-services/overview)[Education & skills](http://www.ncsc.gov.uk/section/education-skills/schools)[News](http://www.ncsc.gov.uk/section/keep-up-to-date/ncsc-news)

guidance

![Image 3](blob:http://localhost/85c8b3f50aa9757314e17b5d82a4fccf)

Copied to clipboard

##### Share

![Image 4: Facebook](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/Facebook.695a42932737575e03881b3dae4c729f.svg)
##### Facebook

![Image 5: Linkedin](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/Linkedin.9c46437a494eb1e6c877fc3e1634aa99.svg)
##### Linkedin

![Image 6: X](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/x-icon-black.8bab2404a5e5c1a0f3e748f82fdcb2e4.svg)
##### X

![Image 7](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/CopyLink.594f762f40cab3b56f5f0248d0cb306a.svg)
##### Copy Link

Guidelines for secure AI system development
===========================================

Guidelines for providers of any systems that use artificial intelligence (AI), whether those systems have been created from scratch or built on top of tools and services provided by others.

Invalid DateTime

Pages
-----

*   [Guidelines for secure AI system development](http://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development)  
*   [Introduction](http://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/introduction) 
*   [Guidelines](http://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/guidelines)![Image 8: Child links of Guidelines](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/plus.f7f0a93f738ef085af9a08e785b14521.svg)  
*   [Further reading](http://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/further-reading) 
*   [About this document](http://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/about-this-document) 

### Published

27 November 2023

### Reviewed

27 November 2023

### Version

1.0

### Written For

*   [Large organisations](http://www.ncsc.gov.uk/section/advice-guidance/large-organisations) 
*   [Cyber security professionals](http://www.ncsc.gov.uk/section/advice-guidance/cyber-security-professionals) 
*   [Small & medium sized organisations](http://www.ncsc.gov.uk/section/advice-guidance/small-medium-sized-organisations) 
*   [Public sector](http://www.ncsc.gov.uk/section/advice-guidance/public-sector) 

![Image 9](blob:http://localhost/85c8b3f50aa9757314e17b5d82a4fccf)

Copied to clipboard

##### Share

![Image 10: Facebook](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/Facebook.695a42932737575e03881b3dae4c729f.svg)
##### Facebook

![Image 11: Linkedin](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/Linkedin.9c46437a494eb1e6c877fc3e1634aa99.svg)
##### Linkedin

![Image 12: X](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/x-icon-black.8bab2404a5e5c1a0f3e748f82fdcb2e4.svg)
##### X

![Image 13](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/CopyLink.594f762f40cab3b56f5f0248d0cb306a.svg)
##### Copy Link

PAGE 1 OF 9
-----------

Change

Guidelines for secure AI system development

PAGE 1 OF 9
-----------

![Image 14](https://www.ncsc.gov.uk/images/library/iStock-864811702.jpg?mpwidth=545&mlwidth=737&twidth=912&dwidth=635&dpr=1&width=1280)

iStock.com/MF3d

Executive summary
-----------------

This document recommends guidelines for providers of any systems that use artificial intelligence (AI), whether those systems have been created from scratch or built on top of tools and services provided by others. Implementing these guidelines will help providers build AI systems that function as intended, are available when needed, and work without revealing sensitive data to unauthorised parties.

This document is aimed primarily at providers of AI systems who are using models hosted by an organisation, or are using external application programming interfaces (APIs). We urge **all** stakeholders (including data scientists, developers, managers, decision-makers and risk owners) to read these guidelines to help them make informed decisions about the **design**, **development**,**deployment** and **operation** of their AI systems.

* * *

About the guidelines
--------------------

AI systems have the potential to bring many benefits to society. However, for the opportunities of AI to be fully realised, it must be developed, deployed and operated in a secure and responsible way.

AI systems are subject to novel security vulnerabilities that need to be considered alongside standard cyber security threats. When the pace of development is high – as is the case with AI – security can often be a secondary consideration. Security must be a core requirement, not just in the development phase, but throughout the life cycle of the system.

For this reason, the guidelines are broken down into four key areas within the AI system development life cycle: **secure design**, **secure development**, **secure deployment**, and **secure operation and maintenance**. For each section, we suggest considerations and mitigations that will help reduce the overall risk to an organisational AI system development process.

1.   1 
#### Secure design

This section contains guidelines that apply to the design stage of the AI system development life cycle. It covers understanding risks and threat modelling, as well as specific topics and trade-offs to consider on system and model design. 
2.   2 
#### Secure development

This section contains guidelines that apply to the development stage of the AI system development life cycle, including supply chain security, documentation, and asset and technical debt management. 
3.   3 
#### Secure deployment

This section contains guidelines that apply to the deployment stage of the AI system development life cycle, including protecting infrastructure and models from compromise, threat or loss, developing incident management processes, and responsible release. 
4.   4 
#### Secure operation and maintenance

This section contains guidelines that apply to the secure operation and maintenance stage of the AI system development life cycle. It provides guidelines on actions particularly relevant once a system has been deployed, including logging and monitoring, update management and information sharing. 

The guidelines follow a ‘secure by default’ approach, and are aligned closely to practices defined in the [NCSC’s Secure development and deployment guidance](http://www.ncsc.gov.uk/collection/developers-collection/principles), [NIST’s Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf), and [‘secure by design principles’ published by CISA](https://www.cisa.gov/sites/default/files/2023-10/SecureByDesign_1025_508c.pdf), the NCSC and international cyber agencies. They prioritise:

*   taking ownership of security outcomes for customers
*   embracing radical transparency and accountability
*   building organisational structure and leadership so secure by design is a top business priority

* * *

Downloads
---------

[![Image 15: Decorative image](https://www.ncsc.gov.uk/images/library/Guidelines-for-secure-AI-system-development_Page_01.jpg?mpwidth=160&mlwidth=190&twidth=190&dwidth=160&dpr=1&width=1280) * pdf * 2334 KB #### Guidelines for secure AI system development Guidelines for providers of any systems that use artificial intelligence (AI), whether those systems have been created from scratch or built on top of tools and services provided by others.](https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf)

[Next page Introduction](http://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/introduction)

Topics
------

[Artificial intelligence](https://www.ncsc.gov.uk/section/advice-guidance/all-topics?topics=Artificial%20intelligence)

### Published

27 November 2023

### Reviewed

27 November 2023

### Version

1.0

### Written For

*   [Large organisations](http://www.ncsc.gov.uk/section/advice-guidance/large-organisations) 
*   [Cyber security professionals](http://www.ncsc.gov.uk/section/advice-guidance/cyber-security-professionals) 
*   [Small & medium sized organisations](http://www.ncsc.gov.uk/section/advice-guidance/small-medium-sized-organisations) 
*   [Public sector](http://www.ncsc.gov.uk/section/advice-guidance/public-sector) 

![Image 16](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/Chevron_blue_up-CA.0731190020f3afd1faf8227c16c32bfd.svg)

Back to top

Also see
--------

[![Image 17](https://www.ncsc.gov.uk/images/library/mistakes%20ai%20vulnerability%20image.jpg?mpwidth=160&mlwidth=190&twidth=190&dwidth=160&dpr=1&width=1280) NEWS * 10 Dec 2025 #### Mistaking AI vulnerability could lead to large-scale breaches, NCSC warns NCSC raises alert on “dangerous” misunderstanding of emergent class of vulnerability in generative artificial intelligence (AI) applications.](http://www.ncsc.gov.uk/news/mistaking-ai-vulnerability-could-lead-to-large-scale-breaches)

[![Image 18](https://www.ncsc.gov.uk/images/library/sql-confused-robot-20251208.jpg?mpwidth=160&mlwidth=190&twidth=190&dwidth=160&dpr=1&width=1280) BLOG POST * 08 Dec 2025 #### Prompt injection is not SQL injection (it may be worse) There are crucial differences between prompt and SQL injection which – if not considered – can undermine mitigations.](http://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)

[![Image 19](https://www.ncsc.gov.uk/images/library/bugs-bypasses-blog-20250902.jpg?mpwidth=160&mlwidth=190&twidth=190&dwidth=160&dpr=1&width=1280) BLOG POST * 02 Sep 2025 #### From bugs to bypasses: adapting vulnerability disclosure for AI safeguards Exploring how far cyber security approaches can help mitigate risks in generative AI systems](http://www.ncsc.gov.uk/blog-post/from-bugs-to-bypasses-adapting-vulnerability-disclosure-for-ai-safeguards)

[![Image 20: National Cyber Security Centre - Home](https://www.ncsc.gov.uk/images/library/Primary%20Logo.svg)](http://www.ncsc.gov.uk/)

Follow us
---------

*   [![Image 21: X](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/x-icon-white.dfdb617724d1a1616a81ab09162c9f61.svg)](https://twitter.com/ncsc)
*   [![Image 22: LinkedIn](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/Linkedin-white.7fc6ffdd4cd5299bfdd30bdf092c924c.svg)](https://uk.linkedin.com/company/national-cyber-security-centre)
*   [![Image 23: Instagram](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/Instagram-white.6b9082ecdca6cffc915d260d2a6f9d3b.svg)](https://www.instagram.com/cyberhq/)
*   [![Image 24: Threads](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/Threads-white.c5c30824a5aaf010d7caf0a03e3d8a6b.svg)](https://www.threads.net/@cyberhq)
*   [![Image 25: RSS](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/RSS%20feed-white.37e8533f3c9c7708e66115ba5507ef2f.svg)](http://www.ncsc.gov.uk/information/rss-feeds)

ABOUT THIS WEBSITE
------------------

*   [Privacy notice](http://www.ncsc.gov.uk/section/about-this-website/privacy-statement)
*   [Cookies](http://www.ncsc.gov.uk/section/about-this-website/cookies)
*   [Accessibility](http://www.ncsc.gov.uk/section/about-this-website/accessibility)
*   [Terms & conditions](http://www.ncsc.gov.uk/section/about-this-website/terms-and-conditions)
*   [Social media policy](http://www.ncsc.gov.uk/section/about-this-website/social-media-policy)

CONTACT THE NCSC
----------------

*   [Report an incident](https://report.ncsc.gov.uk/)
*   [Report suspicious messages or websites](http://www.ncsc.gov.uk/collection/phishing-scams)
*   [Verify an NCSC contact](http://www.ncsc.gov.uk/guidance/how-to-spot-scammers-claiming-to-be-from-the-ncsc)
*   [Report a vulnerability](http://www.ncsc.gov.uk/information/vulnerability-reporting)
*   [Contact the press office](http://www.ncsc.gov.uk/section/about-ncsc/media-centre)
*   [Can't find what you're looking for?](http://www.ncsc.gov.uk/section/about-this-website/cant-find-what-you-are-looking-for)

USEFUL LINKS
------------

*   [GCHQ](https://www.gchq.gov.uk/)
*   [MI5](https://www.mi5.gov.uk/)
*   [SIS](https://www.sis.gov.uk/)
*   [NPSA](https://www.npsa.gov.uk/)
*   [GOV.UK](https://www.gov.uk/)

Search
------

[](http://www.ncsc.gov.uk/search?q=)

### Popular searches

[Cyber Aware](http://www.ncsc.gov.uk/search?q=Cyber%20Aware)

[Cyber Essentials](http://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=cyber%20essentials&sort=date%2Bdesc)

[CYBERUK](http://www.ncsc.gov.uk/search?q=CYBERUK)

[Passwords](http://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=passwords&sort=date%2Bdesc)

[Phishing](http://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=phishing&sort=date%2Bdesc)

[Ransomware](http://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=ransomware&sort=date%2Bdesc)

![Image 26](http://www.ncsc.gov.uk/static-assets/dist/ncsc/static/media/cross-black.99d3cb23242526c0ef46c0d75ebb8cfd.svg)
