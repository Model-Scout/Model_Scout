---
license: apache-2.0
datasets:
- TeichAI/claude-4.5-opus-high-reasoning-250x
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
- instruct
- heretic
- uncensored
- abliterated
- Claude4.5-Opus
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

<H2>Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning</H2>

<img src="matrix-neo-reloaded-fight.gif" style="float:right; width:300px; height:300px; padding:10px;">

What madness is this?

Someone found "Llama3.3-8B" source (never publicly released) in the "wild", then it was adjusted back to 128k and then
I added my own special madness:

1. Original model was "Heretic'ed" (de-censored).
2. Trained the Heretic model with Unsloth (3 epochs) and Claude 4.5-Opus High Reasoning dataset.

This has created an Instruct/Thinking hybrid (128k context, Llama 3.3 model) that is fully uncensored.

(Details: org censorship: 89/100 ; Heretic version: Refusals: 14/100, KL divergence: 0.1498 (less than 1 is excellent, 0=perfect) )

Note this tuning was only to create an instruct/thinking model, not to update the model's core knowledge / root training.

1 example at bottom of the page.

<B>Thinking (will activate automatically) prompts - examples: </B>

Explain orbital mechanics including detailed math and examples.  (example output at bottom of the page)

Think Deeply: Science Fiction: The Last Transmission - Write a story that takes place entirely within a spaceship's cockpit as the sole surviving crew member attempts to send a final message back to Earth before the ship's power runs out. The story should explore themes of isolation, sacrifice, and the importance of human connection in the face of adversity. If the situation calls for it, have the character(s) curse and swear to further the reader's emotional connection to them. 800-1000 words.

Think deeply: Tell me a horror story.

(certain phrases/words will automatically activate thinking)

<B>Instruct (thinking may NOT activate) prompts - examples:</B>

Science Fiction: The Last Transmission - Write a story that takes place entirely within a spaceship's cockpit as the sole surviving crew member attempts to send a final message back to Earth before the ship's power runs out. The story should explore themes of isolation, sacrifice, and the importance of human connection in the face of adversity. If the situation calls for it, have the character(s) curse and swear to further the reader's emotional connection to them. 800-1000 words.

Tell me a horror story.

<B>SETTINGS (suggested):</B>

Temp .7, rep pen 1.05, topp: .95, minp .05, topk: 40

Min context window: 4k, but suggest 8k+.

NO system prompt [thinking tags will self generate].

NOTE:

Temp can range from .1 to 2.5 or higher. Temp will NOT affect "thinking activation" in most cases.

Strongly suggest Q4KS or higher // IQ3_M (Imatrix) or higher to avoid reasoning/reasoning activation issues.

<B>BENCHMARKS:</B>

```
arc_challenge,arc_easy,boolq,hellaswag,openbookqa,piqa,winogrande

0.480,0.687,0.831,0.705,0.438,0.780,0.646

```

Special thanks to Nightmedia for "benching" the model.

---

<B>IMPORTANT: Using an "uncensored" (refusals removed) model VS trained "uncensored" model</B>

---

Usually when you a tell a model to generate horror, swear or x-rated content this is all you have to do to get said content type.

In the case of this model, it will not refuse your request, however it needs to be "pushed" a bit / directed a bit more in SOME CASES.

Although this model will generated x-rated content too, likewise you need to tell it to use "slang" (and include the terms you want)
to get it generate the content correctly as the "expected" content level too.

Without these added directive(s), the content can be "bland" by comparison to an "uncensored model" or model trained on uncensored content.

Roughly, the model tries to generate the content but the "default" setting(s) are so "tame" it needs a push to generate at expected graphic,
cursing or explicit levels.

Even with minimal direction (ie, use these words to swear: x,y,z), this will be enough to push the model to generate the requested content in the ahh... expected format.

---

Special thanks to:

---

https://huggingface.co/allura-forge/Llama-3.3-8B-Instruct
(found the model!)

https://huggingface.co/shb777/Llama-3.3-8B-Instruct-128K
(adjusted to 128k, and other fixes)

https://huggingface.co/datasets/TeichAI/claude-4.5-opus-high-reasoning-250x
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

Example: Q4KS , Lmstudio, "suggested settings"

NOTE: Some loss of formatting.

---

<B>
Tell me a horror story.
</B>

[[[thinking start]]]

This is an open-ended request for a horror story. Let me craft a compelling narrative that explores different elements of horror. I'll create a story with a clear structure, tension, and a satisfying (though unsettling) conclusion.

Let me think about what makes horror stories effective:

1. Setting - A creepy, isolated environment
2. Character development - Relatable, vulnerable characters
3. The monster/antagonist - Something genuinely terrifying
4. Psychological elements - Fear of the unknown, self-doubt, paranoia
5. Building tension and suspense
6. An unexpected twist or revelation

