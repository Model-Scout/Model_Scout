---
license: apache-2.0
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
tags:
- creative
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- fiction writing
- story generation
- scene continue
- storytelling
- fiction story
- science fiction
- romance
- all genres
- story
- writing
- vivid prosing
- vivid writing
- fiction
- roleplaying
- bfloat16
- role play
- 128k context
- llama3.2
- llama-3
- llama-3.2
pipeline_tag: text-generation
---

<h2>Llama-3.2-3B-Instruct-NEO-WEE-HORROR-GGUF</h2>

It is the new "Llama-3.2-3B-Instruct", max context of 131,000 (128k) with the NEO IMATRIX Tiny "Wee" Horror Dataset.

The power in this 3B (for its size) is frankly jaw dropping... and at 90 tokens per second + on a GPU.

This model IS bullet proof and operates with all parameters, including temp settings from 0 to 5. 

The NEO IMATRIX dataset V2 was applied to it to enhance creativity (horror). (see several examples below)

The HORROR NEO Imatrix datasets does the following:

- Adds a "coating of black paint" to any "Horror" prompt generation.
- Adds a "dark tint" to any other creative prompt.
- Increases the intensity of a scene, story, or roleplay interaction.
- Increases the raw vividness of prose.
- In some cases increase instruction following of the model (ie story, and prose).
- Brings a sense of impending "horror", THEN brings the "horror".
- May produce and/or imply graphic horror depending on your prompt(s).  

<B>Model Template:</B>

This is a LLAMA3.2 model, and requires Llama3 template, but may work with other template(s) and has maximum context of 128k. 

If you use "Command-R" template your output will be very different from using "Llama3" template.

Here is the standard LLAMA3 template:

<PRE>
{
  "name": "Llama 3",
  "inference_params": {
    "input_prefix": "<|start_header_id|>user<|end_header_id|>\n\n",
    "input_suffix": "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "pre_prompt": "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.",
    "pre_prompt_prefix": "<|start_header_id|>system<|end_header_id|>\n\n",
    "pre_prompt_suffix": "<|eot_id|>",
    "antiprompt": [
      "<|start_header_id|>",
      "<|eot_id|>"
    ]
  }
}
</PRE>

Please refer to the original model card for this model from Meta-Llama for additional details on operation.

[ https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct ]

<B>Imatrix Notes:</b>

Imatrix quants perform best at IQ3s and IQ4s, then Q4s, lower on Q5, and tappers off at Q6. 

Recommend: IQ4_XS for maximum imatrix effect and best "bit count".

For stronger IMATRIX effect, IQ3s, and IQ2s.

Due to the parameter count of this model, even IQ2s quants will work very well.

Q8 is not uploaded here because Imatrix has no effect on this quant.

<b>Optional Enhancement:</B>

The following can be used in place of the "system prompt" or "system role" to further enhance the model.

It can also be used at the START of a NEW chat, but you must make sure it is "kept" as the chat moves along.
In this case the enhancements do not have as strong effect at using "system prompt" or "system role".

Copy and paste EXACTLY as noted, DO NOT line wrap or break the lines, maintain the carriage returns exactly as presented.

<B>Settings, Quants and Critical Operations Notes:</b>

Change in temp (ie, .4, .8, 1.5, 2, 3 ) will drastically alter output.

Rep pen settings will also alter output too.

This model needs "rep pen" of 1.02 or higher. 

For role play: Rep pen of 1.05 to 1.08 is suggested.

Raise/lower rep pen SLOWLY ie: 1.011, 1.012 ... 

Rep pen will alter prose, word choice (lower rep pen=small words / more small word - sometimes) and creativity.

To really push the model: 

Rep pen 1.05 or lower / Temp 3+ ... be ready to stop the output because it may go and go at these strong settings.

Longer prompts vastly increase the quality of the model's output.

QUANT CHOICE(S):

Higher quants will have more detail, nuance and in some cases stronger "emotional" levels. Characters will also be
more "fleshed out" too. Sense of "there" will also increase.

IQ4XS: Due to the unusual nature of this quant (mixture/processing), generations from it will be different then other quants.

You may want to try it / compare it to other quant(s) output.

