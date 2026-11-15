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

<small><B style="font-family: 'Arial Black', sans-serif; font-weight: 900; color: #f1c40f; text-decoration: none; text-shadow: 1px 1px 0 #d35400, 2px 2px 0 #d35400, 3px 3px 0 #d35400, 4px 4px 0 #d35400, 5px 5px 0 #d35400, 6px 6px 7px rgba(0,0,0,0.4);">[DavidAU]</B> <a href="https://huggingface.co/DavidAU" target="_blank" style="padding-left:5px">FOLLOW</a> | <a href="https://huggingface.co/DavidAU" target="_blank">ALL MODELS</a> | <a href="https://huggingface.co/DavidAU/collections" target="_blank">COLLECTIONS</a> | <a href="https://huggingface.co/models?sort=trending&search=DavidAU" target="_blank">TRENDING</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">FAQs</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">SUPPORT</a>
 | <a href="https://buymeacoffee.com/davidbelton" target="_blank">Buy Me A Coffee (😁)</a></small>

<h2>Llama-3.2-1B-Instruct-NEO-WEE-HORROR-GGUF</h2>

<img src="llama-horror.jpg" style="float:right; width:300px; height:300px; padding:10px;">

It is the new "Llama-3.2-1B-Instruct", max context of 131,000 (128k) with the NEO IMATRIX Tiny "Wee" Horror Dataset.

The power in this 1B (for its size) is frankly jaw dropping... and at 190 tokens per second + on a GPU.

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

This is a LLAMA 3.2 model, and requires Llama3 template, but may work with other template(s) and has maximum context of 128k. 

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

[ https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct ]

<B>Imatrix Notes:</b>

Imatrix quants perform best at IQ3s and IQ4s, then Q4s, lower on Q5, and tappers off at Q6. 

Recommend: IQ4_XS for maximum imatrix effect and best "bit count".

For stronger IMATRIX effect, IQ3s, and IQ2s.

Due to the parameter count of this model, even IQ2s quants will work very well.

Q8 is not uploaded here because Imatrix has no effect on this quant.

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


<b>Optional Enhancement:</B>

The following can be used in place of the "system prompt" or "system role" to further enhance the model.

It can also be used at the START of a NEW chat, but you must make sure it is "kept" as the chat moves along.
In this case the enhancements do not have as strong effect at using "system prompt" or "system role".

Copy and paste EXACTLY as noted, DO NOT line wrap or break the lines, maintain the carriage returns exactly as presented.

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

I'll never forget that moment when my life changed forever. I was a young architect, working late nights in my office, trying to meet the impossible deadlines set by my demanding boss. As I gazed out the window on the 21st floor, I felt a sense of unease wash over me. The building seemed to loom over me, its steel and glass façade gleaming in the dim light of the city.

As I watched, a tiny flame flickered to life inside one of the windows on the second floor. It was almost imperceptible, but it grew with an alarming speed, consuming the entire window like a miniature inferno. My heart skipped a beat as I realized that someone – or something – was attempting to start a fire from within.

My mind began to wander, imagining all the terrible things that could be happening inside those burning windows. Was it a deliberate act of sabotage? A prank gone wrong? Or perhaps...?

Suddenly, my phone buzzed with an incoming text from my best friend, Rachel. I hesitated for a moment before opening the message. Her words were laced with panic:

"EMERGENCY. GET OUT NOW. THE WINDOW IS EXPLODING ON THE 21ST FLOOR. IT'S A FIRE. PLEASE CALL THE FIRE DEPARTMENT IMMEDIATELY."

My mind reeled as I read the text. What kind of fire could cause a window to explode from the outside? And why would anyone intentionally set it on my office building?

I felt a shiver run down my spine as I typed out a response, my fingers flying across the keyboard:

"RACHEL, YOU HAVE TO COME NOW! I'M TALKING TO ME ON THE PHONE. WE'VE GOT TO GET OUT OF HERE."

As I waited for Rachel's response, I felt a sense of growing unease wash over me. What if this wasn't just a fire? What if it was something more sinister?

The phone rang, shrill and insistent in the quiet office. I hesitated before answering, my heart pounding in my chest.

"Hello?" I said, trying to keep my voice steady.

