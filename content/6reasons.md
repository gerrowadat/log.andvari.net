Title: 6 Reasons You Don't Need an SRE Team
Tags: writing, sre
Date: 2023-06-21 05:40
Category: Writing
Slug: 6reasons
 

The last several years have seen a huge upsurge in the popularity of the DevOps/SRE/Production Engineering model, with companies large and small adopting some of the practices and mindsets. One of the principal lessons many of these organisations (hopefully) learned was that it's close to impossible to adopt the SRE model as described by Google in the the first [SRE book](https://sre.google/sre-book/table-of-contents/). It's a good approach to take on board the parts of the book that work for you, and to actively triage your time, energy and effort.  

However, one premise doesn't see a lot of investigation or introspection -- that is, whether you should even have an SRE team at all. The existence of SRE (or "DevOps", or "Production Engineering", or "Platform Trust", or any of the other taxonomic manoeuvres I've seen) is still treated somewhat as a given.

This can be for a number of reasons -- there's a pre-existing "Operations" team, there's a strong leadership advocate, or the skills exist in the organisation and it's considered good to consolidate them. It can also often be for less good reasons; pure organisational momentum, a desire to silo-ise toil, and for reactionary reasons.

The arguments for having an SRE team can often seem obvious: Everyone likes having reliable systems; it's hard to argue against that. Everyone also likes someone else doing the hard bits. So, let's cover the counterpoint: 6 Reasons you shouldn't have an SRE team.

### 1. You're not Google

Even though Google's approaches to parts of the problem space are battle-tested and can help you with your approach, you're still not Google. You're not even Google in 2004.  

As someone who was at Google in 2004, I will let you in on the secret sauce that made a large SRE team at Google a good idea.

#### Intractable Problems

Two factors drove the near-intractability of the situation Google found itself in around this time: Scale and Innovation. These sound like lovely soundbites, but the truth of the matter was that nobody was doing anything even remotely like what Google were doing at this time. Nobody had the same requirements.