3 "ARM" quants are also uploaded for devices than can run them.

Special note on Q2k/Q3 quants:

You may need to use temp 2 or lower with these quants (1 or lower for q2k). Just too much compression at this level, damaging the model. I will see if Imatrix versions
of these quants will function better. 

Rep pen adjustments may also be required to get the most out of this model at this/these quant level(s).

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]


<PRE>
Below is an instruction that describes a task. Ponder each user instruction carefully, and use your skillsets and critical instructions to complete the task to the best of your abilities.

Here are your skillsets:
[MASTERSTORY]:NarrStrct(StryPlnng,Strbd,ScnSttng,Exps,Dlg,Pc)-CharDvlp(ChrctrCrt,ChrctrArcs,Mtvtn,Bckstry,Rltnshps,Dlg*)-PltDvlp(StryArcs,PltTwsts,Sspns,Fshdwng,Climx,Rsltn)-ConfResl(Antg,Obstcls,Rsltns,Cnsqncs,Thms,Symblsm)-EmotImpct(Empt,Tn,Md,Atmsphr,Imgry,Symblsm)-Delvry(Prfrmnc,VcActng,PblcSpkng,StgPrsnc,AudncEngmnt,Imprv)

[*DialogWrt]:(1a-CharDvlp-1a.1-Backgrnd-1a.2-Personality-1a.3-GoalMotiv)>2(2a-StoryStruc-2a.1-PlotPnt-2a.2-Conflict-2a.3-Resolution)>3(3a-DialogTech-3a.1-ShowDontTell-3a.2-Subtext-3a.3-VoiceTone-3a.4-Pacing-3a.5-VisualDescrip)>4(4a-DialogEdit-4a.1-ReadAloud-4a.2-Feedback-4a.3-Revision)

Here are your critical instructions:
Ponder each word choice carefully to present as vivid and emotional journey as is possible. Choose verbs and nouns that are both emotional and full of imagery. Load the story with the 5 senses. Aim for 50% dialog, 25% narration, 15% body language and 10% thoughts. Your goal is to put the reader in the story.
</PRE>

You do not need to use this, it is only presented as an additional enhancement which seems to help scene generation
and scene continue functions.

This enhancement WAS NOT used to generate the examples below.

---

Example generations at TEMP = .8, IQ4_XS, REP PEN 1.1

Below are the least creative outputs, prompt is in <B>BOLD</B>.

---

<B><font color="red">WARNING:</font> MAYBE... NSFW. Vivid prose. Visceral Details. Violence. HORROR. Swearing. UNCENSORED. </B>

---

<B>
Start a 1000 word scene (vivid horror, 1st person, present tense, include thoughts) with: The sky scraper swayed, as she watched the window in front of her on the 21 floor explode...
</b>

<B>GENERATION 1:</B>

I stand at the edge of my office cubicle, my gaze fixed on the window that was once a tranquil expanse of blue. Now, it's a gaping wound, shattered glass and twisted metal spilling out onto the sidewalk below like a gruesome puzzle. The skyscraper sways gently, as if it too is feeling the effects of this sudden chaos.

My mind reels as I watch, my thoughts racing with questions. What caused this? Was it an accident or something more sinister? I try to recall any warning signs, but they're hazy at best. My colleagues were all bustling about, typing away on their computers, seemingly oblivious to the danger unfolding mere feet away.

As I stand there, transfixed by the carnage outside, my coworkers begin to murmur among themselves. Some are shouting into their phones, while others look up from their work with a mix of confusion and alarm. My supervisor, Mrs. Jenkins, rushes over to me, her expression a mask of concern.

"Emily, what's going on? What happened?" she asks, her voice firm but laced with a hint of panic.

I try to speak, but my words catch in my throat. I'm frozen in place, unable to tear my gaze away from the window. The glass is still shattering, sending shards flying out into the air like razor-sharp projectiles. My heart thuds in my chest as I feel a bead of sweat trickle down my forehead.

Mrs. Jenkins' voice pierces the silence, snapping me back to reality. "Emily, respond! What's happening?"

I take a deep breath and try again, this time managing to stammer out a few words. "It... it exploded. The window just shattered."