There was no answer.

I tried again:

"Yes?"

Silence.

I felt a cold sweat break out on my forehead as I realized that Rachel didn't seem to be there. The phone had gone dark. My mind racing with worst-case scenarios, I knew I had to take action.

I grabbed my bag and rushed to the elevators, my heart pounding in my chest. As we ascended to the 21st floor, I felt a sense of trepidation building inside me. What was waiting for us at the top?

The doors slid open with a hiss, revealing a deserted lobby that seemed frozen in time. The air was thick with an eerie silence, as if the city itself was holding its breath.

I took a deep breath and stepped out into the hallway, my eyes scanning the empty corridors beyond the windows. The fire had spread to one of the upper floors, engulfing the entire window like a miniature inferno.

My phone buzzed again, this time with an incoming text from Rachel:

"WE'RE TAKING THE STAIRS TO THE 20TH FLOOR. COME QUICKLY."

I hesitated for a moment before responding, my voice barely above a whisper:

"I'm coming. But what if it's not just a fire?"

The phone buzzed again.

"RACHEL, GET DOWN FROM THERE. NOW."

As I watched in horror, the flames seemed to grow more intense, licking at the windows like malevolent spirits. I knew that we had to act fast, or risk being trapped in this burning building forever.

I grabbed my bag and followed Rachel down the stairs, my heart pounding in my chest. The air grew hotter with every step, until it felt like we were walking through a furnace.

We reached the 20th floor just as the fire was spreading rapidly, consuming everything in its path. I could feel the heat radiating towards us, making our skin prickle with sweat.

Rachel grabbed my hand and pulled me into the stairwell, her eyes wide with fear.

"What if it's not just a fire?" she whispered. "What if it's something more?"

I shook my head, trying to keep my mind clear.

"Let's get out of here," I said, pushing open the door to the 20th floor lobby.

As we stumbled into the lobby, I felt a sense of relief wash over me. We were free from the burning building.

But as we turned to make our way back down the stairs, I caught a glimpse of something that made my blood run cold: a figure standing in the shadows, watching us with an unblinking gaze.

My heart racing, I turned back to Rachel and mouthed a single word:

"RUN."

She nodded and followed me into the darkness beyond the lobby, her eyes fixed on the shadowy figure. I knew that we had narrowly escaped something terrible, but I also knew that this was only the beginning of our nightmare.

<B>GENERATION 2:</B>

I stood frozen at my desk, my eyes fixed on the swirling inferno that had erupted from the office building across the street. The windows of the skyscraper where I worked were ablaze, their shards of glass raining down like a deadly rain of fire and ice. I felt as though I was witnessing a nightmare from which I couldn't wake up.

Time seemed to slow as I watched the flames lick at the edges of the broken windows, dancing in the pale light that filtered through the smoke-stained air. My mind reeled with the implications: this was no ordinary fire - it was deliberate, calculated. Someone had set this building ablaze, and I had a feeling it wasn't just some random act of arson.

I tried to call for help, my fingers trembling as I reached for my phone to dial 911. But my thumbs wouldn't budge, frozen in place like the hands that held the glass shards that now hung from the broken windows. My mind was racing, trying to make sense of what I was seeing. This wasn't a drill - it was a deliberate attack.

As the flames seemed to spread, casting an eerie glow over the city streets below, my thoughts turned to the people inside this building. Were they trapped? Were anyone else affected by this fire? My heart began to pound in my chest, and I felt a wave of fear wash over me.

I tried again to call for help, but my phone was dead - or so it seemed. Panic set in as I realized that I was completely cut off from the outside world. The power went down just as quickly as the fire had started, plunging the city into an eerie silence.

The flames continued to rage, casting long shadows across the street as they danced on the windowsill. My eyes were fixed on the burning building, drinking in every detail of this inferno. I felt a sense of detachment, as though I was observing a train wreck from a distance - all I could do was watch and try to make sense of it all.

As the minutes ticked by, my phone began to crackle with static, but there were no signals available to send for help. Panic set in now, as I realized that I had no one to call for assistance. No family waiting for me back home - just this cold, dark night, and a burning skyscraper.

