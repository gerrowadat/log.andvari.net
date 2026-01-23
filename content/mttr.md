Title: Chasing Boring at Just the Right Speed
Tags: sre, incidents, leadership
Date: 2026-01-22 12:00
Category: Writing
Slug: no-mttr

### Asking the Right Questions

A while back when I was looking for a fulltime gig (and when I was contracting, of course), I had the opportunity to do a bunch of interviews (including the kind of informal boilerplate interviews you do to get a new contracting client). One of my boilerplate questions when asked "Any questions for me?" has always been "What does success look like for the person in this role?". I like to ask it of everyone, even folks who'd be reporting to me or folks far away on the oarg chart. It gives you a good insight into how stitched together the team is on the important bits, I find.

In the majority of cases, I tended to get at least one answer that boils down to "Fewer Outages, Lower MTTR".

"Fewer Outages", to me, is a weird one. I tend to respond to a "There are too many outages" complaint by asking "Well, how many is too many?". Just like [100% is the wrong SLO target for basically everything](https://sre.google/in-conversation/), "None" isn't the right target for number of outages. You take a reasonable and data-informed swag and aim for that. In [the vast majority of cases](/6reasons.html), you're not running a nuclear power plant or a circulatory system, so you get to really think about what number is right.

Similarly, for MTTR (Mean Time To Recovery, or 'how long in seconds it takes you to mitigate the effect of an outage') the last while has seen a "race to the bottom". There are entire companies whose premise for what they'll do for you (and charge you a handsome fee, to boot) is lower your MTTR. They'll generally do it using an AI chatbot (and strand your systems knowledge and capability inside that same bot), but that's neither here nor there - the main gist is "MTTR is your problem", and it's a tempting one to latch onto. Easy to measure, easy to be seen to be grumpy about.

### Doing it the Fastestest

The problem is that MTTR, as a primary focus, is a red herring. It's measuring the wrong thing; or at least, it's measuring something that's downstream of what you actually want.

If you're having the same kinds of outages over and over, getting really fast at recovering from them is like getting really good at bailing water out of a leaky boat. Sure, you're staying afloat, but water coming in is a bad sign, and you built the boat in the first place so should know what's up.

The real purpose of good incident practice isn't to get fast at recovery. It's to feed back what you learn into your software development lifecycle. Every incident is information. Every outage is telling you something about where your systems, processes, or assumptions are wrong. The goal isn't to recover quickly (though you should); it's to ensure you don't have to recover from the same thing twice.

If you wanted to be a little more philosophical about it (in terms your boss would probably hate), you could say that Outages (like all feedback) are a Gift. You pick yourself up, dust yourself off, and see what there is to learn from the (sometimes pretty shitty) experience.

I waxed slightly lyrical recently about [Cloudflare's writeup](https://blog.cloudflare.com/18-november-2025-outage/) on the outage they had in November 2025. The part that was valuable to me was not a power fantasy about how quickly everyone scrambled and dropped everything and mitigated the outage - in fact, I only checked just now how long the outage lasted (3 hours). I'm not concerned about those 3 hours. Less would be nice, but the real outcome is much more valuable. I'm not even a current Cloudflare customer, but the fact that I know what caused the outage, and I know things have changed means more than a much shorter outage, followed by "Sorry customers, it's very technical, won't happen again (probably)". 

### Doing it The Bestest

When I talk to teams about the point of good incident management (primarily retrospectives), I generally say that the point of doing them is twofold. That is:

#### Avoiding Repeats

If you're seeing repeat incidents -- the same service falling over the same way, the same capacity issues, the same configuration mistakes -- then your incident response process isn't doing its job, no matter how good your MTTR looks. You're optimising for the wrong end of the pipeline.

When you focus too hard on MTTR, you create incentives that work against learning. Teams get good at quick fixes and workarounds. They get good at restarting services and clearing queues. They don't necessarily get good at asking "why did this happen, and what systemic change prevents it from happening again?"

When I worked freelance, I ran into at least one shop that used a managed service partner. Their first instinct was to kick things, seemingly at random. Restart the service. Reboot the machine. Reset the network device.

Their MTRR numbers were *amazing*.

Generally when a particular service fell over, it was back within the hour. However, it was falling over every couple of weeks. When I probed for more information on contributing factors, I got crickets. No followups, no logs, no learning. Clearly there's some slider between "mitigate" and "understand" that makes them somewhat mutually exclusive at either end of the slider.

#### Raising All Boats

Post-incident reviews (or postmortems, or whatever you're calling them this week) should be producing action items that feed into your roadmap. Not just "add better monitoring" (though sure, maybe), but real changes: fix the race condition, add the circuit breaker, change the deployment process. Do a priority swap so we fix something we've identified as real, instead of adding additional whizz-bang that may be more speculative in terms of how happy it makes customers. For bonus points, involve your customer support friends to make sure what you're inserting into the SDLC is actually going to move the needle for customers.

The measure of a mature incident response process isn't how fast you recover. It's how rarely you see the same incident twice, and how much of the learning from your outages sticks, in the form of enduring shifts to how you write code and design systems. It's how often your outages are genuinely novel -- new and interesting failures that teach you something new about your systems, and real action on then finding yourself a better class of first-world problems.

### So

So yes, resolve outages quickly. Absolutely. But don't let MTTR become the thing you're optimising for. The goal is to build systems and processes where you're constantly learning and improving, not systems where you're just really efficient at fighting the same fires over and over.

Your incidents should be novel, and retro outcomes should be real. If they're not, your incident process is failing you, regardless of what your status page says.