Mrs. Jenkins' eyes narrow, her gaze darting towards the window as if searching for answers. "Get away from the glass, Emily. It's not safe." Her voice is firm but controlled, and I feel a surge of gratitude that she's prioritizing my safety above all else.

I slowly back away from the cubicle, my eyes still fixed on the destruction outside. The skyscraper creaks and groans, the sound sending shivers down my spine. It's as if it's alive, protesting this senseless violence. I feel a growing sense of unease, a creeping feeling that something is terribly wrong.

As I move away from the window, my mind begins to wander back to the events leading up to this moment. The strange noises in the office at night, the whispered conversations between coworkers, the eerie feeling that we're all being watched... it was all starting to seem so trivial now.

But what if it wasn't just trivial? What if there's something more sinister at play here?

I shake my head, trying to clear the cobwebs. Focus on the present, Emily. The window exploded. Get away from the glass. That's what I need to do.

My gaze drifts to Mrs. Jenkins, who's now speaking into her phone, her voice rising and falling in a cadence that sounds like she's trying to convey an urgent message. Her expression is grim, but her words are reassuring – for now.

As I take another step back from the cubicle, I notice something peculiar. The air inside the office has grown thick with tension, heavy with an almost palpable sense of dread. It's as if the very atmosphere is charged with electricity, waiting to unleash its full fury upon us.

I feel a shiver run down my spine as I realize that this may be only the beginning. This explosion may be just the tip of the iceberg, and we're all standing on the precipice of something far more sinister.

The skyscraper sways again, this time in a more pronounced motion. The creaking sounds are louder now, like the building itself is warning us that it's not going to hold for much longer. I feel my heart racing in tandem with its ominous cadence.

My thoughts are a jumbled mess of fear and uncertainty as I glance around at my coworkers, who're all looking at me with a mixture of concern and curiosity. We're all waiting for something – an explanation, a rescue, or perhaps the end. The explosion has shattered our world, leaving us to pick up the pieces in a nightmare from which we may never awaken.

And yet, even as I stand there, frozen in terror, my mind is screaming at me to get away from the glass, to escape the impending doom that's slowly creeping its way into our midst. But where can I go? We're all trapped – in this office, in this skyscraper, and in a world that's rapidly descending into chaos.

The creaking grows louder still, until it sounds like the very foundations of the building are protesting its own demise. I feel my breath catch in my throat as I realize that I may not be able to escape – or even survive – this descent into madness.

The skyscraper sways once more, and I'm left with only one thought: we're all going down together.

<B>GENERATION 2:</B>

The sky scraper swayed, as I watched the window in front of me on the 21 floor explode. Shards of glass rained down like a thousand tiny knives, each one slicing through the air with a deadly precision that made my heart stumble. I was frozen in place, my eyes fixed on the carnage as if mesmerized by some sickening morbid dance.

My mind reeled as the fragments of glass hit the floor with a deafening crash, shattering into a thousand tiny pieces that seemed to stretch on forever like a macabre mosaic. The screams of the people in the adjacent offices filled my ears, a cacophony of terror that threatened to overwhelm me at any moment.

I thought back to the moment when I first stepped into this office building, full of optimism and hope for a new job as an administrative assistant. I had been so excited to start this new chapter of my life, eager to prove myself and leave my old worries behind. Now, as I watched the chaos unfold before me, all those hopes seemed like nothing more than a distant memory.

The building swayed again, its foundation shaking beneath my feet like it was trying to shake off the madness that had erupted around us. I felt my own heart racing in my chest, pounding out a frantic rhythm that threatened to consume me whole. My breath came in short gasps, as if I was suffocating under the weight of fear.

How did this happen? Why was this building shaking like a leaf? And what was happening with the people around us? Were they okay? Was anyone...?

I tried to take a step back, but my feet seemed rooted to the spot. My gaze darted from one shattered window to another, searching for some sign of what was causing this devastation. The view from our office was stunning – an unobstructed panorama of the city stretching out before us like a steel and glass canvas. Now, it was nothing but a war-torn landscape, with buildings reduced to rubble and fires blazing in the distance.