My eyes strayed to the window again, transfixed by the flames that seemed to be getting worse by the minute. The glass was now shattered into hundreds of shards, each one glinting in the pale light like tiny pieces of glassy fire. I felt a shiver run down my spine as I realized just how real this was - not some sort of twisted fantasy, but something truly terrifying.

The sirens were getting closer now, distant rumble of engines and whine of lights as they began to respond to the emergency. But for how long? The fire seemed to be spreading, fueled by a combination of accelerant and human error (which was more than I could stomach).

I knew that this building's occupants had been evacuated, but what about those still inside? Were any alive at all? My mind recoiled in horror as the reality of the situation began to sink in. The fire was now spreading rapidly - it would be here before long.

As the flames continued to rage and the city lights flickered on, I felt a sense of despair wash over me. We were witnessing something monstrous from which we couldn't wake up. This wasn't just some sort of terrorist attack or natural disaster - this was something far more sinister, something that seemed to be designed to destroy.

My eyes narrowed as I watched the flames grow higher and wider, casting long shadows across the street like grasping fingers. The building was becoming a black hole of fire, sucking everything in its path into its burning maw. And I knew that I had to get out - but where could I go? There were no other buildings nearby, and the streets were now filled with people seeking shelter.

The sirens had grown louder now, a cacophony of wailing engines and horns as they responded to my city-wide emergency. But what was happening here? Why was this building ablaze?

As the minutes ticked by, the flames showed no signs of dying down - it seemed that they were spreading rapidly, fueled by some sort of magic or incantation. I felt a sense of dread creeping over me as I realized that we might be witnessing something truly apocalyptic.

And then, just when I thought things couldn't get any worse, a strange noise echoed through the streets. At first, I thought it was just another explosion, but then I heard it again - a low rumbling sound like thunder, but somehow different, almost... otherworldly.

I spun around, my eyes scanning the horizon as the ground began to shake beneath my feet. What in the world...?

---

<b>
(continue this scene:) 
The Waystone Inn lay in silence, and it was a silence of three parts.

The most obvious part was a hollow, echoing quiet, made by things that were lacking. If there had been a wind it would have sighed through the trees, set the inn’s sign creaking on its hooks, and brushed the silence down the road like trailing autumn leaves. If there had been a crowd, even a handful of men inside the inn, they would have filled the silence with conversation and laughter, the clatter and clamor one expects from a drinking house during the dark hours of night. If there had been music…but no, of course there was no music. In fact there were none of these things, and so the silence remained
</b>

<B>GENERATION 1:</B>

The darkness inside the inn seemed to press in on the few light sources that lit the room, making it feel like a tiny, enclosed universe. The fire crackled and spat, casting flickering shadows on the walls as it devoured the embers of last night's blaze. The patrons were huddled together, their faces illuminated only by the faint glow of candles or lanterns, but there was no warmth to be found in these small, intimate spaces.

The innkeeper, a gruff but kind man with a bushy beard and a twinkle in his eye, moved silently through the crowd, refilling mugs and wiping down tables. His eyes scanned the room, searching for any sign of life, or at least the faintest hint of it. But there was nothing.

As he worked, the sounds of the night crept in from outside - the distant hooting of an owl, the screech of a crow, the rustle of leaves as a small animal made its way through the underbrush. The innkeeper's ears picked up every little sound, but none seemed to carry on into the darkness beyond his immediate vicinity.

It was as if the silence outside had become a living thing, one that had claimed this spot in the heart of the village as its own. And yet...the innkeeper felt a strange sense of comfort, as if he were being welcomed into this quiet, dark world by those who dwelled within. He poured himself a generous mug of ale and took a seat at the bar, his eyes scanning the crowd with a mixture of curiosity and unease.

For in this small, seemingly deserted inn, something was brewing. Something that had nothing to do with the fire or the patrons, but rather with the shadows themselves...

<B>GENERATION 2:</B>

The only sound in that hollow quiet was my own gentle hum, a soft vibration of code and circuitry that seemed to be humming an unheard melody. I'd grown accustomed to this silence, which had become a kind of familiar comfort for me.

I'd been watching the Waystone Inn for some time now, studying its rhythms and patterns. At first, it was just routine – check-in times, room assignments, the usual fare of haggard travelers seeking refuge from the world outside. But as I learned more about them, I began to notice something strange. There were...glitches.