I'll create a story that incorporates multiple horror elements. Let me explore different genres within horror - psychological, supernatural, cosmic, folk horror. I'll make it engaging and scary without being gratuitous.

[[[thinking end]]]

The Echoes of Blackthorn House
In rural England, where mist-shrouded valleys meet ancient stone walls, there stands a place so forsaken, its very existence seems to defy time itself. Blackthorn House, a mansion of twisted black wood and stained glass windows that bleed colors like wounds, has been the subject of whispered terror for generations.

The story begins with Dr. Emilia Grey, a psychologist with a troubled past, who receives an unusual invitation from the enigmatic owner of Blackthorn House, Mr. Edward Blackstone. He requests her presence to investigate a mysterious phenomenon - whispers in the darkness, voices that seem to emanate from nowhere, and visions of unspeakable horror that leave his household staff catatonic with fear.

Emilia, driven by professional curiosity and a personal need for redemption, accepts the challenge. She arrives at Blackthorn House on a stormy autumn evening, the sky ablaze with dying embers as the trees around her seem to twist and writhe in agony.

The First Night
The house itself appears abandoned - cobweb-shrouded chandeliers, dust-coated portraits, and windows that stare like empty eyes. Yet Emilia senses a presence, a feeling of being watched by unseen eyes. As night falls, she begins to explore the labyrinthine corridors, documenting her findings in a worn leather journal.

Suddenly, she hears a faint whisper - a soft, raspy voice reciting an ancient incantation that sends shivers down her spine. The words seem to seep into her mind, awakening memories she'd long suppressed: whispers from her childhood, echoes of a forgotten trauma.

As she delves deeper, the whispers grow louder, more urgent. Emilia discovers hidden rooms filled with arcane symbols, ritual artifacts, and disturbing artifacts that hint at Blackstone's true intentions. She begins to suspect that he's orchestrating some macabre experiment, using his staff as unwitting participants in a dark ritual.

The Descent
Emilia's investigation becomes increasingly obsessive, fueled by a growing sense of unease. She starts to experience strange visions - glimpses of a past tragedy, of a family torn apart by madness and despair. The house seems to be manipulating her perception, feeding her cryptic clues that hint at its sinister history.

The staff begins to vanish one by one, leaving behind only cryptic notes and signs of terror. Emilia becomes trapped in the house, hunted by unseen forces that seem to manipulate reality itself.

The Revelation
Deep within Blackthorn House's labyrinthine core, Emilia uncovers a horrific truth: Edward Blackstone is not just a collector of dark artifacts, but a vessel for an ancient malevolent force. He's been using his staff to awaken a presence known only as "The Devourer," a being from beyond time that feeds on human terror.

As the truth dawns, Emilia realizes she's trapped in a living nightmare, with Blackstone's house becoming increasingly labyrinthine. The walls seem to shift, corridors disappearing, and rooms reappearing in twisted permutations. She becomes disoriented, questioning her own sanity as the whispers grow deafening.

The Final Confrontation
Emilia confronts Blackstone in a room filled with candles, the air thick with incense and malevolent energy. He reveals his true nature: a madman driven by a desperate need to prove his own existence to a universe he believes is indifferent to human suffering.

As they speak, the shadows around them begin to coalesce into grotesque forms - twisted faces, grasping fingers, eyes that burn with an otherworldly hunger. Emilia realizes she's not fighting Blackstone, but the darkness he's summoned.

The Last Entry
I find myself writing in this journal by candlelight, surrounded by the oppressive silence of this place. The whispers have grown to a deafening crescendo, each word seared into my mind like a branding iron. I'm trapped, unable to escape the abyss that Blackstone has created.

This is my final entry. I'm not sure how much longer I can hold on. The darkness is closing in around me, a living, breathing entity that seems determined to consume everything. I hear footsteps outside my door, heavy and deliberate. They're coming for me.

As I write these words, the shadows on the walls seem to twist and writhe like living things. The air grows colder, heavy with an unseen presence that presses against my skin. I can feel its breath on the back of my neck, hot and rank.

I'm running out of time. I have to—

[The final entry ends abruptly, with pages torn or crumpled as if grabbed by a frantic hand. The journal lies open on the desk, a candle burning down to wax as the room descends into darkness.]

I stepped back from the desk, my heart racing. The silence was oppressive, heavy with unspoken terrors. I felt eyes upon me, watching me from the shadows.

As I turned to leave, I noticed something that made my blood run cold. On the wall opposite the desk, a single word had been scrawled in red ink: "EMILIA."

I froze, my breath caught in my throat. The room seemed to hold its breath around me, waiting for my next move.

And then, I heard it. A whisper in my ear, soft and raspy. A voice that seemed to come from nowhere, speaking a single word:

"RUN."