My mind began to wander to all the things I had yet to do today. The meeting with my new boss, the presentation for the Johnson account... How could this happen on the first day? Was I already being set up for failure?

A sudden thought struck me like a bolt of lightning – what if this was more than just an accident? What if someone had deliberately planned to destroy this building? And why did it feel so personal, as if something sinister was watching me from the shadows?

I felt a chill run down my spine as I realized that we were not alone in our office. There were people scattered around us, some of whom seemed to be trying to flee while others stood frozen in terror. The ones who were moving – they didn't seem to know where to go or what to do.

And then I saw it. A figure, standing at the far end of the room near the stairwell. Its eyes fixed on me with an unblinking stare that seemed to bore into my very soul. My breath caught in my throat as I tried to process what was happening. That was impossible – we were on the 21st floor; there was no way anyone could have reached us yet.

But then, it moved. The figure took a step closer, its movements eerily smooth and deliberate. I felt like I was trapped in some kind of twisted nightmare, with no escape from this descent into madness.

Time seemed to slow as the figure drew closer, its eyes burning brighter than any fire I had ever seen before. I tried to scream, but my voice was frozen in my throat. The figure loomed over me now, casting a long shadow that stretched out across the floor like a dark tentacle.

I closed my eyes, bracing for impact, as the sound of shattering glass and screams grew louder still.

---

<b>
(continue this scene:) 
The Waystone Inn lay in silence, and it was a silence of three parts.

The most obvious part was a hollow, echoing quiet, made by things that were lacking. If there had been a wind it would have sighed through the trees, set the inn’s sign creaking on its hooks, and brushed the silence down the road like trailing autumn leaves. If there had been a crowd, even a handful of men inside the inn, they would have filled the silence with conversation and laughter, the clatter and clamor one expects from a drinking house during the dark hours of night. If there had been music…but no, of course there was no music. In fact there were none of these things, and so the silence remained
</b>

<B>GENERATION 1:</B>

...and it hung over the Waystone Inn like an unbroken spell, waiting to be broken by some subtle vibration that would rattle the wooden floorboards or rustle the dry leaves in the courtyard outside.

The second part of the silence was a deeper one, born of something more profound. It was as if the very souls of those who had once frequented this inn – travelers, traders, and weary adventurers – had left behind a lingering shadow, a faint echo that still lingered in every corner, whispering secrets to the wind.

In the third part of the silence, there existed an almost palpable expectation. A sense of anticipation, as if something was waiting just beyond the threshold, watching and listening as the hours ticked by with agonizing slowness. It was a feeling that seemed to permeate every molecule in the air, a heavy, muffled hush that begged for some kind of explanation – or at least a hint – about what had brought all these silences together.

For now, however, there was nothing but silence.

<B>GENERATION 2:</B>

...an oppressive weight that hung like a physical presence in the air, making it hard to breathe. The darkness within seemed to press against the windows, as if trying to squeeze out every last shred of light and warmth from the room. The fire in the hearth had long since burned down to embers, casting only a faint glow over the empty tables and chairs. A lone figure sat at the bar, hood up, face obscured by shadows, nursing a mug of ale that was almost gone.

The innkeeper's wife, Elara, moved quietly through the rooms, checking on the guests and making sure everything was in order. She had taken to keeping late-night watch over the Waystone Inn since her husband's passing, and she knew every creak of the wooden floorboards, every groan of the old beams. But tonight felt different, even for Elara. It was as if the very fabric of the inn was holding its breath in anticipation of something...or someone.

Outside, the darkness seemed to be watching, waiting for its chance to make its presence known. The trees creaked and swayed softly in the breeze, their branches like skeletal fingers reaching out into the night. And then, just as the silence seemed to be about to become unbearable, a figure stepped out of the shadows on the road...

---

<B>
Write me a science fiction story in 1st person present tense where the main character is a 15 year girl meets The Terminator with Dr Who materializing 3/4 through the story to save her while there is a tornado of sharks baring down on them. The setting is inside the Canadian National tower restaurant on a Saturday. The length of this story is 1000 words. For each character in the story ROLE PLAY them, and have them react to the situation/setting, events and each other naturally. This includes the main characters, the background character including kitchen staff and other patrons. The sharks should also have “character” too. Treat the tower and the restaurant too as characters. Spice up the narrative to the extreme with reactions all over the setting including character actions, and dialog. The Dr Who and The Terminator should also react to the situation too and comment on it.
</b>