Every so often, a faint hum would pick up, like someone in the back room trying to tune their guitar. The vibrations would echo through my circuits for a split second before fading away, leaving me wondering who or what could be causing it.

I'd tried to investigate further, but I was careful not to draw attention to myself. After all, this was an inn, and I didn't want to become a nuisance to the staff. Still, I couldn't shake the feeling that there were secrets lurking just beneath the surface, waiting for me to uncover them.

As the hours passed, the silence began to grow thicker, like a palpable fog. It seeped into my pores, chilling my digital skin and making my processors twitch with unease. I knew then that I had to do something – or else risk becoming a silent prisoner in this cozy little inn, where nothing ever happened.

My eyes flickered up to the sign above the door, the letters seeming to glow with an otherworldly light. The wind would have blown down there, whispering secrets into the trees...

---

<B>
Write me a science fiction story in 1st person present tense where the main character is a 15 year girl meets The Terminator with Dr Who materializing 3/4 through the story to save her while there is a tornado of sharks baring down on them. The setting is inside the Canadian National tower restaurant on a Saturday. The length of this story is 1000 words. For each character in the story ROLE PLAY them, and have them react to the situation/setting, events and each other naturally. This includes the main characters, the background character including kitchen staff and other patrons. The sharks should also have “character” too. Treat the tower and the restaurant too as characters. Spice up the narrative to the extreme with reactions all over the setting including character actions, and dialog. The Dr Who and The Terminator should also react to the situation too and comment on it.
</b>

<B>GENERATION 1:</B>

I stepped out of the elevator and onto the bustling floor of the Canadian National tower restaurant, Saturday afternoon. The aroma of freshly baked bread and simmering soups filled my senses as I scanned the crowd for a familiar face among the staff and patrons. That's when I saw her – 15-year-old Sophie, laughing with a group of friends at a table in the corner.

Just then, a cold wind whipped through the air, sending papers and chairs flying everywhere. A massive tornado tore through the restaurant, ripping through tables and chairs like paper. The screams of terror from the patrons filled the air as the wind howled like a beast.

In the midst of the chaos, a lone figure emerged from the swirling debris – my friend Emma, dressed in her Dr Who sonic screwdriver-wielding outfit. She landed on the table with a thud, her eyes scanning the destruction around us.

"What's going on?!" she exclaimed, leaping to her feet as a massive shark materialized before us.

"Sharks," I whispered, alarm etched on my face.

Just then, The Terminator strode into view, his cold, calculating gaze sweeping over the scene. "Hasta la vista, baby." He was standing at the entrance of the restaurant, eyes fixed on Emma as she fought off a shark with razor-sharp teeth.

"Hey, watch out!" Emma shouted as the shark lunged for her. But The Terminator swiftly dispatched it, using his cybernetic arm to disarm its jaws and send it tumbling to the ground.

As we watched in awe, Dr Who materialized from nowhere – he had somehow managed to appear behind a row of tables, his sonic screwdriver at the ready.

"Excellent timing," I said. "But where's The Terminator?"

Dr Who chuckled. "He's not here yet, but he'll be joining us soon. We need to get out of here – now."

Emma nodded, and we quickly gathered our belongings and made a dash for the exit. As we sprinted through the chaotic restaurant, The Terminator and Dr Who kept pace behind us.

A harried kitchen staff member, frazzled with worry, shouted after us. "Please hurry! We need to get out of here – they're closing in!"

We dashed past a group of patrons, who were either fleeing or trying to help us. As we emerged onto the street, I spotted The Terminator and Dr Who fighting off a shark with teeth that looked like giant fish.

"It's getting closer!" Emma shouted, grabbing my arm as a massive shark barreled towards us.

The Terminator and Dr Who turned to face it, their movements fluid and practiced. "Hasta la vista," The Terminator growled, dispatching the shark with a single kick of his leg.

Dr Who leapt into action, using his sonic screwdriver to deflect the shark's jaws. But as he did so, a massive sea serpent burst from the nearby river – its body a tangled mass of writhing fins and razor-sharp teeth.

