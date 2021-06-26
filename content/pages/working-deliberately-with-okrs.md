Title: Working Deliberately with OKRs
Tags: writing
Date: 2021-06-26 23:32
Category: Writing
Status: hidden
Slug: working-deliberately-with-okrs
 
[gdocs link](https://docs.google.com/document/d/16vL-Q9HrlyG67xTnnZSJqbYJ7Sp-CqQIesN4_5R1L8Y/edit#)

####A Brief History of OKRs (and me)

OKRs as a concept came originally from Intel (where they were called [something different](https://en.wikipedia.org/wiki/OKR)) -- they were introduced early on at Google, and for many years, they’ve survived mostly intact as a thing that most teams (and many individuals) have at Google. 

I was at Google from 2004 to early 2021 - so I have about 16 years of experience of setting personal, team and org-level OKRs (for a team of about 300). There is a reasonable amount of documentation internally about refinements of the process, or org-specific OKR-setting methods -- but that’s not what I’m trying to do here. The main points I’ll address are where OKRs are only a partial fit for the reasons they’re used. To make this document actually useful instead of just complaining, I’ll also set out some of the ways we (and by ‘we’, I mean folks in industry who have, or are looking to adopt OKRs for whatever reason) can do better.


####What Are OKRs?
First of all, I’m going to guess that most people responsible for OKRs have not read the [original book](https://archive.org/details/highoutputmanage00grov) from 1983 they are set out in. I certainly haven’t; I got a primer on them when I started working for an enterprise that had adopted the method -- so for the purposes of fidelity, let me pass it on!

OKRs look a little bit like this (with a cycle being a quarter, or 3 months):

<table width=80%>
  <tr bgcolor="#a1edf3">
    <td>
      <b>O: Here’s something we want to do that will take a few OKR cycles.</b>
      <ul>
      <li><b>KR</b>: Here’s a measurable amount of progress we mean to achieve in this cycle.
      <li><b>KR</b>: Here’s another one.
      </ul>
    </td>
  </tr>
</table>


These could be at the team or individual level. In broad terms, OKRs are the set of promises we make to our stakeholders and ourselves. As a document for ourselves, they help focus us on what’s important for a given planning cycle. For many of us, keeping focused in a high-interrupt, high-paced environment is extremely difficult - we can show up to work each day and run headlong at the first thing to come at us, so having a grounding in a set of promises helps focus, and also acts as a clever shorthand in a number of areas.

If you experience something that’s not in your OKRs, you can use that to start a more in-depth conversation about how it can get in there, and what needs to be bumped out. You have your **O**bjectives, which the new thing may be in service of, which means adjusting or swapping out an expected **K**ey **R**esult. Business realities may mean that you even drop or swap an Objective. However, the main benefit of the approach is that this is a conversation where everyone is speaking the same language about the promises they’ve made to each other, and can make the hard choices about what does or doesn’t get done if there is pressure on.

The other crucial part of the OKR method is that KRs are measurable and scorable - at Google, it’s generally on a scale of 0.0 to 1.0 -- so when writing KRs, you want to make sure to be specific in your goals, rather than everything being either ‘done’ or ‘not done’. I do believe this was responsible for much of Google’s early progress. Rather than saying vague “Let’s try to do this thing” objectives, we made ourselves have KRs like “GMail 7-day active users increases to X”, where X (or X%) would then be used to score the KR afterwards, and aggregate scores upwards.

We’d then take the overall mean scores and come up with one score, either personally or as a team. This number wasn’t used in any direct formulaic way for performance management, but a pattern of misses (or mis-promises) from a team or individual would get noticed as a pattern. 


####Retrospective: 15 years of OKRs

Over time, OKRs started to look more like this:


<table width=80%>
  <tr bgcolor="#e98b62">
  <td>
    <b>O: Ongoing Maintenance [<font color=red>P100</font>]</b> <i>[owner: Sam]</i>
    <ul>
      <li><b>KR</b>: System sustains growth successfully [<font color=red>P100</font>] <i>[owner:all]</i>
    </ul>
    <b>O: Deliver Fibble Project [<font color=orange>P75</font>]</b> <i>[owner: Terry]</i>
    <ul>
      <li><b>KR</b>: Design doc written and approved [<font color=orange>P75</font>] <i>[owner: Terry]</i>
      <li><b>KR</b>: Make progress on proof of concept implementation <i>[owner: Jo]</i>
    </ul>
    <b>O: Try to finish off migration from last cycle [<font color=green>P30</font>]</b> <i>[owner: Sal]</i>
  </tr>
</table>


Okay, this is a pretty egregious example, but the point is that OKRs can easily morph into a couple of things that are not related to promises to other stakeholders.

#### What OKRs Aren’t (And Other Stories)

#####A Planning Tool
As planning tools go, a flat bullet list of things to do for a quarter is ok for an individual to keep track - it’s not so great for a team or organization of any size -- they immediately need more granularity, intra-quarter time tracking, more fine-grained prioritisation, individual assignment to tasks. Maybe the team already has a task planning method, like whatever parts of Agile work for them? In any case, it’s not reasonable to expect that OKRs are even an input to a useful planning tool. If anything, they’re the output. Having over-granular priorities and too much metadata like owners, dependencies, etc. can also encourage mistaking the OKR artifact from the process you should have for planning.

Since OKRs are generally set quarterly, it’s tempting to have a hard-stop cadence for Objectives at the 3-month mark. This can mean that every project ends up only lasting a quarter, or that many of the Objectives are ‘finish off’ type items (see the example as the final O in the list above). Projects take as long as they take, and if there’s a long enough time horizon that you plan to, you should be able to come up with OKRs that indicate progress quarter on quarter -- seeing an O that later morphs into “finish off O” in later quarters is a pretty good signal that a team is using OKRs to do a lot of heavy lifting around project planning, rather than tracking things holistically. This can also prevent a team from thinking more than a quarter ahead.

Working cycle-to-cycle on that boundary for results can also affect other teams’ ability to plan. I more then once spoke to leads for large projects who claimed that to plan beyond 3 months out was an impossibility -- since everyone was planning on 3 month cycles, they could not predict asks from stakeholders in advance, and everything was linked to a ‘big bang’ planning exercise each quarter. While I don’t think it’s true that you can have longer-term plans in this situation, it’s hard not to be sympathetic to the notion when you exist in an ecosystem of teams that do this.

#####A Todo List
If you’re simultaneously trying to formulate KRs that are scoreable and meaningful, and also trying to assign work to folks on a team, the two use cases are antagonistic. KRs describe an outcome -- so if you’re assigning the outcome to a team or individual, the planning of how that gets done immediately shifts to outside the OKRs and into whatever task tracking or planning tool you use (even if it’s post-its).
An Exclusive and Exhaustive Todo List
It’s tempting to try to use OKRs as an excuse to do nothing but what’s on the list -- and in capturing the list of KRs, you try to capture everything you sign off on being done. First, good luck micromanaging people to that extent! Even if people put up with it, you’re likely wasting a lot of your own time doing this, when the fungible nature of priorities in modern tech are so fickle. You could easily end up throwing out all your careful work, or doing something worse like having your team be inflexible to changes in situation.

Trying to make your OKRs be an exclusive list of everything you or your team will do in the planning cycle (no more, no less) is almost always the wrong target. Modern practices always shift priorities mid-cycle, and the effort planning method you use should be resilient to this, and be designed for change and update. This applies in equal measure to OKRs, with the additional benefit being making sure your stakeholders are aware of your promises.

It can also be tempting for each team member to believe that their work is not relevant to the team’s objectives unless they own an Objective or KR listed on the team’s OKRs. Similarly, for folks who own an effort within a team or org, it doesn’t necessarily have to feature in team or org-level OKRs; it’s still valid work as agreed with leadership and stakeholders. Going down the slippery slope of OKRs being an exhaustive and exclusive list generally makes people think this way, and this anti-pattern will be reinforced.


####KRs should be Measurable
I measured, graded and reviewed hundreds of sets of OKRs from teams for over a decade, and this is by far the most common piece of advice I offer. Much of the value of the OKR method is in the specificity of targets. There are a number of examples in the list above of this anti-pattern, such as the “100% or 0%” KR of writing of a design doc, the magical “make progress” phrasing, (which can be scored arbitrarily), or the classic ‘do not fail as a business during this cycle’ catch-all about growth. Even if it feels a little contrived, specific targets are a crucial element to each KR. 100% is a fine target, once the possible outcomes aren’t just that or 0%.
Knowing the Point of OKRs, and The Power of Naming
‘OKRs’, from the outset, is a term doomed to eventual failure if you want a large organisation to immediately know exactly what you mean. It doesn’t mean anything unless you go on to explain it, and as a [mnemonic device](https://en.wikipedia.org/wiki/Mnemonic), it reproduces imperfectly. Yes, it’s an acronym, but it’s an acronym for two businessy phrases that are heavily overloaded.

I’ve had best results when I’m able to phrase things in a way that (a) captures intent and (b) reduces ambiguity. My benchmark for these terms is that if you ask a generally sensible person to ‘bullshit’ an explanation for something given just the name, how close to your intended description would they get?

Objectives are our personal dreams, or our team’s dreams. You don’t put a time-box on them, you keep moving forward until you realise that dream. It doesn’t come true on a quarter boundary, and can morph and change over time.

Key Results are our promises. We set them out, we hold ourselves to them, and we let people know if we think we’re going to break them. In a relationship with stakeholders, it’s helpful to be explicit about chopping and changing our promises, and we should take pride in delivering on our promise, and that it sometimes isn’t everything we were asked for. 

So, why don’t we call them Dreams and Promises? There is power in naming, and in using naming to demystify. I’ll talk more about this in the sections below.


####What’s Changed
What’s changed since the early 80s, when OKRs were first mooted? Turns out, a ton. 

I wasn’t in the workforce in the early 80s, but I’ve learned that as far as planning went, things moved a little slower, but not hugely so. Different business units were able to plan in coordination because they were business units -- they had their own way of doing things, and they were absolutely results-focused, rather than steeped in real-time collaboration or regular checkins. If you were setting OKRs, you’d set them with your partners and stakeholders, and then you might catch up with them 3 months later, and you’d better have those KRs hit!

Today, with the advent of email, instant messaging, cheap and plentiful air travel (at least, pre-COVID), and 40 years of advancement in project management methodologies, the need for OKRs remains -- you do want to set out what you plan to do, and a set of measurable milestones along the way. However, the way it gets done becomes fungible. You end up needing a project/program management methodology that complements your OKRs, and a model that has OKRs as the output (as opposed to the input) of your planning starts to make sense -- project planning isn’t served by being on a cadence when the cadence isn’t driven by anything but the calendar. 

####Doing Better
Having experienced the administration of OKRs on a large and small scale, I think a modern practice is still well-served by them, and much of the benefit is still realised if we’re careful about what they are and what they aren’t. Here are a few suggestions I’d suggest trying if you’re in the nascent stage of OKR method adoption.

#####Maybe….Don’t
First and foremost, you should consider what you’d like to get from OKRs. If you want a lightweight way of tracking objectives and results (or dreams and promises, for that matter!) think about how this would slot into your existing planning practice, if any. If you find yourself getting too far down the nuts and bolts of how to make this happen, remember to keep thinking about the outcome you want and how you’ll measure it (your...Key Result, if you will!). If you lose sight of that, there is always the option to not use OKRs. In the end, it should be a low-overhead augmentation to your existing planning.

#####Naming
There is huge power in naming. If you have an enterprise where the term “OKRs” means essentially nothing and you’re planting that seed, you have the opportunity to do better. 

As I intimated above, my personal favourite I’d love to try is ‘Dreams and Promises’. It’s a little unwieldy, but the names fit a little better if we want to be directive about how OKRs are used and people only have the names, or an [elevator pitch](https://en.wikipedia.org/wiki/Elevator_pitch) of what they’re supposed to be. It passes the “Smart person bullshits the details and is mostly correct” test I describe above.

What are your team’s dreams?

How likely are you to say that your team’s dreams are to do the business as usual tactical stuff? Not likely, and that’s good because those generally don’t belong in OKRs.
How likely are you to say that your team dreams of doing some short-term project that’s been shoe-horned into a quarter-cadence project so we can call it a ‘dream’? Also unlikely, for the same reason. Can you think of something you dream of more? Can you take that quarter-long project and tie it to something more meaningful?

Similarly, If you say your team ‘promises’ to ‘make progress’ on some deliverable, does that sound like a good-quality promise? Is it a promise you’d accept as being meaningful if someone promised you they’d do it? ‘Make progress’ promises nothing, and promising it is counter-productive to the point of having OKRs as an expectation-setting tool.

#####Planning Separately
If you think of OKRs as being the root of your team’s direction and planning focus, I respectfully advise you to think again! Being definite about the direction you’re taking and the incremental outcomes within a given planning cycle are crucial to high-quality outcomes, but these are not by themselves driven by the quality of your OKRs - they are a function of the quality of your planning and prioritisation exercise, and your own leadership in setting a direction for the team (or how you marshal your own time, for individual OKRs).

Rather than thinking about how you’re going to take a set of promises you’ve made and get them done in a quarter, approach what you’re going to do holistically, and think of OKRs as an artifact you should just be able to get your existing planning tooling to spit out. If you end up having to negotiate dropping or adding OKRs, this is essentially an interface into your planning - any amendments to your OKRs are a side-effect of that.