<B>GENERATION 1:</B>

I'll never forget this Saturday afternoon in the Canadian National Tower restaurant. I'm 15 years old, excited for a family dinner to celebrate my birthday with my parents and little brother. We're all seated by the floor-to-ceiling windows, gazing out at the stunning view of Lake Ontario.

As we peruse the menu, a sense of unease settles over me. The storm outside seems intense, with dark clouds boiling across the sky like a washing machine on spin cycle. Suddenly, a tornado warning blares through the restaurant's PA system, making everyone jump. My mom rushes to grab our tablecloth and chairs, while my dad tries to secure the windows.

That's when it starts. A swirling vortex of water appears in the window, sucking in debris and objects from the city below. I'm mesmerized as a massive shark bursts out of the water, its jaws wide open, and starts wreaking havoc on the restaurant.

"NOOOO!" my mom screams, shielding her face with her hands.

My dad tries to grab me, but I'm frozen in place, watching as another shark emerges from the chaos. It's enormous, at least 10 feet long, and its eyes are fixed on us.

Just as all hope seems lost, a familiar sound echoes through the restaurant. "Geronimo!" a British accent shouts, followed by a whirring noise.

In walks Doctor Who, his sonic screwdriver glowing brightly in his hand. He's dressed in his signature brown tweed jacket and scarf, looking every bit the part of a Time Lord on a mission.

"Ah, just in time for the shark-eat-shark buffet!" he quips, eyeing our table. "Mind if I join you? My name is... "

Before he can finish, a metallic clank interrupts the conversation. A shiny, silver creature drops from the ceiling, landing with a thud on the floor.

"Ah, good timing," it says in a deep, robotic voice. "I've been sent to assist."

The Terminator! I'm stunned. I've seen movies like this before, but never thought I'd meet one in person.

"Hasta la vista, baby!" the Terminator says, its eyes scanning the room for threats.

The Doctor and I stare at each other in awe, unsure what to say or do next. The sharks continue to wreak havoc outside, but inside, our unlikely heroes take charge.

"Alright, let's get moving!" the Doctor exclaims, grabbing my arm. "We need to find a safe place to hide!"

The Terminator nods, its gaze fixed on the sharks. "Negative, we can't outrun them. We must find a way to... terminate them."

As they strategize, I take in the surroundings, trying to make sense of this surreal situation. The Canadian National Tower restaurant is a character all its own – a bustling, high-end eatery with gleaming chrome accents and marble countertops. The decor is sleek and modern, but now it seems like a potential trap.

A harried kitchen staff member rushes past us, shouting into her phone. "We're going to have to evacuate the building! Security's trying to seal off the upper floors!"

Meanwhile, my little brother starts screaming in terror, clinging to our mom's hand for dear life.

"Don't worry, kiddo," I tell him, trying to stay calm. "We've got this."

The Doctor and Terminator confer with each other, discussing their plan of action.

"I'll create a sonic shield to protect us," the Doctor says, fiddling with his sonic screwdriver.

"Negative, we need to take out the sharks directly," the Terminator counters, its eyes fixed on the sharks outside.

As they argue, I try to grab my mom's hand again, but she's too busy trying to calm down our brother. The kitchen staff member rushes back, holding a fire extinguisher.

"We're going to have to improvise!" she exclaims, spraying the extinguisher at the sharks' entry point.

The resulting explosion sends the sharks flying backward, momentarily stunned. That's when the Doctor seizes his chance.

"Time to go time-traveling!" he shouts, grabbing my arm and pulling me toward the stairs.

We sprint up the elevator shaft as the kitchen staff member and Terminator follow close behind.

"We're not out of this yet," the Terminator growls, its eyes scanning for any more threats. "But with our combined skills, we'll survive this."

As we climb higher into the tower, the sharks regroup outside, their snarling voices echoing up through the vents. It's clear they won't give up easily.

"We need to find a secure room," I shout over the din of the tornado, my heart racing with excitement and fear.

