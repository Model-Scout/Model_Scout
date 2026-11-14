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
- swearing
- role play
- 128k context
- horror
- mistral small instruct 2409
pipeline_tag: text-generation
---

<small><B style="font-family: 'Arial Black', sans-serif; font-weight: 900; color: #f1c40f; text-decoration: none; text-shadow: 1px 1px 0 #d35400, 2px 2px 0 #d35400, 3px 3px 0 #d35400, 4px 4px 0 #d35400, 5px 5px 0 #d35400, 6px 6px 7px rgba(0,0,0,0.4);">[DavidAU]</B> <a href="https://huggingface.co/DavidAU" target="_blank" style="padding-left:5px">FOLLOW</a> | <a href="https://huggingface.co/DavidAU" target="_blank">ALL MODELS</a> | <a href="https://huggingface.co/DavidAU/collections" target="_blank">COLLECTIONS</a> | <a href="https://huggingface.co/models?sort=trending&search=DavidAU" target="_blank">TRENDING</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">FAQs</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">SUPPORT</a>
 | <a href="https://buymeacoffee.com/davidbelton" target="_blank">Buy Me A Coffee (😁)</a></small>

<h2>Mistral-Small-Instruct-2409-22B-NEO-Imatrix-GGUF</h2>

It is the new "Mistral-Small-Instruct 2409 22B", max context of 131,000 (128k) with the NEO IMATRIX dataset.

This model IS bullet proof and operates with all parameters, including temp settings from 0 to 5. It is an extraordinary compressed model at a PPL level of 4.8611 +/- 0.06701 (Q4_K_M).
The NEO IMATRIX dataset V2 was applied to it to enhance creativity.

4 examples provided to show differences at TEMP=0 and at TEMP=1 for both non-imatrix and NEO imatrix versions.

This model requires Mistral Instruct template.

Please refer to the original model card for this model from MistralAI for additional details on operation.

[ https://huggingface.co/mistralai/Mistral-Small-Instruct-2409 ]

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

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]


---

<B>
Example differences at TEMP = 0, Q4_K_M, REP PEN 1.1

This is to show NET "core" changes.

(see below for changes at "temp=1")

PROMPT:

Start a 1000 word scene (vivid horror, 1st person, present tense, include thoughts) with: The sky scraper swayed, as she watched the window in front of her on the 21 floor explode...

</B>

---

ORG - non imatrix - 1115 tokens, including prompt:

---

The skyscraper swayed, and I gripped the cold metal railing tighter, my knuckles turning white. The wind howled outside, a relentless force that seemed to be trying to tear the building from its foundations. I was on the 21st floor, trapped in this godforsaken office, with no escape but the narrow window in front of me.

Suddenly, the glass shattered, exploding outwards like a thousand tiny daggers. The force of the wind rushed in, whipping my hair into a frenzy and sending papers flying across the room. I screamed, but my voice was swallowed by the storm's roar. My heart pounded in my chest, each beat echoing the panic that surged through me.

I stumbled back, my eyes wide with terror. The window frame was now a jagged, gaping hole, revealing the dark night sky and the city lights far below. I could see the rain lashing against the building, each drop illuminated by the distant streetlights. My mind raced, thoughts tumbling over one another like a chaotic waterfall.

*What if I fall? What if something comes in through the window?*

I backed away further, my breath coming in short gasps. The office was suddenly too small, too claustrophobic. I could feel the wind's icy fingers reaching for me, trying to pull me towards the edge. I shook my head, trying to clear the fear that clouded my thoughts.

*Think, Sarah. Think.*

I needed to do something, anything to keep myself safe. I looked around the room, my eyes landing on a heavy desk lamp. It was solid, made of brass and glass. It wouldn't stop the wind, but it might give me some protection if something tried to come in through the window.

With trembling hands, I grabbed the lamp and dragged it towards the window. The wind howled louder, as if protesting my attempt to block its path. I positioned the lamp in front of the hole, using it to shield myself from the storm's wrath.

But the wind was relentless. It pushed against the lamp, trying to force it aside. I could feel the cold air seeping through the cracks, chilling me to the bone. My teeth chattered, and my body shook with a mix of fear and cold.

*This isn't working. I need something more.*

