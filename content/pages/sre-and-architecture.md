Title: Production, SRE and the Architecture of the Built Environment
Tags: writing
Date: 2023-02-15
Category: Writing
Status: hidden
Slug: sre-and-architecture
 
>"We create our buildings and then they create us. Likewise, we construct our circle of friends and our communities and then they construct us." 
>    *-- Frank Lloyd-Wright (1867-1959)*

We live in production -- our practices, customs and very culture are designed by us, but then also inform our capabilities and practice. Despite how our SRE practice might be designed or set out, those surroundings inform our ability to make forward progress, and our collective desire to do so.

People become attached to tooling, to processes, to the structure, and also often to the anti-patterns.

I will give a real example: I once spoke to an engineering leader about an SRE-style engagement for their feature. I asked about current levels of toil and what might be acceptable -- they said that the system paged only maybe twice a week. This was a deal-breaker for me and my team, which shocked the product lead: they had lived around systems with a baseline level of paging and toil for so long, that getting paged all the time was unremarkable to them. 2 pages a week seemed perfectly normal and part of being alive. It was a concrete post in the middle of their living room. Getting a human to intervene was considered part of the feature.

How we build and interact with our production systems has more than a passing similarity to how we interact with and are defined by the architecture of the buildings and cities around us. The approaches toward building tools and processes to serve people are the same. The architecture must serve people, first and foremost.

> “Vous savez, c'est la vie qui est juste et l'architecte qui a tort” *-- Le Corbusier (1887-1965)*

Life is right, and the architect is wrong. We often find ourselves building systems that we then serve. We create a self-fulfilling feedback loop of toil and of workarounds that can often not actually result in meaningful outcomes as far as reliability goes.

It's easy to consider yourself a hero in the trenches of production, and all the unexpected twists and turns that can result from interacting with it. We sometimes forget that the system serves you -- that life, the human, the people on the teams working within this architecture, are in charge. The robots work for us.

> "You cannot save wonderful towns. You can only save wonderful towns by building new ones." *-- Ludwig Mies Van der Rohe (1886-1969)*

I have often spoken to folks who either look in from outside, or who are inside the SRE/production engineering/DevOps space, and who claim a lack of innovation. I couldn't disagree more.

Everything we have built came from dust -- the vast majority of the systems, patterns, and practices we have built came from nothing within our lifetimes. In the main, they will also return to dust within our lifetimes also. Talk to someone who's been in industry for 20 years about how much difference they've seen -- for the most part, very little has stayed. We are constantly rebuilding, and in the infrastructure/production engineering space, we see near-constant change of practice, of interface, and of thought.

The last several years have seen a huge uptick in systems that were previously seen as supplementary or 'nice to have' -- Incident Management, Retrospective, Process enablement are now all more marketable than they've ever been. These are the tools with which we now build our new architecture of person-centric production.

## In Practice

Writing near the end of the first century B.C.E., Roman architect Vitruvius Pollio identified three elements necessary for a well-designed building: **firmitas**, **utilitas**, and **venustas**. Rendered memorably into English by Henry Wotton, a seventeenth century translator, “**firmness**, **commodity**, and **delight**” remain the essential components of all successful architectural design.

### Firmness

Always present, almost always the least interesting. We want a system to be resilient to failure -- we design in fault tolerance, graceful degradation, load-shedding, and everything the general practice of engineering teaches us. The foundation comes from theory and is built in; it must stand on its own without intervention. Failures here must be addressed aggressively and designed out, rather than picked at piecemeal and manually.

### Commodity/Utility

> "A House is a Machine for living in" -- *Le Corbusier*

Any built environment must meet the functional needs of its inhabitants. Customer focus is often considered the end of this journey, but the developers, builders and operators of complex systems must also be served by the commodity of the system as viewed from inside. It must be beautiful and stand up by itself, but must also be nice to be inside. Think about what operating your system is like. If it's difficult or overly complex, this is an issue with utility, rather than an unavoidable inevitability to be borne stoically. Occasionally throw out your old sofa, or that toaster that keeps going on fire. You have an extinguisher, but that's not the point.

### Delight

It is the nature of humans to build and to produce something that elicits delight. It's not enough that it stand up and be useful. Your customers must enjoy using it, and you must be delighted while producing it. This part is most often completely absent when I talk to people who run complex systems. We frame our experiences living in the houses we built as 'war stories', and compare notes on how best to deal with leaking pipes and often take a kind of perverse pride in the nature of effluvia that sometimes emerges from said pipes. Think about where you'd take your systems so that you are delighted to coexist with them.

## So.

We live and work in our systems. If we want the three principles above to be core parts of these systems, the first people to ask permission from is ourselves. Do we question the steel column or load-bearing wall we walk around every day as a fact of life, or demand utility and delight of use for ourselves?

We are the designers; the things we build are that way intentionally. Whether we consider the needs of ourselves or the people who live in our designs is entirely up to us.