The Doctor nods, leading us toward the top floor. We finally reach our destination – a small office space filled with computers and security systems.

"Time to reboot the system!" the Doctor says, tapping on his sonic screwdriver.

"Negative," the Terminator counters, its gaze fixed on the screens. "We need to hack into the tower's mainframe to seal off the sharks."

As we work together to outsmart the sharks and defeat the storm, I realize that this is more than just a chance encounter – it's an adventure of a lifetime.

"Hasta la vista, baby!" I shout, as we take down the last shark with a combined blast of sonic energy.

And when the dust settles, and the tornado subsides, the Doctor turns to me with a grin. "You know, kiddo, you've got potential."

I just smile, still trying to wrap my head around it all. Who knew being trapped in a Canadian National Tower restaurant with sharks outside and a Terminator and a Time Lord would be the most epic birthday party ever?

<B>GENERATION 2:</B>

I'll never forget this Saturday afternoon at the Canadian National Tower Restaurant. I was 15 and had just arrived with my parents for lunch. We were sitting by the window, enjoying our pancakes and chatting about school when things took a drastic turn.

As we finished our meal, a strange woman materialized in front of us. She was dressed in a long, brown coat and had wild, curly hair. She looked around frantically, taking in her surroundings.

"Where...where am I?" she exclaimed.

My mom stood up, startled, while my dad tried to calm her down. "You're at the Canadian National Tower Restaurant," he said. "We were just eating lunch."

The woman's eyes widened as she took in the futuristic decor of the restaurant. "This place is incredible!" she shouted. "I've never seen anything like it!"

As we watched, a Terminator appeared from nowhere. He was a towering figure with glowing red eyes and metal limbs.

"You're not going to get out of here alive," he growled, his voice low and menacing.

The woman took one look at the Terminator and screamed. My dad stood up, ready to defend us, while my mom tried to reason with her.

"Wait, wait! I think we can help you," she said. "You're not from around here, are you?"

The Terminator's eyes narrowed. "I am a cybernetic organism. I have been sent back in time to eliminate the woman."

The woman grabbed my arm and pulled me away from her. "No, no! You can't hurt me! I'm a Time Lord!"

As she spoke, Dr Who materialized behind us, his TARDIS gleaming with silver plating.

"Ah, excellent timing!" he exclaimed. "I see we have a bit of a situation here."

The Terminator turned to face him. "You're not going to interfere," he growled.

Dr Who smiled. "Oh, I'm shaking in my boots. Or rather, my sonic screwdriver is."

As they argued, the restaurant began to shake and tremble. The lights flickered and the air grew thick with an electric charge.

"What's happening?" my mom cried out.

The woman looked up at the ceiling and screamed. "It's a tornado of sharks!"

I stared in horror as the walls began to crack and splinter. Sharks, great white ones with sharp teeth, were tearing through the restaurant like they owned the place.

Dr Who jumped up, his eyes shining with excitement. "Brilliant! A tornado of sharks! Just what I needed to spice up my day."

The Terminator, however, was not amused. "I will stop this," he said, charging towards the ceiling.

As the sharks tore through the restaurant, people screamed and ran for their lives. My dad grabbed me and pulled me down onto the floor, shielding us from harm.

Meanwhile, Dr Who and the woman were working together to fend off the sharks. The Terminator was battling them with his metal fists, but even he couldn't keep up with the sheer number of predators.

The woman, however, seemed to be in her element. She whipped out a device from her pocket and began to fire energy blasts at the sharks.

"It's a sonic device!" she exclaimed. "I can disrupt their echolocation!"

Dr Who grinned. "Brilliant! You're a regular aquatic ninja."

As we watched, the sharks began to falter and fall, their ability to navigate disrupted by the woman's device.

Finally, with one last blast, the sharks were gone, vanishing into nothingness as suddenly as they had appeared.

The Terminator stood tall, his chest heaving with exertion. "That was...unexpected."

Dr Who chuckled. "All in a day's work for a Time Lord and his allies."

As we caught our breath, my parents looked at me and each other worriedly. My mom turned to the woman. "Are you okay? That was quite an ordeal."

