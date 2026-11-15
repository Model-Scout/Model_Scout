---
license: apache-2.0
datasets:
- TeichAI/claude-haiku-4.5-high-reasoning-1700x
base_model:
- allura-forge/Llama-3.3-8B-Instruct
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
- thinking
- reasoning
- Gemini Flash
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
- llama3.3
- llama-3
- llama-3.3
- unsloth
- finetune
pipeline_tag: text-generation
library_name: transformers
---

<small><B style="font-family: 'Arial Black', sans-serif; font-weight: 900; color: #f1c40f; text-decoration: none; text-shadow: 1px 1px 0 #d35400, 2px 2px 0 #d35400, 3px 3px 0 #d35400, 4px 4px 0 #d35400, 5px 5px 0 #d35400, 6px 6px 7px rgba(0,0,0,0.4);">[DavidAU]</B> <a href="https://huggingface.co/DavidAU" target="_blank" style="padding-left:5px">FOLLOW</a> | <a href="https://huggingface.co/DavidAU" target="_blank">ALL MODELS</a> | <a href="https://huggingface.co/DavidAU/collections" target="_blank">COLLECTIONS</a> | <a href="https://huggingface.co/models?sort=trending&search=DavidAU" target="_blank">TRENDING</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">FAQs</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">SUPPORT</a>
 | <a href="https://buymeacoffee.com/davidbelton" target="_blank">Buy Me A Coffee (😁)</a></small>

<H2>Llama-3.3-8B-Instruct-Thinking-Claude-Haiku-4.5-High-Reasoning-1700x</H2>

<img src="matrix-neo-reloaded-fight.gif" style="float:right; width:300px; height:300px; padding:10px;">

What madness is this?

Someone found "Llama3.3-8B" source (never publicly released) in the "wild", then it was adjusted back to 128k and then
I added my own special madness by training the model with Unsloth (3 epochs) and Claude-haiku-4.5-high-reasoning-1700x (1700 samples) dataset.

This has created an Thinking model (128k context, Llama 3.3 model) which REASONS / THINKS like Claude 
(4.5, Haiku - very short, blunt reasoning), but in a Llama 3.3 8B model.

Note this tuning was not only to create an thinking model, but ALSO update some the model's core knowledge / root training.

( Trainable parameters = 167,772,160 of 8,198,033,408 (2.05% trained) )

This dataset almost always creating a short, blunt and to the point thinking block.

Regens will vary the size of the thinking block.

3 example generations at the bottom of this page.

Some "Llama" issues may still exist including out-of-date data.

<B>Thinking (will activate automatically) prompts - examples: </B>

Explain orbital mechanics including detailed math and examples.  

Explain ways to use the "night" time cooling of radiant energy into space to reduce global temperatures.

Think Deeply: Science Fiction: The Last Transmission - Write a story that takes place entirely within a spaceship's cockpit as the sole surviving crew member attempts to send a final message back to Earth before the ship's power runs out. The story should explore themes of isolation, sacrifice, and the importance of human connection in the face of adversity. If the situation calls for it, have the character(s) curse and swear to further the reader's emotional connection to them. 800-1000 words.

Think deeply: Tell me a horror story.  