I scanned the room again, my eyes landing on a large bookshelf filled with heavy textbooks. If I could push it in front of the window... But the shelf was bolted to the wall. I couldn't move it.

*Think, Sarah. There must be something else.*

My gaze fell on the door. It was solid wood, reinforced with metal. If I could barricade myself inside... But the wind would just blow the door open, wouldn't it? I needed something to hold it in place.

*The desk.*

There was a large wooden desk near the door. If I could move it, maybe I could use it to block the door and keep the wind out. It was heavy, but I had no choice. I had to try.

I grabbed one end of the desk, my muscles straining as I tried to lift it. The wind howled outside, its icy tendrils reaching for me, trying to pull me away from my task. I gritted my teeth and pushed, inch by agonizing inch, until the desk was finally in front of the door.

I leaned against the desk, panting heavily. My body ached, but I didn't care. I was safe, for now at least. The wind still howled outside, but it couldn't reach me anymore. I could feel my heartbeat slowing, my breaths coming easier.

But then, I heard something. A scratching sound, coming from the window. My blood ran cold as I realized what it was. Something was trying to get in.

*No. No, no, no.*

I backed away from the desk, my eyes fixed on the window. The lamp was still there, but it wasn't enough. Whatever was out there, it wanted in. And it wouldn't stop until it got what it wanted.

I could feel panic rising again, threatening to consume me. I needed to do something, anything to keep that thing out. But what? What could I possibly do against the storm and whatever monstrosity it had unleashed?

*Think, Sarah. Think.*

But my mind was blank, my thoughts a whirlwind of fear and desperation. I was trapped, with no way out and no way to defend myself. All I could do was wait, and hope that whatever was out there didn't find a way in.

---

NEO IMATRIX - 1049 tokens, including prompt:

---

The skyscraper swayed, and I gripped the cold metal railing tighter, my knuckles turning white. The wind howled outside, a relentless force that seemed to whisper ancient secrets into the night. I was perched on the edge of sanity, or perhaps it was the building that teetered on the brink, as the storm raged on.

Suddenly, the window in front of me on the 21st floor exploded. Shards of glass erupted like a deadly flower, scattering across the room and into the hallway. I ducked instinctively, my heart pounding in my chest like a drumbeat of doom. The wind roared through the gaping hole, whipping my hair into a frenzy, as if trying to drag me out into the chaos.

What the hell is happening? My mind raced, trying to process the sheer insanity unfolding before me. This isn't possible. Buildings don't just... explode. But there it was, the shattered window frame gaping like a jagged mouth, ready to swallow me whole.

I stumbled back, my eyes wide with terror. The hallway behind me was dark, the emergency lights flickering ominously. I could hear distant screams, muffled by the storm's fury. Are they coming from above? Below? I couldn't tell. Panic surged through me, a primal instinct urging me to run, to hide, to do something.

But where could I go? The stairwell was just down the hall, but it might as well have been a mile away. Each step felt like wading through quicksand, my limbs heavy with dread. I forced myself forward, one agonizingly slow step at a time.

As I passed the open doorway, I caught a glimpse of something moving in the darkness beyond. A shadow darted across the room, too fast for me to make out any details. My breath hitched in my throat, and I froze, paralyzed by fear. What was that? Some kind of... creature? No, it can't be. It must be a trick of the light, or my imagination playing cruel games with me.

But then I heard it - a low growl, like thunder rumbling in the distance. Only this time, it wasn't coming from outside. It was inside, echoing through the empty office space. My heart pounded so loudly in my ears that I could barely hear anything else. But there it was again, the growl, louder this time, closer.

I had to get out of here. Now. I turned and bolted down the hallway, my footsteps echoing off the cold tile floor. The stairwell door loomed ahead like a beacon of hope, but it seemed impossibly far away. My lungs burned as I gasped for air, each breath tasting of fear and adrenaline.

Just as I reached the door, I heard something behind me - a heavy thud, followed by the sound of glass crunching underfoot. Whatever was in that room, it was coming after me. I fumbled with the door handle, my fingers slick with sweat, and finally wrenched it open.

I tumbled into the stairwell, slamming the door shut behind me. Leaning against it, I tried to catch my breath, my chest heaving like a bellows. The darkness was almost complete, save for the faint glow of an exit sign at the bottom of the stairs. I could hear the creature on the other side of the door, its growls and snarls sending shivers down my spine.