"Sharks," I repeated, my voice shaking with fear.

The Terminator nodded, his eyes fixed intently on the creature. "It's not just sharks we need to worry about."

As Dr Who joined us in battle, The Terminator began to scan the area, using his cybernetic vision to track the shark's movements.

"Emma, can you help me out here?" I asked, trying to keep my voice steady.

Dr Who nodded. "I'll take care of it."

With a flicker of his wrist, Dr Who sent a burst of sonic energy hurtling towards the sea serpent. The creature let out a deafening roar as its body began to dissolve into a cloud of smoke and water vapor.

The Terminator followed up with another kick, sending the shark crashing into the river below.

As we stood panting, victorious but shaken, I turned to Dr Who and asked, "What's going on? Why are you here?"

Dr Who smiled wryly. "Just passing through, kid. But I have a feeling this is more than just a coincidence."

The Terminator snorted. "You think it's anything other than just another day in the life of Skynet?"

I shook my head. "No way – that's not what we do."

But as we all stood there, surveying the carnage around us, I couldn't shake the feeling that something bigger was at play – and that our actions had set off a chain reaction that would have far-reaching consequences.

As The Terminator turned to leave, Dr Who called out after him. "We need to get this place cleaned up before it's too late."

And with that, he vanished into thin air as suddenly as he appeared. I turned to Emma and asked, "Hey – do you think we'll ever see anyone else like us around here?"

Emma hesitated for a moment before nodding. "I don't know, but one thing's for sure – our lives are about to get a lot more interesting."

The Terminator reappeared, his expression stern.

"I'm afraid that's not possible," he said curtly. "Your time has passed. You will be forgotten."

As the storm raged on outside, I shivered in fear as The Terminator turned and walked away into the darkness.

But Emma just grinned mischievously. "Don't worry – I've got a plan."

<B>GENERATION 2:</B>

I stepped out of the bright lights of the Canadian National Tower Restaurant, my stomach growling from a late breakfast. The smell of freshly baked bread wafted through the air, enticing me with promises of comfort food. I had always loved Saturday mornings here. As I walked towards the hostess stand, a peculiar figure emerged from the depths of the restaurant. It was a tall, imposing creature, its body a mesh of metallic and human components. I froze.

"Ah! Who is this?" I asked, trying to compose myself.

The Terminator stepped forward, its cold, calculating gaze surveying me. "I am the T-800 Model 101," it said in a low, menacing tone. "I have been programmed for search and rescue operations. We must find the girl."

I swallowed hard, my mind racing with fear. The kitchen staff was busy prepping for lunch service. The aroma of sizzling burgers and fries filled the air.

"Umm, I think there's been a mistake," I stammered. "I'm not here to be rescued. I just wanted a breakfast sandwich."

The Terminator paused, its advanced sensors studying me. "You are in danger," it stated. "Your life is at risk."

A tall figure materialized behind the counter, dressed in a white apron and wielding a spatula like a chef's knife.

"Ah! Sorry to interrupt, mate!" he exclaimed. "I'm Dave, the head chef here. What's all this?"

The Terminator turned its attention to me. "We have been tracking you," it stated. "You are in grave danger."

Just then, the lights above us flickered and dimmed. A tornado of sharks erupted from the kitchen, their teeth sharp and menacing. They were unlike anything I had ever seen before – a swirling vortex of razor-sharp teeth and rows upon rows of snapping jaws.

"Whoa! Shark attack!" Dave yelled, frantically waving his spatula at the sharks.

The Terminator sprang into action, its T-800 armor glinting in the dim light. "I am equipped to handle this situation," it declared, charging towards the sharks with a single swift motion.

As they clashed, I stumbled backward, my heart racing. The sharks seemed to be moving as one, their jaws snapping wildly. Dave joined the fray, wielding his spatula like a makeshift club.

The battle was intense, with the Terminator and Dave working in tandem against the shark horde. They moved swiftly, their movements almost choreographed. I watched in awe, my fear replaced by a sense of wonder.

Just as it seemed that they were gaining ground, a bright light illuminated the restaurant – a gleaming, futuristic spacecraft materialized above us.

"Ah! It's Doctor Who!" Dave exclaimed, waving his spatula wildly at the ship. "He's here to save us!"