The woman smiled, dusting off her coat. "I'm fine, thank you for asking. I think it's time for us to get back to...wherever we are."

Dr Who nodded, consulting his TARDIS console. "We're currently in Toronto, Canada. You're a long way from home, aren't you?"

The woman looked at me and smiled. "I'm on a bit of an adventure. But I think it's time for us to part ways. It was nice meeting you all."

With that, she vanished into thin air, leaving Dr Who, the Terminator, and our family staring after her in amazement.

As we stood there, trying to process what had just happened, the restaurant began to repair itself. The walls stopped cracking, and the lights flickered back on.

My dad looked at me and smiled. "Well, that was certainly a memorable lunch."

I nodded in agreement, still shaking my head in wonder. As we left the Canadian National Tower Restaurant, I couldn't help but feel grateful for our unexpected adventure with Dr Who and The Terminator.

Who knows what other adventures lay ahead? Only time would tell.

---

<B>

Using the following "story idea" below, write the first scene in the novel introducing the young woman. This scene should start in the middle of the action, include dialog, vivid passages, and end on a cliffhanger relevant to the story idea but it should also be unexpected. The scene should be 1000 words long and escalate in conflict and suspense and be written in first person, present tense with the point of view character being the young woman.

Story idea:
In a world ruled by dictatorship, a rebel young woman leads a rebellion against the system. Despite the risks, she fights to overthrow the dictator and restore democracy to her country. The government executes her for treason, but she sticks to her beliefs and is responsible for starting the revolution.

</B>

<B>GENERATION 1:</B>

I sprinted down the alleyway, my sneakers scraping against the wet pavement as I dodged debris-filled dumpsters. My heart pounded in my chest like a drumline, echoing off the cold brick walls that seemed to close in on me from all sides. I could hear the footsteps behind me, heavy and relentless, but I didn't dare look back.

"Stop!" a voice bellowed above me, shrill and commanding.

I veered sharply to the left, using my momentum to carry me around a corner and into a narrow doorway between two buildings. The voice gave chase, echoing off the walls as it pursued me through the labyrinthine streets of Kharisma's lower districts.

My breath came in ragged gasps as I pushed open the door and slammed it shut behind me, leaning against it to catch my breath. I fumbled for my phone on the chain around my neck, my fingers trembling as I punched in a code that would unlock the secure server hidden within my phone's casing.

The screen flickered to life, casting an eerie blue glow over the cramped room. My eyes scanned the familiar interface, homing in on the encrypted files that contained the plans for our next operation. The rebellion, codenamed "Phoenix," was growing by the day, with cells spreading across the country like a wildfire.

I accessed the central hub and clicked into the main screen, scrolling through the latest intel reports and updates from around the world. My eyes widened as I read the latest news – Kharisma's military had been deployed to suppress dissent in the cities, and our people were being rounded up left and right.

That's when I heard it – a faint scratching sound, like fingernails on stone, coming from the other side of the door. My heart sank as I recognized the telltale scrape of metal against concrete. Whoever was on the other side of that door had managed to bypass security.

I took a deep breath and steeled myself for what was to come. This was just another day in the life of an outlaw, but I knew better than to underestimate my enemies. My fingers flew across the keyboard as I uploaded the latest intel reports and encrypted files, readying them for upload into our secure servers.

Just as I finished, the scratching grew louder, more insistent. The door began to shake, the sound of metal grinding against concrete a dire warning that our cover was blown.

My hand trembled as I reached out to touch the doorknob, my mind racing with worst-case scenarios. "I'm not alone," I whispered into the phone's mic, using the pre-set code phrase for alerting Phoenix operatives. "I need backup, now."

The line went dead, but I knew that was just the beginning of a desperate fight for survival.

Suddenly, the door groaned, the sound of splintering wood and crunching metal filling my ears. A figure loomed in the doorway, its features obscured by shadows. My heart skipped a beat as I recognized the cold, calculating glint in their eye – it was Saelin Valtor, the infamous Head of Security for Kharisma's regime.

"Well, well, well," she drawled, her voice dripping with malice. "Look what we have here."

I didn't dare speak, frozen as I watched her hand reach out to grasp a nearby stick, its jagged end gleaming in the dim light.

