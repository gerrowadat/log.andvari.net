Title: Disappoint People Early
Tags: writing, sre, leadership
Date: 2026-02-02 12:00
Category: Writing
Slug: disappoint-people-early

One of my favourite phrases to remind people of as I'm fumbling about the business of producing reliable systems is **"We Should Disappoint People Early"**. I've gotten enough funny looks about this that I figure I should explain myself.

The 'polite' assumption most folks make is that we should aim to never disappoint people at all. However, the wisdom is in the timing. If disappointment is coming (and it usually is, somewhere), you want it to arrive early enough that everyone can adjust, rather than late enough to cause real damage.

This applies everywhere: SLOs, product roadmaps, support response times, vendor relationships, and most critically, to the implicit promises we make when we *don't* say anything at all.

### The Implicit Promise Problem

My erstwhile colleague Niall Murphy wrote an excellent piece on [implicit SLOs and their dangers](https://blog.relyabilit.ie/implicit-slos-and-their-dangers/) that crystallises something I've seen over and over. The short version: your users are already forming expectations about your service's reliability, whether you tell them what to expect or not.

If your service has been running at eleventy nines for the past year, your customers have noticed. They've built systems that depend on it. They've made architectural decisions predicated on "this thing is always up." They've stopped building fallbacks. You've made an implicit promise, and you probably didn't mean to.

The problem comes when you need to break that promise. Maybe there's cost-cutting. Maybe there's a re-architecture. Maybe you're just doing some planned maintenance that you've been putting off. Suddenly, you're at three nines instead of eleventy, and your customers are furious -- not because three nines is unreasonable, but because you violated an expectation they'd built up over time.

As Niall puts it: even if you smoothly manage the transition, if you fail 100x more often than you previously did, people are going to notice.

### Why Stating an SLO is Better Than Not Stating One

[The SRE book](https://sre.google/sre-book/service-level-objectives/) makes this point clearly: the business must establish what the availability target is for the system. Not the SRE team, not the platform engineers -- the business, informed by what users will actually tolerate and what makes commercial sense.

[Ben Treynor's observation](https://sre.google/in-conversation/) that "100% is the wrong reliability target for basically everything" is foundational here. You're not running a pacemaker. You get to decide what's reasonable, and more importantly, you get to tell people.

The alternative -- not stating an SLO -- is worse in every way. You've still made a promise; you just don't know what it is. Your customers have inferred one from your historical performance, and it's probably higher than you'd have chosen. You now have all the obligations of a promise without any of the negotiation that should have gone into making it.

You have to make trade-offs. You can't make trade-offs against a number you haven't decided on. When you decide on that number, you then need to staple it to people's faces and let them emote about it early.

### The Same Pattern in Roadmaps

Product roadmaps suffer from exactly the same dynamic. A product team should not make a promise until they've conducted enough discovery work to understand what's truly required, and the only people who can make such a promise are the team responsible for delivering it. The corollary is stark -- if you're making roadmap commitments before you understand what delivery entails, you're setting up a future betrayal.

This is the implicit promise problem wearing different clothes. If you show a customer a roadmap with specific features and dates, you've made a promise. If the business context changes -- and it will -- you're now in the position of either delivering something suboptimal because you committed to it, or "breaking your promise" by adapting to reality.

The fix isn't to hide your roadmap. The fix is to disappoint people early by being explicit about the nature of roadmaps: they're current best guesses, subject to change, and the further out you look, the fuzzier they get. Product leaders who've learned this lesson put "subject to change" disclaimers on everything, use confidence percentages, and replace hard dates with buckets like "Now," "Next," and "Later." Obviously you can hedge too much, but a certain amount of expectation-setting is healthy.

When roadmap planning is treated as a rigid forecast, it creates pressure and distrust. When it's treated as a dynamic, communication-first process, it builds trust and momentum -- even when timelines shift. The early disappointment of "this might change" is infinitely preferable to the late disappointment of "you promised."

### Vendor Relationships and the Shared Responsibility Trap

There's a particularly insidious version of this problem that plays out when companies move from on-premises infrastructure to PaaS or SaaS, in either Security or for provision of a dependency. The [cloud shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) is supposed to be clear: the provider is responsible for security *of* the cloud, while the customer is responsible for security *in* the cloud. In practice, it's a mess of unstated expectations.

[Gartner famously predicted](https://www.cio.com/article/416343/the-top-cloud-security-threat-comes-from-within.html) that through 2025, 99% of cloud security failures will be the customer's fault. This sounds like finger-pointing, but it reflects a deeper truth: when companies adopt cloud services, they often expect the vendor to take over responsibilities that were never part of the deal. They're specifically abdicating duty of care as part of the purchase, but then they treat the new solution as their own personal ops team.

When vendors aren't explicit about what they *won't* do, customers fill in the gaps with optimism. And when something breaks, the disappointment isn't just about the outage -- it's about betrayed expectations that were never actually set. [The NSA and CISA published guidance in March 2024](https://media.defense.gov/2024/Mar/07/2003407863/-1/-1/0/CSI-CloudTop10-Shared-Responsibility-Model.PDF) specifically because so many organisations were accelerating their cloud journeys "without proper planning and an appreciation for shared responsibilities."

This creates an ugly dynamic. If you're a vendor and you're not telling customers what failures to expect, they're going to want the full list of all things that can go wrong. That nervousness translates into demands for breadth-first total coverage of all eventualities. But there are always failures you won't be able to enumerate specifically -- the unknown unknowns, the novel combinations, the things that have never happened before.

The answer is to disappoint early. Be explicit about what's in scope and what isn't. Document the failure modes you *do* know about. Make clear that you can't possibly predict everything, and explain what happens when the unexpected occurs. The discomfort of that conversation now is vastly preferable to a customer discovering during an incident that their assumptions about your service were wrong. It also precludes a lot of demands from those same customers that are driven by vibes and nervousness at not feeling they know enough about potential failure modes and outcomes.

### Support Response Times: The Hidden SLO

Every support team has an SLO, whether they've stated one or not. If you typically respond to tickets within 4 hours, your customers have noticed. They've calibrated their workflows around it. The first time you take 24 hours, they'll be furious -- not because 24 hours is unreasonable in isolation, but because you violated the expectation you accidentally created. This applies also to customers who only open the occasional support request - the feigned surprise that they don't get a 15-minutes response when the SLA is an hour (or more) will be familiar to anyone who's been on a customer support rotation. Customers who open tickets all the time will be more familiar with the expected performance because they've been told more recently.

This is where "disappoint early" becomes almost literal. If you know you can't offer priority support between midnight and 5 AM, say so upfront. If critical issues get faster response than routine questions, publish your priority matrix. If your support capacity means occasional delays during high-volume periods, tell people before they need help, not after they've been waiting.

### Internal Customers Too

This isn't just about external customers. The same dynamic plays out inside your organisation, often more acutely.

If you're a platform team that offers services internally, your internal customers (the product teams) are forming expectations about your services just as external customers would. If you've been accidentally excellent at something -- say, keeping your deployment pipeline at sub-minute latencies -- you've now made an implicit promise. The moment that slips to five minutes because you've added some necessary safety checks, you'll hear about it.

The conversation is much easier if you've stated up front: "We target 95th percentile deploy times under 5 minutes." Now there's a conversation to be had. Maybe 5 minutes isn't good enough for some use cases. Maybe it's plenty. But at least everyone knows what they're working with.

Similarly with stakeholders and leadership. If you're asked "when will this be done?" and you say "soon" or "we're working on it," you've allowed them to fill in their own number. That number will be wrong, and it will be too optimistic. The disappointment arrives later, bigger, and with compound interest.

Saying "this will take four weeks" might disappoint someone today. But that disappointment is manageable. They can plan around it. They can reprioritise. They can have the argument about whether four weeks is acceptable *now*, when there's still time to do something about it.

### The Discomfort is the Point

Stating an SLO feels uncomfortable precisely because it's a commitment. The same is true for publishing a support response time matrix, or putting "subject to change" on a roadmap, or listing the failure modes your SaaS platform *won't* protect against. Each of these forces you to confront the reality that you can't be all things to all people. It makes explicit something that was previously implicit and negotiable.

That discomfort is valuable. It's the discomfort of honesty. And it's far preferable to the discomfort of a customer discovering during an outage that your service wasn't as reliable as they'd assumed, or finding out during an incident that their cloud vendor doesn't cover what they thought it did, or learning that the feature they were counting on got deprioritised.

The core of "disappoint early" is this: small disappointments now prevent large disappointments later. An SLO that seems modest compared to your historical performance might disappoint a customer today. A roadmap that says "this might change" feels less confident than one with firm dates. A vendor contract that explicitly lists what's out of scope seems less comprehensive than one that doesn't mention limitations at all.

But in each case, the explicit version creates space for honest conversations about what they actually need, what you can actually deliver, and what happens when those don't align. The implicit version creates the illusion of agreement that shatters on first contact with reality.

### So.

If you're running a service without a stated SLO, you've already made a promise -- you just don't know what it is. Your customers have inferred one, and it's probably more optimistic than you'd like.

If you're sharing a roadmap without caveats about uncertainty, you've created expectations you may not be able to meet.

If you're a vendor who hasn't explicitly documented what failures customers should expect, they're filling in the blanks with assumptions that will turn into accusations when something goes wrong.

If you're working with stakeholders without explicit expectations about timelines, support responsiveness, or capabilities, you've allowed them to assume. Those assumptions will bite you.

The fix is the same in every case: have the uncomfortable conversation now. State what you can actually commit to. Document what's out of scope. Put confidence levels on your forecasts. Publish your priority matrix. Be boringly, repetitively explicit about constraints and limitations.

It's often a good idea to overcompensate when communicating constraints or expectations that may be 'disappointing.' The customer who understands your limitations upfront is a customer who can plan around them. The customer who discovers them during a crisis is a customer you're about to lose.

It's paradoxical, but the path to being a more reliable partner -- to your customers, your stakeholders, your colleagues -- runs directly through being willing to disappoint them sooner.