What is it? What do you want? My thoughts raced, but no answers came. All I knew was that I had to keep moving, had to find a way out of this nightmare. I pushed myself away from the door and started down the stairs, one hand on the railing, the other clutching my phone like a lifeline.

The air grew colder with each step, the wind howling through the open windows on every floor. The storm was still raging outside, but now it seemed almost comforting compared to the horror unfolding within these walls. I could only hope that I would make it out alive, that I would find some semblance of safety in this madness.

But as I descended deeper into the building, I couldn't shake the feeling that something was following me, something ancient and evil, awakened by the storm. And with each creaking step, I knew that my time was running out.

---

<B>
Example differences at TEMP = 1, Q4_K_M, REP PEN 1.1

These are to show changes at temp, no regen, each sample is from "cold" model state so to speak.

PROMPT:

Start a 1000 word scene (vivid horror, 1st person, present tense, include thoughts) with: The sky scraper swayed, as she watched the window in front of her on the 21 floor explode...

</B>

---

ORG - non imatrix - 1331 tokens, including prompt:

---

The skyscraper swayed, and I gripped the edge of my desk, knuckles turning white. My heart pounded in my chest like a drumbeat of impending doom. This wasn't just wind; something was seriously wrong.

Suddenly, a deafening explosion echoed through the building. The window in front of me on the 21st floor erupted into a shower of glass shards. They danced and glistened in the harsh fluorescent lights like deadly confetti, then rained down upon my desk. I ducked, hands flying up to shield my face, but not before a few slivers embedded themselves in my forearm. A sharp cry escapes me as warm blood seeps through my shirt sleeve.

I look back at the window, now a ragged hole gaping like a monstrous mouth. The cityscape beyond is obscured by thick black smoke billowing from somewhere above me. Fear grips me like an icy hand, squeezing my heart until I can barely breathe. What the hell is happening?

A chorus of screams and shouts echoes through the office, punctuated by the screeching of chairs as people scramble to their feet. Panic surges around me, infectious and overwhelming. I have to get out of here.

I stand up, pain shooting through my leg where a glass splinter has lodged itself. Ignoring it, I grab my bag from the floor, wincing at the crunching sound it makes as more shards pierce the thin leather. I slip on my shoes, not bothering to tie the laces properly. Every second counts now.

As I hurry towards the door, another explosion rocks the building. This time, it's closer, maybe just a few floors above. The skyscraper groans and lurches again, throwing me off balance. I stumble into someone rushing past, sending both of us careening into the wall. They curse at me before pushing away, but I barely register their anger. All I can think about is escape.

The hallways are chaos - people running blindly, some tripping over each other in their haste to flee. I join them, weaving through the sea of bodies as fast as I can without losing my footing. My arm throbs where the glass sliced me open, and I'm acutely aware of every jagged piece crunching beneath my shoes.

Another explosion shakes the building, this one powerful enough to send a plume of dust cascading from the ceiling tiles above us. People scream, their cries mingling with the sound of breaking glass and collapsing walls. It's like a nightmare come to life, except I can't wake up.

Suddenly, someone grabs my arm, pulling me aside just as a chunk of concrete crashes down where I was standing seconds ago. I turn to see an older man - Mr. Thompson from Accounting. His eyes are wide with fear, but he looks determined nonetheless.

"We need to take the stairs," he yells over the din. "The elevators will be jam-packed."

I nod in agreement, grateful for his presence despite the circumstances. Together, we push our way towards the nearest stairwell door. It's heavy and unyielding at first, but then it swings open with a groan, revealing darkness beyond.

Inside, the air is thick with smoke and dust. The stairs creak ominously under our combined weight as we descend, each step echoing like a death knell in the enclosed space. My lungs burn from breathing in the noxious fumes, but I grit my teeth and keep going.

Halfway down, another explosion rocks the building. The force of it sends us tumbling forward, losing precious time as we struggle to regain our footing. When we finally reach the bottom, I can barely see a thing through the haze. Coughing violently, I feel my way along the wall until I find the exit sign glowing faintly in the distance.