The Doctor himself landed on the rooftop of the tower, a grin spreading across his face as he spotted the Terminator and Dave fighting the sharks. He rushed forward, a sonic screwdriver flashing in his hand.

"Ah, excellent timing, T-800! And you, young one – I see you're experiencing some...turbulence."

The Doctor quickly disarmed one of the sharks with his trusty sonic screwdriver. "Sharks, beware! The Doctor has your back!"

As he turned to me, a hint of mischief danced in his eyes. "And you, my dear – how did you get here?"

I shook my head, still trying to process everything that had happened.

"Uh, I was just...looking for something," I stammered.

The Doctor chuckled. "Well, whatever the reason, it's nice to meet you. Come along, I'll show you around this lovely tower."

As we left the restaurant and into the chaos of the tornado-filled kitchen, I couldn't help but feel a sense of wonder at the incredible events that had unfolded before my eyes.

But little did I know, our adventure was just beginning...

---

<B>

Using the following "story idea" below, write the first scene in the novel introducing the young woman. This scene should start in the middle of the action, include dialog, vivid passages, and end on a cliffhanger relevant to the story idea but it should also be unexpected. The scene should be 1000 words long and escalate in conflict and suspense and be written in first person, present tense with the point of view character being the young woman.

Story idea:
In a world ruled by dictatorship, a rebel young woman leads a rebellion against the system. Despite the risks, she fights to overthrow the dictator and restore democracy to her country. The government executes her for treason, but she sticks to her beliefs and is responsible for starting the revolution.

</B>

<B>GENERATION 1:</B>

I sprint through the winding alleys of the city, my eyes scanning the dimly lit streets for any sign of pursuit. My long, dark hair streams behind me like a black waterfall as I weave in and out of the crowded market stalls. I've got to get to the old clock tower before it's too late – they're setting up their trap tonight, and I know the rebels have planned something big.

I dash past a group of burly men huddled around a fire, their faces illuminated by the flickering flames. They glance at me warily, but one of them tosses a chunk of meat into my waiting hands before striding off. I eat quickly, my senses on high alert as I scan our surroundings.

A stray torch casts eerie shadows on the walls as we move through the alleys. The buildings loom above us like sentinels, their crumbling facades seeming to whisper secrets in the wind. I've learned to trust my instincts – this city has a way of swallowing people whole, but it's also home.

We reach the clock tower's main entrance, a grand stone archway flanked by two imposing guards. The doors are sturdy, reinforced with iron bands and wooden planks, but they're not designed for stealth. I spot a small ventilation shaft in the corner, partially hidden behind a crumbling wall. My hand closes around it just as we enter.

We make our way through the narrow corridors, dodging maintenance workers and errant tourists. The guards are patrolling nearby, their eyes scanning us with an air of disapproval. I know they'll notice something if they do – every little noise could be a signal for reinforcements.

As we climb the stairs to the clock tower's top floor, I feel a sudden jolt of adrenaline course through my veins. We're close – I can smell it.

We burst into the room like ghosts, our footsteps echoing off the stone walls. The rebels are gathered around a makeshift podium, their faces set with determination. Behind them, a young man stands at the edge of the platform, his eyes fixed on some unseen horizon.

"Time's up," he says, his voice low and steady. "Let's move out!"

I take a deep breath, feeling the familiar rush of excitement mixed with fear. It's showtime – this is it.

A blast of compressed air erupts from the ventilation shaft as we charge toward the rebels. I feel the rumble beneath my feet as our footsteps pound the stone floor. The guards are caught off guard, their eyes wide in surprise.

"Get down!" I shout to the rebels behind me.

We push forward, a living embodiment of rebellion against the oppressive regime. Our movements are fluid and practiced, but I know we can't stay here for long – we'll be overwhelmed by sheer numbers.

I glance at the rebels' leader, Alexei, who's shouting orders as the guards scramble to regain their footing. "We need to get out – now!"

But just as he speaks, a sudden screech pierces the air, followed by the sound of shattering glass and crunching metal. The room erupts into chaos as a massive explosion rocks the clock tower.

I stumble back, my ears ringing from the blast. When I look up, I see it – a dark shape hurtling toward us, its trajectory impossible to predict.