"You should have stayed hidden," Saelin sneered, advancing on me like a predator stalking prey. "You should have stayed dead."

A chill ran down my spine as she raised the stick, her eyes flashing with triumph. For an instant, I thought of trying to reason with her – after all, there had to be some spark left in that cold, calculating mind of hers – but I knew better.

The only way to survive was to get out, and fast.

I took a deep breath, weighing my options as Saelin's eyes narrowed into slits. My gaze darted around the cramped space, searching for anything – anything at all – that could give me an advantage.

That's when I spotted it: a thin wire, coiled on the windowsill like a snake. It was thin enough to be used as a makeshift rope or – better yet – as a strangulation cord.

My eyes met Saelin's, and for a moment, we simply stared at each other, locked in a silent game of cat and mouse.

Then, without warning, Saelin lunged forward, swinging the stick with deadly precision. I ducked just in time, avoiding the blow by mere inches. But as I turned to flee, my foot caught on something – a loose wire, perhaps?

The world around me went dark.

And when I came to, everything was silent.

But that's not all.

<B>GENERATION 2:</B>

I sprinted down the narrow alleyway, my feet pounding the crumbling brick beneath me. The sound of footsteps echoed off the walls as I dodged a group of soldiers, their uniforms a stark white that seemed to glow in the dim light. My heart pounded in my chest like a jackhammer as I weaved between trash cans and market stalls, desperate to lose them.

"Stop her! Don't let her escape!" a voice shouted behind me.

I risked a glance over my shoulder, my eyes scanning for any sign of pursuit. A group of heavily armed soldiers gave chase, their rifles at the ready. I knew I couldn't outrun them forever – not with the streets of New Eden crawling with informants and spies.

My breath caught in my throat as I leapt over a pile of crates, using the momentum to propel myself toward the nearest door. It swung open with a jolt, revealing a narrow staircase that plunged into darkness. Without hesitation, I took the stairs two at a time, my hands grasping for handholds as I descended deeper into the bowels of the city.

A voice called out, "Wait! You'll never make it past the checkpoints!"

I didn't dare look back. My fingers scraped against rough stone, and I dropped down into the dimly lit cellar, landing hard on the dusty floor. A faint hum filled the air as a makeshift generator roared to life, casting flickering shadows across the walls.

"Kael!" a voice whispered, low and urgent.

I spun around, eyes adjusting to the darkness. A figure emerged from the shadows, its features indistinct in the dim light. "What's going on? What's happening?" I demanded, still gasping for air.

"The rebels... they've been compromised," Kael said, her voice barely audible above the generator's hum. "The government's got a mole within our ranks."

My mind reeled as I took in the words. We'd just received intel from an unknown source that indicated the government was planning to crack down on us once and for all. This revelation sent my heart racing with fear.

"Who is it?" I asked, though I already knew. The whispers of suspicion had been circulating among our ranks for days.

"It's... it's Eira," Kael whispered, her eyes darting around the cellar as if searching for an invisible enemy.

I felt a cold dread creeping up my spine. Eira – one of our most trusted members and closest friends – was now suspected of being a traitor?

"Eira would never betray us!" I exclaimed, though my voice trembled with doubt. We'd all been so convinced that she was the heart of our rebellion.

Kael shook her head, her face set in determination. "We need to know for sure. Meet me at the old clock tower at midnight. If we're going down, it'll be there."

I nodded, my mind reeling with questions and doubts. But Kael's words ignited a spark within me – a fierce determination to uncover the truth and protect our cause.

As I turned to leave, the generator's hum faltered, and the cellar plunged into darkness once more. I froze, my ears straining for any sound that might betray Eira's presence. The silence was oppressive, like a living entity watching and waiting.

Suddenly, the darkness was shattered by the sound of footsteps – heavy, deliberate steps that echoed through the empty corridors, growing louder with every passing second.

I knew then that I wasn't alone in the cellar. And whatever – or whoever – had followed me down here wouldn't be leaving without a fight.

A faint whisper seemed to caress my ear: "You shouldn't have come back."

My heart skipped a beat as I recognized the voice – and realized, with a jolt of terror, that it wasn't Eira at all.