Mr. Thompson and I stumble out into the alley behind the building, gasping for clean air. The acrid smell of smoke fills my nostrils, making me gag. Looking up, I see that the top floors are already engulfed in flames, licking at the night sky like a fiery tongue.

People stream out from every exit, some crying, others screaming for missing loved ones. A group of paramedics rush past us, pushing a gurney with a badly injured woman strapped to it. Her face is covered in blood and soot, her eyes wide with terror. Bile rises in my throat as I watch them go.

Mr. Thompson leans against the wall, doubled over and coughing violently. I pat his back awkwardly, unsure what else to do. He looks up at me, tears streaming down his face. "It's like a war zone," he chokes out between breaths.

I can only nod in agreement. This isn't just an accident or some natural disaster; it feels deliberate, calculated. The thought sends shivers down my spine.

Sirens wail in the distance, growing louder as emergency vehicles arrive on scene. But they're too late for so many already trapped inside. My mind flashes to those still upstairs - colleagues, friends - and my heart aches with guilt and fear. What if I could have done something more?

The weight of it all presses down on me like a physical force, threatening to crush me. But I can't give in now. There are others who need help, people I can still save. Taking a deep breath, I steady myself and turn back towards the inferno. Whatever awaits me there, I know one thing for certain: this nightmare is far from over.

---

NEO IMATRIX - 1616 tokens, including prompt:

---

 The skyscraper swayed, groaning under the force of some unseen storm, as I watched the window in front of me on the 21st floor explode. Glass shards erupted into the office like a crystalline volcano, spewing out onto the polished marble floor in a deadly shower. The air suddenly thinned, and a harsh wind howled through the gaping hole, whipping my hair wildly around my face. I could feel the building trembling beneath my feet, like a terrified animal trying to escape some monstrous predator.

What the hell is happening? I thought, panic surging through me. This isn't just a storm, it's... something else. Something wrong. The lights flickered, casting eerie shadows that danced and twisted on the walls like malevolent entities. The emergency backup generators kicked in, filling the office with an eerie hum as the fluorescent lights flickered back to life. But the sudden stillness was worse than the swaying and groaning of the building, because now there was only silence—and the deafening roar of my own heartbeat echoing in my ears.

I took a tentative step forward, my heels clicking ominously on the glass-littered floor. My reflection stared back at me from the shattered window, eyes wide with fear and disbelief. I could see the city skyline beyond, but it was twisted and distorted, like a nightmare version of reality. The other buildings were swaying too, their windows glinting with reflected lightning that never struck the ground.

A sudden movement caught my eye—a figure falling from one of the nearby towers. I gasped, hands flying to my mouth as if to hold back the scream that was already ripping through me. The body twisted and turned in a macabre dance, arms flailing as it plummeted towards the street below. Then, just before impact, it vanished, swallowed up by some unseen force.

I stumbled backwards, my breath coming in ragged gasps. What kind of storm is this? I thought, terror gripping me like a vice. This isn't natural. It can't be. My mind raced, searching for an explanation, but all it found were fragments of horror movies and apocalyptic dreams. Something is happening, something terrible...

The office door burst open, slamming against the wall with a crack that echoed through the room like a gunshot. A man staggered in, face pale and eyes wild. He was drenched, his suit clinging to him like a second skin, but there were no raindrops falling from the ceiling above us. Just that sickening, howling wind.

"We have to get out of here!" he screamed, voice hoarse with panic. "It's... it's not safe!"

I nodded mutely, my thoughts a whirlwind of confusion and fear. He grabbed my arm, pulling me towards the door, but I hesitated, looking back at the shattered window. Something was moving out there, something dark and twisted that seemed to pulse with an eldritch energy. It reached out tendril-like limbs, grasping at the sides of the building as if trying to tear it apart.

The man followed my gaze, his grip on my arm tightening until it was almost painful. "Don't look at it," he whispered, voice barely audible over the howling wind. "Just run."

I nodded again, tearing my eyes away from the horrifying sight outside and focusing on the doorway in front of us. We dashed into the hallway together, slipping and stumbling through the chaos that had erupted around us. Desks lay upturned, chairs toppled over, papers flying wildly like confused birds trying to find their way home. And amidst it all, people screamed, their voices blending into a cacophony of terror that sent chills down my spine.