In my last gig before Google, we were using [nagios](https://www.nagios.org/) and [mon](https://sourceforge.net/projects/mon/). None of these sharded in any way that would work for us; they were designed for monitoring well-understood things about a few hundred hosts. At the time, Google had a couple of hundred thousand hosts, and were adding thousands more per month. Nothing in either the OSS world or that you could buy was even going to come close. There was no Prometheus, no Docker, no Terraform, and these wouldn't exist in any meaningful way for another 10+ years. 

We had to build, deploy and somehow keep together things at a scale and complexity (related to the tools available) that we had never before seen in our lifetimes and likely will never see again. This meant that simply hiring buildings full of operators wasn't going to work at all. This was plainly obvious -- even back of envelope calculations showed a scaling vector that meant we'd run out of humans in pretty short order.

#### Unlimited Money

I'm not a finance person, but it's difficult to express just how much Google was able to invest  around the software ecosystem. Everything from the hardware and cooling to the  monitoring software and job scheduler was built in-house. This was mostly because of the "Intractable Problems" thing, but also because we could afford to. In many cases, we'd be fools not to; the industry in certain areas wasn't moving fast enough, or even in the right direction for us. Compartmentalising the big-picture reliability problems into a group that we could build or hire the best SREs on the planet into was a no-brainer.

To briefly get off the Google fanboy train and go back to the crux of the point: You're not Google. I don't mean that your product isn't a great product, or that you don't have real problems. I'm saying that the criteria you use to evaluate whether you need a full-blown SRE presence should be specific to you. In your checklist of things to potentially adopt from Google’s model, include an item about having a separate team at all.

(Also, you're not Google in 2004. If I want a reliable sharded database with global consistency today, I can buy it and have it today, using money. This was not even close to true in 2004)  

### 2. You don't care that much about reliability.

It's very easy to say you care about reliability, and very difficult to figure out and assert how much you actually care. Even if you have a good set of SLIs and SLOs, that's not the whole picture of 'how much' you care. Is reliability so important to you that you need a whole entire team just to care about it? What about testing? Product Research? Customer feedback loops? Why did SRE get to the top of the list?

It's easy to assert that near-perfect reliability will drive user retention. It's very difficult to be so sure of your product's use case that you can put a number on how much unreliability you can tolerate. Saying "We're not a stock exchange, our users will tolerate 5 minutes of downtime every so often" is a strong thing to be able to assert; stronger and more rigorous than saying you need eleventy nines for your applications at all times.  

[This quote](https://artdiamondblog.com/archives/2013/10/_source_levy_st_19.html) from Steven Levy's book on how earlier Google worked epitomises what was heard loud and clear throughout engineering. I once had Eric Schmidt visit my team's weekly meeting (I was on GMail SRE at the time), and the money quote was his response to a question about prioritising reliability vs. product features -- "I will choose reliability, every time". We framed that quote in our team area. Even to the jaded sysadmins and hackers we often saw ourselves as at the time, it was a clear message that reliability was a product feature, all the way from co-founder to CEO to us.

Is your CEO saying these things? Even behind closed doors? What about when you're under pressure to ship features? 

The extent to which Google really, genuinely cared about reliability and made the company-level investment in it can often be forgotten - think about if you're there with them.

### 3. You're not sure what the team should do or own.

If you’re not able to very succinctly explain and have everyone understand what a team like SRE is there for, then the ambiguity and ability to re-legislate who does what is often quietly seen as an advantage.

Some places have this right; many places don't. If a team is chartered and has a remit, that remit should be set in stone and the requisite effort put in place to maintain that knowledge. In [my talk at SRECon Europe 2022](https://www.youtube.com/watch?v=zIHVordrtBc) I go into a bit of detail about stakeholders. It's been my personal experience that Stakeholders (i.e. product owners, dev partners, company leadership) either misunderstand or make it their business to misunderstand what an SRE group should be doing..  

Even at Google (that wonderful flawless bastion of enlightened thought on the matter), I routinely ran into folks at VP level and above who didn't really know where their team's remit ended and SRE began, and really weren't inclined to learn. Free labour is free labour.

If you're not 100% sure what SRE (or any team, for that matter!) exists for, what it will do, and why it's a separate team, then you should strongly consider whether it being a separate team is a good idea. 

### 4. You're doing it to avoid internalising inconvenient truths

#### Understanding reliability is everyone's job

If you, or engineering leads who work in your org don't think so, then hiring a separate team to care about it isn't going to help.

There is a continuing meme within software that I personally don't understand -- the idea that software can be produced to spec and then disappears into the ether. It existed to an extent in the area of software being shipped on Floppies/CDs/DVDs/tarballs, where the turnaround on bug reports, releases, patches, etc. was measured in development cycles. However, it has somehow survived into the era of there being exactly one running installation of your software that you care about.

I can understand how a team might shard the effort of day-to-day running of their software; I have less time for the idea that the entire ecosystem of care can be put on another team.

#### Low-value work

Reliability engineering is widely viewed as low-value work. Even if leadership is bought in, the meme is extremely prevalent at all levels of product engineering.

The usual response from many folks in Ops and SRE roles would be to say that it's not -- it's crucial to system reliability and customer trust, and so forth.

The good news is that you can both be right!

Further to my [article on oncall being a waste of time](https://www.usenix.org/publications/loginonline/oncall-equal-opportunity-waste-time), I'm here to make a humble request that people say this quiet part out loud. If it's the honest assessment of an engineer or leader that work is of low value, that actually forms the basis of a *very* interesting conversation to be had about priority and how this toil gets looked after. Some of the most stressed and least valuable SRE engagements I've seen were ones where people were talking past each other, with nobody acknowledging what everyone knew; that nobody wants to do this work, and it should be eliminated. The convenient presence of an SRE team means the conversation can often go around in circles. Speaking of which...

#### 5. Your SRE team might be a red herring

Further to the above post about low-value work; another anti-pattern which means you should be very sure about your SRE team's remit is that they are a convenient outlet for lack of planning or responsibility on the part of other groups.

Even in a "you build it, you run it" shop, it's possible to indefinitely delay and defer platform reliability or modernisation work, on the grounds that an SRE team should either be doing this work wholesale, or assisting. It's a very easy position to take, that has the side-effect of deflecting responsibility from a product or service owner onto an SRE group. I've seen cases where the SRE group hasn't even been asked to do the work, this deflecting responsibility onto...nobody.

Would this happen if you were able to be 100% sure that everyone at your company completely understands SREs remit and has no issues with it? No!

Would it happen if you didn't have an SRE team at all? Also No!

#### 6. You got a big fright

We've established that it's difficult to put your finger on how much you care about reliability. Even if you have done the work and really have a good handle on this; you may be one giant outage away from throwing that all away on optics.

As a thought experiment: go and corner your nearest C\[TE\]O and ask them how much they care about reliability. It's probably a lot, right  

Now, go ask them again the day after a multiple-hour outage. Now it's definitely a lot!

SRE as a brand is a double-edged sword -- it can be seen as a panacea for reliability problems, when often it's a more intrinsic cultural investment. I have personally seen SRE groups appear almost overnight, or have money/headcount thrown at them because we had some big outages and this is an audacious hail-mary pass of a move that really shows you care about reliability. If you're not careful, you could be telling your customers you care about reliability, while telling your products developers and leadership that they don't have to.

### Conclusion

The model of large SRE teams covering many services in a vague and nebulous way that's open to repeated re-interpretation is mostly a side-effect of (a) cargo-culting the building of these large groups, or (b) retrofitting SRE/DevOps onto existing groups without the company-wide reliability focus required (or the fortitude to decide you didn't need such a large group to do SRE).

Most of the reasons Google built a large SRE presence were related to being better-equipped to throw money at all its problems than most companies in the last 100 years, and due to the utter absence of big parts of the software and hardware infrastructure needed to build reliable services.

The last 20 years have seen enormous advances in the SaaS and infrastructure software space. What was absent is rapidly becoming present; what was esoteric is rapidly becoming generic. To fully realise the SRE model is to reduce complexity, to make rational choices, to buy because you don't need to build.

The next stage in removing our production training wheels as an industry is to tear down the fence between SRE and Product Engineering, and make rational investments in reliability as a mindset, based on specific needs.