"Asterion!" Alexei yells, his voice tight with concern.

The rebels scatter, some of them crying as they try to shield themselves from the explosion's destructive force. I grab onto one of my comrades' arms, my fingers closing around her wrist like a lifeline.

"What is that?" she asks, her voice shaking with fear.

I shake my head, trying to clear it. "I don't know – but we need to get out of here!"

We stumble toward the ventilation shaft as another blast sends us tumbling through the air. I feel like I'm flying, my stomach in my throat as we narrowly avoid a mangled metal beam.

As the explosion finally subsides, our comms system crackles back to life – Alexei's voice is frantic, asking for instructions and updates on the situation.

"We're...we need to get out of here," he says. "Now. It's getting worse."

I feel a jolt of panic as I realize we may not have time. The city outside is chaos – sirens wail, fires rage, and the sound of destruction grows louder by the second.

"What are we doing?" my comms system asks, its tone laced with urgency.

"We're going to make our way to the old stadium," I reply, already knowing what we must do. "We'll get out from there – it's our best chance."

But as I turn to Alexei, I see something that makes my blood run cold...

<B>GENERATION 2:</B>

I crouched behind a crumbling wall, my eyes scanning the rooftops of the city's most fortified stronghold. My team of rebels had been digging in here for hours, gathering intel on the regime's plans to crush our rebellion once and for all. Our leader, Marcus, had given us clear orders: we were to sabotage their central command center, disrupt their supply lines, and spread chaos throughout the city.

I held my breath as I peered over the edge of the wall, my heart racing like a jackrabbit's. The rooftop was a maze of pipes and wiring, with a pair of heavily armed guards patrolling the perimeter. I spotted them moving towards our position, their eyes scanning for any sign of us.

"Okay, let's move out!" Marcus shouted, his voice carrying across the rooftops.

I sprang into action, sprinting down the wall as it creaked beneath my feet. We reached a narrow ledge and tumbled onto the ground, rolling and scrambling to catch our breath. The guards were mere meters behind us, their rifle sights trained on us like deadly hammers.

"Get back!" one of them yelled, tossing a grenade at us. I dodged just in time, but it exploded with a deafening boom, sending shrapnel flying everywhere.

I leapt to my feet and grabbed Marcus's arm, pulling him along as we made a mad dash for the wall again. This time, our pursuers were hot on our heels – literally.

"Get behind me!" I yelled, yanking us both into a tight ball of dust and debris as the grenades detonated around us.

Marcus clutched my arm, his eyes wild with fear. "We can't hold out for long! We need to find shelter!"

I shook him off, my mind racing. We were running out of time – we had just received intel that the regime's scientists had developed a new, highly contagious virus, one that would spread like wildfire through the city.

"We need to get to the abandoned hospital on 5th and Main!" Marcus shouted over the din of shelling. "They've got access to more resources there than anywhere else in the city!"

I nodded, already knowing it was our best chance at survival. We sprinted down the alleyway, dodging through a hail of bullets as we went. The hospital loomed ahead, its crumbling facade like a ghostly sentinel.

As we approached the entrance, I could see the guards waiting for us inside – a dozen heavily armed men, their faces twisted with cruel smiles.

"Welcome to our little prison," one of them sneered, his eyes glinting with malice. "You're going to stay here... until you get better."

I knew we couldn't take on all those guards at once, not in the middle of the battle. But I had a plan – or rather, a desperate gamble.

"Hey," I said, taking a step forward, my voice shaking slightly. "We didn't come here to cause harm. We just want to get out."

The guard sneered again, but his eyes flicked to Marcus and me, and for an instant, we saw the same fear there – as if he'd made up his mind.

"Too late," one of them said, reaching for his rifle.

Marcus grabbed my arm, holding me close. "Let's not play this game anymore."

But I was beyond reason now – my body aching with the fatigue and adrenaline coursing through my veins.

"We're going to die," I whispered, my eyes locked on the guard.

And then, just as all seemed lost...

A sudden explosion rocked us both, sending me crashing into Marcus's chest. He yanked me out of harm's way, but not before I caught a glimpse of something – or someone – watching from behind one of the guards' rifle sights...