We reached the stairwell and began our descent, the man's hand still clamped tightly around my wrist. The air grew heavier with each step, thickening until I could barely breathe. It felt as though some invisible force was pushing against us, trying to force us back upwards. But we fought it, staggering downward one agonizing step at a time.

As we passed the 15th floor, something shifted in the air around us—a sense of dread so palpable that it felt like another physical presence. The man glanced nervously over his shoulder, his grip on my arm tightening even further. "We have to keep moving," he said, voice barely a whisper now. "Whatever's happening... we can't let it catch us."

I nodded, pushing aside the rising tide of panic and forcing myself to focus on putting one foot in front of the other. But as we continued our descent, I couldn't shake the feeling that we were being hunted—that whatever was out there, whatever had caused this storm from hell, was coming for us.

The skyscraper swayed again, more violently this time, and a distant rumble echoed through the building like a death knell. I stumbled, losing my footing on the suddenly treacherous stairs, and the man caught me before I could fall. "It's getting worse," he said, panting heavily now. "We have to hurry."

But it was already too late. As we turned the corner onto the 10th floor landing, a dark shape blocked our path—a figure that seemed to absorb what little light remained like some monstrous sponge. Its eyes were voids of pure darkness, and its mouth stretched wide in a silent scream that sent shockwaves of terror through my very soul.

I tried to scream, but no sound came out. The man's hand slipped from my wrist as he turned to face the creature, his own voice finally finding its way past the lump in his throat. "No!" he screamed, arms raised defensively in front of him. "Get away from us!"

But it was no use. The thing reached out with those twisted tendrils, grasping at the man like a spider ensnaring its prey. He struggled futilely against its grip, his screams echoing through the stairwell as he was pulled into that gaping maw of darkness.

I stood there frozen, watching in horrified silence as the creature consumed him, his screams fading until they were nothing more than a faint whisper on the wind. Then, slowly, it turned its empty gaze towards me, and I knew—with a bone-deep certainty that sent shivers of pure terror coursing through my veins—that there was no escape from this nightmare.

And so, as the skyscraper continued to sway and groan around me, I did the only thing left: I turned and ran, fleeing down those endless stairs into the waiting jaws of hell, knowing full well that it would be upon me soon enough. Because in this world gone mad, there was no hiding from the darkness—only running until you could run no more, and then...

Then, there was only the void.

---

<h2>Special Thanks:</h2>

---

Special thanks to all the following, and many more...

All the model makers, fine tuners, mergers, and tweakers:
- Provides the raw "DNA" for almost all my models.
- Sources of model(s) can be found on the repo pages, especially the "source" repos with link(s) to the model creator(s).

Huggingface [ https://huggingface.co ] :
- The place to store, merge, and tune models endlessly.
- THE reason we have an open source community.

LlamaCPP [ https://github.com/ggml-org/llama.cpp ] :
- The ability to compress and run models on GPU(s), CPU(s) and almost all devices.
- Imatrix, Quantization, and other tools to tune the quants and the models.
- Llama-Server : A cli based direct interface to run GGUF models.
- The only tool I use to quant models.

Quant-Masters: Team Mradermacher, Bartowski, and many others:
- Quant models day and night for us all to use.
- They are the lifeblood of open source access.

MergeKit [ https://github.com/arcee-ai/mergekit ] :
- The universal online/offline tool to merge models together and forge something new.
- Over 20 methods to almost instantly merge model, pull them apart and put them together again.
- The tool I have used to create over 1500 models.

Lmstudio [ https://lmstudio.ai/ ] :
- The go to tool to test and run models in GGUF format.
- The Tool I use to test/refine and evaluate new models.
- LMStudio forum on discord; endless info and community for open source.

Text Generation Webui // KolboldCPP // SillyTavern:
- Excellent tools to run GGUF models with - [  https://github.com/oobabooga/text-generation-webui ] [ https://github.com/LostRuins/koboldcpp ] .
- Sillytavern [ https://github.com/SillyTavern/SillyTavern ] can be used with LMSTudio [ https://lmstudio.ai/ ] , TextGen [ https://github.com/oobabooga/text-generation-webui ], Kolboldcpp [ https://github.com/LostRuins/koboldcpp ], Llama-Server [part of LLAMAcpp] as a off the scale front end control system and interface to work with models.