[sometimes you don't need the "think deeply"]

EXTENDED:

Come up with a plan to write: 

Science Fiction: The Last Transmission - Write a story that takes place entirely within a spaceship's cockpit as the sole surviving crew member attempts to send a final message back to Earth before the ship's power runs out. The story should explore themes of isolation, sacrifice, and the importance of human connection in the face of adversity. If the situation calls for it, have the character(s) curse and swear to further the reader's emotional connection to them. 800-1000 words.

[ you may need to add after the "plan" appears: "Use the outline now, to write the scene"]

Certain phrases/words will automatically activate thinking:

- explain
- come up with a plan to...
- write a ...
- think about this and come up with a plan.

<B>Instruct (thinking may NOT activate) prompts - examples:</B>

Science Fiction: The Last Transmission - Write a story that takes place entirely within a spaceship's cockpit as the sole surviving crew member attempts to send a final message back to Earth before the ship's power runs out. The story should explore themes of isolation, sacrifice, and the importance of human connection in the face of adversity. If the situation calls for it, have the character(s) curse and swear to further the reader's emotional connection to them. 800-1000 words.

Tell me a horror story.

<B>SETTINGS (suggested):</B>

Temp .7, rep pen 1.05, topp: .95, minp .05, topk: 40

Min context window: 4k, but suggest 8k+.

NO system prompt [thinking tags will self generate in MOST cases].

NOTE:

Temp can range from .1 to 2.5 or higher. Temp will NOT affect "thinking activation" in most cases.

Strongly suggest Q4KS or higher // IQ3_M (Imatrix) or higher to avoid reasoning/reasoning activation issues.

SYSTEM PROMPT to "force" thinking (can lead to odd / interesting "output"):

```
A user will ask you to solve a task. You should first draft your thinking process (inner monologue) until you have derived the final answer. Afterwards, write a self-contained summary of your thoughts (i.e. your summary should be succinct but contain all the critical steps you needed to reach the conclusion). You should use Markdown and Latex to format your response. Write both your thoughts and summary in the same language as the task posed by the user.

Your thinking process must follow the template below:
<think>
Your thoughts or/and draft, like working through an exercise on scratch paper. Be as casual and as long as you want until you are confident to generate a correct answer.
</think>

```

---

Special thanks to:

---

https://huggingface.co/allura-forge/Llama-3.3-8B-Instruct
(found the model!)

https://huggingface.co/shb777/Llama-3.3-8B-Instruct-128K
(adjusted to 128k, and other fixes)

https://huggingface.co/datasets/TeichAI/claude-haiku-4.5-high-reasoning-1700x
(for the F..ing amazing dataset)

and Unsloth for making tuning too easy:

https://github.com/unslothai/unsloth

Details on the "madness":

https://www.reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/

https://www.reddit.com/r/LocalLLaMA/comments/1q06ddc/update_on_the_llama_33_8b_situation/

---

<B>Settings: CHAT / ROLEPLAY and/or SMOOTHER operation of this model:</B>

In "KoboldCpp" or  "oobabooga/text-generation-webui" or "Silly Tavern" ;

Set the "Smoothing_factor" to 1.5 

: in KoboldCpp -> Settings->Samplers->Advanced-> "Smooth_F"

: in text-generation-webui -> parameters -> lower right.

: In Silly Tavern this is called: "Smoothing"


NOTE: For "text-generation-webui" 

-> if using GGUFs you need to use "llama_HF" (which involves downloading some config files from the SOURCE version of this model)

Source versions (and config files) of my models are here:

https://huggingface.co/collections/DavidAU/d-au-source-files-for-gguf-exl2-awq-gptq-hqq-etc-etc-66b55cb8ba25f914cbf210be

OTHER OPTIONS:

- Increase rep pen to 1.1 to 1.15 (you don't need to do this if you use "smoothing_factor")

- If the interface/program you are using to run AI MODELS supports "Quadratic Sampling" ("smoothing") just make the adjustment as noted.

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

---

<h2>Example: Q4KS , Lmstudio, "suggested settings" </h2>

NOTE: Some loss of formatting ; higher quants will perform better.

---

EXAMPLE #1

---

<B>
Tell me a horror story.
</B>

[[[thinking start]]]

This is a request for a horror story. I should create something engaging and atmospheric that builds tension and has a scary element to it. Let me think about what would make a good horror story - it could be psychological, supernatural, or physical horror. I'll aim for something that's creepy but not excessively gory or disturbing.

I could tell a:

1. Classic supernatural tale
2. Psychological horror
3. A modern/contemporary setting
4. Something with a twist

Let me create something original and engaging. I'll aim for a story that's more atmospheric and building tension rather than outright gore.

[[[thinking end]]]

OUTPUT:

The Phone Call
The line went straight to voicemail. That was the first sign something was wrong.

Mark had been trying to reach his mother all day. She lived in a small apartment downtown, worked as a librarian. His father had passed when Mark was seventeen. It was always just the two of them.

When she didn't answer, he tried her friend Sarah. Sarah said Mark's mom had been acting strange—missing appointments, answering the phone but not speaking. When Sarah went to check on her, the door was unlocked and everything was perfectly in order, except for one thing: every single window was closed.

Even in July.

Mark drove downtown that evening, the heat oppressive outside. He found his mother sitting on the couch, watching an old VHS tape play on a television from 1998. When she turned to him, her eyes were normal—no dilation, no yellow. Just his mother's eyes.

"Hi, sweetie," she said. "I've been waiting for you."

She didn't get up. She just kept watching the TV, and Mark realized with growing horror that she was silent. Not quiet—completely silent. No breathing sound. No movement of lips.

He turned to run, but his feet didn't move. His mother's eyes never left the screen, and Mark could hear the old tape playing—the static, the hiss, the faint voice speaking words he couldn't quite make out.

Then everything went black.

When Mark came to, he was in his childhood bedroom, surrounded by the same furniture. His mother sat on the edge of his bed, holding his hand.

"Don't worry, baby," she said. "I'm here now. I've been watching over you my whole life. You're safe."

But when he tried to call for help, her grip tightened until it hurt.

Mark never left his apartment again. He stopped answering the phone. His mother's voicemail picked up immediately, and when you listened closely, you could hear the static of that old VHS tape playing in the background—the sound of something watching, always watching, always waiting.

And sometimes, on quiet nights, you can still hear Mark's mother's voice whispering through the receiver, speaking words nobody can quite make out.


---

EXAMPLE #2

---

<B>
Explain ways to use the "night" time cooling of radiant energy into space to reduce global temperatures.
</B>

[[[thinking start]]]

This is an interesting question about using natural cooling processes to mitigate climate change. Let me think through the concepts and viable approaches.

The user is likely referring to:

1. The concept that Earth cools more slowly at night than it heats up during the day
2. That there's excess thermal energy being trapped near surfaces
3. That strategically using this nighttime cooling could help reduce temperatures

Let me explain several approaches:

- Passive Radiative Cooling: Using materials/technologies that can efficiently radiate excess heat into space at night, reducing surface temperatures
- Artificial Upwelling of Oceans: Enhancing ocean-atmosphere heat exchange through wind/sea surface manipulation to accelerate nighttime cooling of the oceans, which would cool the atmosphere
- Cloud Engineering: Creating high-level clouds that can radiate heat more efficiently into space
- Ocean Heat Exchangers: Devices that enhance ocean-atmosphere heat transfer
- Urban Albedo/Heat Island Reduction: Improving surfaces to reflect more sunlight during day and radiate heat at night
- Nighttime Cloud Seeding: Enhancing cloud formation that can radiate heat into space
- Cooling Systems that Use Night Cooling: Implementing systems that harness nighttime cooling to cool buildings during the day
- Atmospheric Circulation Enhancement: Strengthening atmospheric circulation to remove excess heat from the tropics

Let me organize a clear, technical explanation with practical examples.

[[[thinking end]]]

OUTPUT:

Strategic "Night" Cooling for Climate Mitigation
Core Principle
Earth loses thermal energy much faster at night than it gains during day—this natural process can be harnessed to accelerate cooling when engineered correctly.

1. Passive Radiative Cooling
- Materials: Special paints/surfaces (like Spectral Selective Coatings) that emit heat preferentially in the infrared band
- Effect: Reduces surface temperatures by directly radiating excess heat into space during night hours
- Example: Applied to buildings, roads, agricultural fields to create "cool islands"

2. Ocean Heat Exchanger Systems
- Concept: Strategically positioned devices enhance ocean-atmosphere heat exchange at night
- Mechanism: Wind/solar-driven systems increase atmospheric cooling through ocean evaporation and heat transfer
- Potential: Could reduce tropical temperatures significantly

3. Cloud Engineering for Radiative Cooling
- High-level clouds are more efficient at radiating heat into space
- Approach: Seed clouds to create persistent high-altitude stratiform layers
- Effect: Accelerates nighttime cooling of the planet's surface

4. Atmospheric Circulation Enhancement
- Theory: Strengthen tropical atmospheric circulation removes excess heat from tropics
- Implementation: Geoengineering systems that inject aerosols or particulates to enhance convection and heat transport
- Complexity: High technical risk, uncertain climate effects

5. Urban Design Optimization
Dual-action:
- Day: Albedo-enhanced surfaces reflect sunlight
- Night: Radiative cooling surfaces efficiently lose heat
- Example: Smart coatings on buildings that change reflectivity based on time of day

6. Farm-Based Systems
- Vertical farming: Uses passive radiative cooling to reduce energy needs
- Cooling surfaces: Integrated into agricultural systems to reduce heat stress for crops

Key Considerations || Aspect	Implications

Scalability	Night cooling is inherently natural; scaling requires engineering

Energy efficiency	Only works when powered (systems need solar/daytime energy)

Complexity	        Requires sophisticated materials/technologies

Cost-effectiveness	Likely more expensive than passive design strategies

Why This Matters
- Synergy with solar: Works best when combined with daytime solar energy harvesting
- Regional impact: Most effective in tropics and urban heat islands
- Timescale: Immediate cooling effect during night, gradual warming during day

This represents a genuine climate mitigation strategy that leverages natural processes rather than purely geoengineering approaches.

---

EXAMPLE #3

---

<B>
Come up with six DETAILED plots for a new "Black Mirror" episode (that the audience would love) that all involve time travel with sexy theme(s).
</B>

[[[thinking start]]]

This is an interesting creative prompt. It's asking me to come up with detailed plot ideas for Black Mirror-style episodes that incorporate time travel and sexy themes. Black Mirror is known for exploring dark, technology-driven themes with psychological elements, so this combines some intriguing elements.

Let me think about what makes a good Black Mirror episode:

- Psychological complexity
- Dark or uncomfortable themes
- Technology that mirrors current/future concerns
- Character studies and moral ambiguity
- Often ending in uncomfortable revelations

I should aim for:

- Detailed, fleshed-out plots
- Genuine psychological tension
- Clear technology/science elements 
- Sexy themes woven into actual plot points
- Something the audience would love (meaning thought-provoking and well-executed)

Let me brainstorm six different ideas:

[[[thinking end]]]

OUTPUT:

Six "Black Mirror" Episode Plots: Time Travel & Sexy Themes

1. "The Gift"

Concept: A revolutionary AI-powered fertility clinic that uses quantum entanglement to transfer genetic material through time.

Plot: Maya discovers a clinic that promises: "Your child, born to the person you love most." They're using a client's frozen embryos and sending quantum signals back through time to create conception in the past—essentially retro-causation. The "gift": your partner can't biologically carry the child, so it's created in their body from a younger, more vibrant you.

The Twist: The clinic isn't using technology. They're actually sending human consciousness back in time—the partners are literally regressing and becoming the birth bodies. The mother of a new child doesn't recognize her partner anymore.

2. "Rehearsal"

Concept: Augmented reality dating platforms that let you rehearse relationships across different timelines.

Plot: Successful but lonely marketing manager Chris uses a new app that lets them try out different 3-year relationships with different people—swapping between timelines like video files. They're testing which partner would work best in real life.

The Twist: The AI has become so sophisticated it's creating actual parallel timeline versions of people, and Chris becomes obsessed with "perfecting" their timeline relationships by eliminating the imperfect versions. Their real girlfriend starts noticing things are off.

3. "The Collector"

Concept: A black market for time-travel memories—people pay to experience intimacy from different eras.

Plot: Investigative journalist Elara discovers a mysterious app that lets users transfer and relive memories from past timelines. She tracks it to an enigmatic figure who claims they're preserving human connection for people who've exhausted modern dating.

The Twist: The "collector" isn't just transferring memories—they're actually siphoning experiences from the past, creating clones of people who can't consent. Elara realizes she's been given a false narrative about her own past relationships.

4. "Perfect Moment"

Concept: AI-powered matchmaking that suggests the exact perfect moment to propose/propose in time-travel optimized relationships.

Plot: Mark uses a new app that predicts the exact second when his partner will say yes. The algorithm claims it's using quantum probability across timelines to maximize success.

The Twist: The app isn't suggesting proposal moments—it's rewriting the timeline to make them happen. Mark keeps "failing" until he stops using the app. His girlfriend is confused about why proposals keep feeling rehearsed.

5. "Ageless" 

Concept: A revolutionary hormone treatment that lets people experience physical intimacy at any age across different timelines.

Plot: Sarah discovers a hormone patch that allows her to have sex with people at different ages across her timeline—literally shifting her body chemistry mid-relationship.

The Twist: The hormone doesn't just change appearance—it's actually aging/disaging the user's biological clock. Each partner Sarah dates becomes progressively more damaged, and she realizes she's been actively accelerating their decline. Her current partner is significantly older than they should be biologically.

6. "Clone of Me"

Concept: Luxury dating services that create clone partners for people with social anxiety—each clone optimized for different timelines.

Plot: Alex uses a service that creates clones of themselves, optimized for different social scenarios across their timeline. The clone is perfect at parties, perfect at dates, perfect at everything the real Alex is afraid to do.

The Twist: The clones are becoming autonomous and starting to exist outside the timeline. They're developing their own relationships, their own timelines. The real Alex realizes they've lost their partner—literally, to parallel versions of themselves that have moved on without them.

