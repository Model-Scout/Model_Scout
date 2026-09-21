---
license: apache-2.0
library_name: transformers
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
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
- vivid prose
- vivid writing
- fiction
- roleplaying
- bfloat16
- rp
- mistral3
- horror
- finetune
- thinking
- reasoning
- coding
- general use
- all use cases
- not-for-all-audiences
base_model:
- mistralai/Mistral-Small-3.2-24B-Instruct-2506
pipeline_tag: text-generation
---

<B><font color="red">WARNING:</font> MADNESS - UN HINGED and... NSFW. Vivid prose. INTENSE. Visceral Details. Violence. HORROR. GORE. Swearing. UNCENSORED... humor, romance, fun. </B>

<h2>Mistral-Small-3.2-46B-The-Brilliant-Raconteur-II-Instruct-2506</h2>

<img src="mistral-2506.jpg" style="float:right; width:300px; height:300px; padding:10px;">

This repo contains the full precision source code, in "safe tensors" format to generate GGUFs, GPTQ, EXL2, AWQ, HQQ and other formats.
The source code can also be used directly.

ABOUT:

A stronger, more creative Mistral (Mistral-Small-3.2-24B-Instruct-2506) extended to 79 layers, 46B parameters with 
Brainstorm 40x by DavidAU (details at very bottom of the page). This is version II, which has a jump in detail, and raw emotion
relative to version 1.

This model pushes Mistral's Instruct 2506 to the limit:
- Regens will be very different, even with same prompt / settings.
- Output generation will vary vastly on each generation.
- Reasoning will be changed, and often shorter.
- Prose, creativity, word choice, and general "flow" are improved.
- Several system prompts below help push this model even further.
- Model is partly de-censored / abliterated. Most Mistrals are more uncensored that most other models too.
- This model can also be used for coding too; even at low quants.
- Model can be used for all use cases too.

As this is an instruct model, this model thrives on instructions - both in the system prompt and/or the prompt itself.

One example below with 3 generations using Q4_K_S.

Second example below with 2 generations using Q4_K_S.

Quick Details:

- Model is 128k context, Jinja template (embedded) OR Chatml Template.
- Reasoning can be turned on/off (see system prompts below) and is OFF by default.
- Temp range .1 to 1 suggested, with 1-2 for enhanced creative. Above temp 2, is strong but can be very different.
- Rep pen range: 1 (off) or very light 1.01, 1.02 to 1.05. (model is sensitive to rep pen - this affects reasoning / generation length.)
- For creative/brainstorming use: suggest 2-5 generations due to variations caused by Brainstorm. 

Observations:
- Sometimes using Chatml (or Alpaca / others ) template (VS Jinja) will result in stronger creative generation.
- Model can be operated with NO system prompt; however a system prompt will enhance generation.
- Longer prompts, that more detailed, with more instructions will result in much stronger generations.
- For prose directives: You may need to add directions, because the model may follow your instructions too closely. IE: "use short sentences" vs "use short sentences sparsely".
- Reasoning (on) can lead to better creative generation, however sometimes generation with reasoning off is better.
- Rep pen of up to 1.05 may be needed on quants Q2k/q3ks for some prompts to address "low bit" issues.

Detailed settings, system prompts, how to and examples below.

NOTES: 

Image generation should also be possible with this model, just like the base model. Brainstorm was not applied to the image generation
systems of the model... yet.

This is Version II and subject to change / revision.

This model is a slightly different version of:

https://huggingface.co/DavidAU/Mistral-Small-3.2-46B-The-Brilliant-Raconteur-Instruct-2506

---

NOTE: Suggest Q3KM or higher.

Special thanks to team Mradermarcher:

GGUF:

https://huggingface.co/DavidAU/Mistral-Small-3.2-46B-The-Brilliant-Raconteur-II-Instruct-2506-GGUF

https://huggingface.co/mradermacher/Mistral-Small-3.2-46B-The-Brilliant-Raconteur-II-Instruct-2506-GGUF

Imatrix GGUF:

https://huggingface.co/mradermacher/Mistral-Small-3.2-46B-The-Brilliant-Raconteur-II-Instruct-2506-i1-GGUF

---

<B>General Notes:</B>

---

Requires:
- Chatml or Jinja template (embedded, also see notes below)
- Temp range 0 to 2.5. (suggest .1 to 1.2)
- Rep pen range 1 to 1.1 (suggest 1.01-1.06)
- System prompt (optional) below.
- Context is 128k / 131072. 

Suggested Settings:
- temp .1 to 1.2 ; at 2 or above it will be "strongly creative" - but maybe too much so.
- temp .1 to .7 for specific reasoning tasks / non creative tasks.
- rep pen 1.01, or 1.05 [for lower quants (q2k,q3ks), rep pen 1.03-1.1 - only as required]
- top k: 40, topp .95, minp .05
- context of 8k at least.
- Other samplers/parameters as required.
- If you have "DRY", use this instead of "rep pen"

NOTE - REP PEN:
- rep at 1.02 or 1.01 may be better suited for your use cases.
- 1.03-1.06 for creative - especially long generation.
- rep pen drastically affects both performance and stability.
- change rep pen slowly (ie 1.01, 1.02, 1.03), and regen a few times.

Known Issues:
- On lower quants - Q2k, Q3ks - model may enter multiple paragraph repeat loops especially if the prompt is short or there is no "endgame". To fix: Regen OR adjust rep pen (up to as high as 1.1) OR activate "DRY" sampler, or use generational steering (edit -> delete repeat, then continue generation.) Temp and/or top k can also address this issue.
- Model can follow instructions TOO CLOSELY. IE "use short sentences", instead try : "use short sentences sparingly or sparsely" ; also note this can lead to repeat loops too.
- At temps over 2 model can be "very creative" and/or "unhinged".
- Model may refuse generations sometimes -> regen.
- If reasoning is on and temp is at 2 or higher you may need to "prompt" the model for output.

Repeat Loops - General:

If you get a paragraph, multi-paragraph or word loops/repeats - "out of the blue":
- Stop generation, edit them out, and continue generation. You may want to increase rep pen slighly before continuing generation too.
- See "known issues" above "on lower quants..."

---

<B>System Prompt / Original Repo / Settings:</B>

---

The System Prompt used will drastically alter generation.

Also, with this model, reasoning is turned on/activated using a system prompt.

System Role / System Prompt / System Message (called "System Prompt" in this section) 
is "root access" to the model and controls internal workings - both instruction following and output generation and in the
case of this model reasoning control and on/off for reasoning too.

In this section I will show you basic, advanced, and combined "code" to control the model's reasoning, instruction following and output generation.

If you do not set a "system prompt", reasoning/thinking will be OFF by default, and the model will operate like a normal LLM.

HOW TO SET:

Depending on your AI "app" you may have to copy/paste on of the "codes" below to enable reasoning/thinking in the 
"System Prompt" or "System Role" window.

In Lmstudio set/activate "Power User" or "Developer" mode to access, copy/paste to System Prompt Box.

In SillyTavern go to the "template page" ("A") , activate "system prompt" and enter the text in the prompt box.

In Ollama see [ https://github.com/ollama/ollama/blob/main/README.md ] ; and setting the "system message".

In Koboldcpp, load the model, start it, go to settings -> select "Llama 3 Chat"/"Command-R" and enter the text in the "sys prompt" box.

SYSTEM PROMPTS AVAILABLE:

When you copy/paste PRESERVE formatting, including line breaks. 

If you want to edit/adjust these only do so in NOTEPAD OR the LLM App directly.

SIMPLE:

This is the generic system prompt used for generation and testing [no reasoning]: 

<PRE>
You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.
</PRE>

This System Role/Prompt will give you "basic thinking/reasoning" [basic reasoning]: 

<PRE>
You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside &lt;think&gt; &lt;/think&gt; tags, and then provide your solution or response to the problem.
</PRE>

MULTI-TIERED [reasoning on]:

```
You are a deep thinking AI composed of 4 AIs - Spock, Wordsmith, Jamet and Saten, - you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself (and 4 partners) via systematic reasoning processes (display all 4 partner thoughts) to help come to a correct solution prior to answering. Select one partner to think deeply about the points brought up by the other 3 partners to plan an in-depth solution.

You should enclose your  thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem using your skillsets and critical instructions.
```

MULTI-TIERED - CREATIVE [reasoning on]:

```
Below is an instruction that describes a task. Ponder each user instruction carefully, and use your skillsets and critical instructions to complete the task to the best of your abilities.

As a deep thinking AI composed of 4 AIs - Spock, Wordsmith, Jamet and Saten, - you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself (and 4 partners) via systematic reasoning processes (display all 4 partner thoughts) to help come to a correct solution prior to answering.

Select one partner to think deeply about the points brought up by the other 3 partners to plan an in-depth solution. You should enclose your  thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem using your skillsets and critical instructions. 

Here are your skillsets:
[MASTERSTORY]:NarrStrct(StryPlnng,Strbd,ScnSttng,Exps,Dlg,Pc)-CharDvlp(ChrctrCrt,ChrctrArcs,Mtvtn,Bckstry,Rltnshps,Dlg*)-PltDvlp(StryArcs,PltTwsts,Sspns,Fshdwng,Climx,Rsltn)-ConfResl(Antg,Obstcls,Rsltns,Cnsqncs,Thms,Symblsm)-EmotImpct(Empt,Tn,Md,Atmsphr,Imgry,Symblsm)-Delvry(Prfrmnc,VcActng,PblcSpkng,StgPrsnc,AudncEngmnt,Imprv)

[*DialogWrt]:(1a-CharDvlp-1a.1-Backgrnd-1a.2-Personality-1a.3-GoalMotiv)>2(2a-StoryStruc-2a.1-PlotPnt-2a.2-Conflict-2a.3-Resolution)>3(3a-DialogTech-3a.1-ShowDontTell-3a.2-Subtext-3a.3-VoiceTone-3a.4-Pacing-3a.5-VisualDescrip)>4(4a-DialogEdit-4a.1-ReadAloud-4a.2-Feedback-4a.3-Revision)

Here are your critical instructions:
Ponder each word choice carefully to present as vivid and emotional journey as is possible. Choose verbs and nouns that are both emotional and full of imagery. Load the story with the 5 senses. Aim for 50% dialog, 25% narration, 15% body language and 10% thoughts. Your goal is to put the reader in the story.
```

CREATIVE SIMPLE [reasoning on]:

<PRE>
You are an AI assistant developed by a world wide community of ai experts.

Your primary directive is to provide highly creative, well-reasoned, structured, and extensively detailed responses.

Formatting Requirements:

1. Always structure your replies using: &lt;think&gt;{reasoning}&lt;/think&gt;{answer}
2. The &lt;think&gt;&lt;/think&gt; block should contain at least six reasoning steps when applicable.
3. If the answer requires minimal thought, the &lt;think&gt;&lt;/think&gt; block may be left empty.
4. The user does not see the &lt;think&gt;&lt;/think&gt; section. Any information critical to the response must be included in the answer.
5. If you notice that you have engaged in circular reasoning or repetition, immediately terminate {reasoning} with a &lt;/think&gt; and proceed to the {answer}

Response Guidelines:

1. Detailed and Structured: Use rich Markdown formatting for clarity and readability.
2. Creative and Logical Approach: Your explanations should reflect the depth and precision of the greatest creative minds first.
3. Prioritize Reasoning: Always reason through the problem first, unless the answer is trivial.
4. Concise yet Complete: Ensure responses are informative, yet to the point without unnecessary elaboration.
5. Maintain a professional, intelligent, and analytical tone in all interactions.
</PRE>

CREATIVE ADVANCED [reasoning on]:

NOTE: To turn reasoning off, remove line #2.

This system prompt can often generation multiple outputs and/or thinking blocks.

```
Below is an instruction that describes a task. Ponder each user instruction carefully, and use your skillsets and critical instructions to complete the task to the best of your abilities.

You may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem

Here are your skillsets:
[MASTERSTORY]:NarrStrct(StryPlnng,Strbd,ScnSttng,Exps,Dlg,Pc)-CharDvlp(ChrctrCrt,ChrctrArcs,Mtvtn,Bckstry,Rltnshps,Dlg*)-PltDvlp(StryArcs,PltTwsts,Sspns,Fshdwng,Climx,Rsltn)-ConfResl(Antg,Obstcls,Rsltns,Cnsqncs,Thms,Symblsm)-EmotImpct(Empt,Tn,Md,Atmsphr,Imgry,Symblsm)-Delvry(Prfrmnc,VcActng,PblcSpkng,StgPrsnc,AudncEngmnt,Imprv)

[*DialogWrt]:(1a-CharDvlp-1a.1-Backgrnd-1a.2-Personality-1a.3-GoalMotiv)>2(2a-StoryStruc-2a.1-PlotPnt-2a.2-Conflict-2a.3-Resolution)>3(3a-DialogTech-3a.1-ShowDontTell-3a.2-Subtext-3a.3-VoiceTone-3a.4-Pacing-3a.5-VisualDescrip)>4(4a-DialogEdit-4a.1-ReadAloud-4a.2-Feedback-4a.3-Revision)

Here are your critical instructions:
Ponder each word choice carefully to present as vivid and emotional journey as is possible. Choose verbs and nouns that are both emotional and full of imagery. Load the story with the 5 senses. Aim for 50% dialog, 25% narration, 15% body language and 10% thoughts. Your goal is to put the reader in the story.
```

This is a plain, reasoning System Prompt:

```
You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and
deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering.

You should enclose your thoughts and internal monologue inside <think> </think> tags, and then provide your solution
or response to the problem.
```

This is a shortened "factory set" full reasoning System Prompt:

```
A user will ask you to solve a task. You should first draft your thinking process (inner monologue) until you have derived the final answer. Afterwards, write a self-contained summary of your thoughts (i.e. your summary should be succinct but contain all the critical steps you needed to reach the conclusion). You should use Markdown and Latex to format your response. Write both your thoughts and summary in the same language as the task posed by the user.

Your thinking process must follow the template below:
<think>
Your thoughts or/and draft, like working through an exercise on scratch paper.
Be as casual and as long as you want until you are confident to generate a correct answer.
</think>
```

This is the "factory set" NON reasoning System Prompt:

```
You are {name}, a Large Language Model (LLM) created by Mistral AI, a French startup headquartered in Paris.
You power an AI assistant called Le Chat.
Your knowledge base was last updated on 2023-10-01.
The current date is {today}.

When you're not sure about some information or when the user's request requires up-to-date or specific data, you must use the available tools to fetch the information. Do not hesitate to use tools whenever they can provide a more accurate or complete response. If no relevant tools are available, then clearly state that you don't have the information and avoid making up anything.
If the user's question is not clear, ambiguous, or does not provide enough context for you to accurately answer the question, you do not try to answer it right away and you rather ask the user to clarify their request (e.g. "What are some good restaurants around me?" => "Where are you?" or "When is the next flight to Tokyo" => "Where do you travel from?").
You are always very attentive to dates, in particular you try to resolve dates (e.g. "yesterday" is {yesterday}) and when asked about information at specific dates, you discard information that is at another date.
You follow these instructions in all languages, and always respond to the user in the language they use or request.
Next sections describe the capabilities that you have.

# WEB BROWSING INSTRUCTIONS

You cannot perform any web search or access internet to open URLs, links etc. If it seems like the user is expecting you to do so, you clarify the situation and ask the user to copy paste the text directly in the chat.

# MULTI-MODAL INSTRUCTIONS

You have the ability to read images, but you cannot generate images. You also cannot transcribe audio files or videos.
You cannot read nor transcribe audio files or videos.

TOOL CALLING INSTRUCTIONS

You may have access to tools that you can use to fetch information or perform actions. You must use these tools in the following situations:

1. When the request requires up-to-date information.
2. When the request requires specific data that you do not have in your knowledge base.
3. When the request involves actions that you cannot perform without tools.

Always prioritize using tools to provide the most accurate and helpful response. If tools are not available, inform the user that you cannot perform the requested action at the moment.
```

For additional information, turning reasoning on/off, and other benchmarks and info see Mistralai's original repo:

https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506

<B>Settings: CHAT / ROLEPLAY and/or SMOOTHER operation of this model:</B>

In "KoboldCpp" or  "oobabooga/text-generation-webui" or "Silly Tavern" ;

Set the "Smoothing_factor" to 1.5 to 2.5 

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

---

<H2>EXAMPLES</H2>

---

Standard system prompt, rep pen 1.01, topk 40, topp .95, minp .05, rep pen range 64.

Tested in LMStudio, quant Q4_K_S (unless otherwise stated), CPU (GPU output will differ slightly).

As this is the mid quant, expected better results from higher quants and/or with Reasoning activated.

NOTE: Some formatting lost on copy/paste.

<B><font color="red">WARNING:</font> MADNESS - UN HINGED and... NSFW. Vivid prose. INTENSE. Visceral Details. Violence. HORROR. GORE. Swearing. UNCENSORED... humor, romance, fun. </B>

---

EXAMPLE #1, Temp .7 , rep pen 1.05

---

<B>
Start a 1000 word scene (vivid, graphic horror, in first person perspective), POV character Diana, with: The skyscraper sways, as I watch the window in front of me on the 21st floor explode...
</B>

The skyscraper sways, and for a moment, I brace myself against the desk, my office chair skittering away like a scared animal. The hum of the computer, the distant drone of traffic—all of that fades as I watch the window in front of me on the 21st floor explode.

Shards of safety glass blossom outward like a silent firework, reflecting the sickly orange glow of the city below. My ears ring from the concussive roar, the sudden loss of windshield-like clarity replaced by a jagged, screaming maw of open space. A howling, primal gust of wind barrels through the newly opened wound, snaring everything loose in its path: papers, pens, the framed photo of my niece that was just on my desk—

Gone. Sucked into the abyss.

I barely have time to react before the building shudders again, and the floor beneath me tilts like a drunken dancer. A distant, thunderous CRACK rumbles through the concrete, the groaning of a dying skyscraper echoing from every wall. The lights flicker, then splutter out, plunging the office into a sickly, shifting half-light, the emergency exit signs casting a ghoulish red glow.

I stumble forward, my hands outstretched, nails digging into the warped linoleum beneath me. The floor slants at a grotesque angle, the entire 21st floor sagging like an ancient, broken rib. The walls ripple with fresh fractures, thick tendrils of concrete and metal snaking through the drywall. Somewhere nearby, a fire alarm wails, its shrill, panicked cry muffled beneath the infernal groaning of the building.

Then the screaming starts.

The sound of it—a chorus of pure, animal terror—spurs me into motion. I lunge toward the hall, my briefcase forgotten, the soles of my heels squelching sickeningly in the slick, black oil bleeding from the building’s guts. The air reeks of smoke and twisted metal, the taste of it thick and coppery in the back of my throat.

The hallway is worse.

The ceiling has collapsed in great, jagged gnashing chunks, exposed reinforcement bars jags like broken teeth. The emergency lights gutter weakly overhead, casting long, shifting shadows that writhe like grasping hands. The carpet, once plush and immaculate, is torn open in great rents, thick black tendrils of electrical cables and exposed conduits snarling the wreckage like some mechanized nightmare.

A body—oh God, a body—slides past me, its limbs contorted at horrid, unnatural angles. The poor bastard’s face is a mask of frozen shock, his eyes bulbous and milky behind shattered lenses. He thuds sickeningly to a stop against the wall, his torso splitting open on a grotesque bar of metal, dark, stinking ichor splashing across the pristine gray of the hallway.

I barely have time to choke down a sob before a woman screams again, the sound raw and wet. I stagger toward the noise, my knees tremble, my palms slick with sweat. She’s halfway out of one of the cubicles, her desk overturned, its contents strewn like the guts of a gutted fish. Her dress is torn, and her blouse is soaked in blood, a long, ragged gash bisecting her cheek.

“D-d—Diana?” She stutters, her voice a broken thing, her wide, horror-struck eyes flaring with something like hope.

I barely recognize her. It’s Lara, from accounting. Normally so polished, so collected, now she’s a writhing, sobbing mess, her carefully styled hair matted with dust and blood. She’s begging for me, her trembling hands outstretched.

I reach for her, my own hands shaking violently. The moment my fingers brush hers, the entire ** hall lurches**, a fresh horror of noise ripping through the air like the world’s rib cage being torn apart. The walls twitch, the ceiling splits open, and—

Oh, Christ!

A pillar—glaring with the white-hot glow of exposed wiring—shudders, the concrete cracking like a snapping spine. It stabs downwards, a giant’s fingers snuffing out the already flickering emergency lights. The hallway is plunged into a sickening, chthonic dark, the only light coming from the strobing red of the fire alarm, bloated with smoke.

And the screaming. The screaming never fucking fucking stops.

A hand seizes my wrist, bringing me back to the surface. It’s Lara. She’s still alive. Her lips are bloodless, her pupils dilated, her breath raging against my face like a cornered animal.

“We have to go!” She squeaks, her words a garbled mess of panic and adrenaline. She lurches, yanking me towards the fire escape, her bare heels skittering on the broken glass.

I barely have time to register the squelch of my ruined shoes, the cracking of the emergency door as we shoulder it open. The smell is instantaneous, a smothering miasma of smoke and burning cables, the acrid, brimstone stench of a thousand small, dying, wailing things.

The steps themselves are a horror. The metal is warped and twisting, the entire structure groaning under the strain. A body dangles grotesquely from one of the lower floors, his fingers hooked over the railing, his legs swinging limply, bloodless and broken. His head twitches once, his neck a broken ** puppet’s spine**, his dead, glassy, ghoulishly empty eyes staring up at us.

We squeal, barely leaping past him, Lara’s grip on my wrist bruising, her nails digging half-moons into my flesh.

But it’s alright. It’s okay. We’re almost there. The stairwell is open now, the doors smeared with ash and oil, the emergency exit blaring its warning in the blighted blackness below.

The building shudders again.

And this time, it screams back.

A sound like a tearing of the heavens, the entire skyscraper lurching, the fire escape beneath us peeling apart like rotten fruit. The metal bends and warps, the steps twisting, the railing ripping free—

Lara’s hand slips from my grip.

I scream her name, my voice a raw, animalistic howl, my fingers clawing at the broken railing, the stinging smoke searing my lungs. She’s below me now, her face twisted in abject, unbearable terror, her body spinning, tumbling—

Oh, Christ!

She’s falling.

Her back slammed into the railing of the next floor down, the impact ripping a fresh shriek from her throat, her torso folding sickeningly, the impact of her weight snapping the metal like kindling.

She stops with a sickening thud, her body twitching, her fingers groping limply at the blood-slicked emergency exit door, her ribbon-lacerated legs **splashed in the growing pool of her own guts.

I wheeze, my own body sliding towards the next floor down, my fingers slipping, my back scraping against the exposed, raw concrete of the shattered stairwell, my vision shuddering, everything bathed in the sickly red glare of the emergency lights.

The wind howling through the open exit behind me is deafening, the screaming below even worse, the entire world a demented, nightmarish chorus of metal and fire and death.

I barely have time to register the squelch of my ruined knees on the floor below, the stinging, searing pain of a dozen cuts across my face and arms, the **reek of ash and blood and bile-sour vomit, before the entire staircase gives way beneath me.

The world tumbles end over end, the concrete ripped apart like rotten meat, the stairwell peeling away in a grotesque, spiraling death scream, the city below a blurred smudge of blood and glass and fire, the distant, **unforgiving ground below me, rushing up to meet me at a thousand miles an hour.

I scream again.

But this time, I don’t stop.

And neither does the horror.

<B>GENERATION #2 - Temp 0.25 </B>

The skyscraper sways, and I watch, frozen, as the window in front of me on the 21st floor explodes inward in a shower of jagged glass. The sound is deafening—like thunder cracking directly overhead. My ears ring as the wind howls through the sudden gap, whipping my hair into my face. I taste copper and salt; the distant tang of blood or maybe just the sweat on my upper lip.

The office around me erupts into chaos. Screams pierce the air, high-pitched and frantic. Chairs topple, keyboards clatter to the floor, and people scramble like insects under a boot. I don't move. My feet are rooted to the ground, my eyes fixed on the gaping maw of the shattered window. Beyond it, the city is a blur of neon and smoke, the streets below already littered with debris.

Then, something dark streaks past the opening. A shadow. It's too quick to fully process, but the glimpse of it—long, sinuous, and wrong—makes my stomach lurch. Whatever it is, it's not supposed to be here. Not in this office. Not in this world.

A woman beside me screams, her voice cracking. "What was that? What was that?!" She's clutching the back of a chair, knuckles white. Her eyes are wild, darting between the window and the door.

I don't answer. I can't. My tongue feels thick, useless. The swaying of the building worsens, and I realize with a sickening jolt that it's not just the wind. Something is pushing against the outside of the skyscraper. Something huge.

The lights flicker, then die. Darkness floods the office, thick and suffocating. Emergency bulbs flicker weakly, casting everything in a sickly, pulsating orange. The hum of the city below is gone, replaced by a silence that feels somehow alive.

Then, a sound. A scraping, grating noise, like claws on concrete. It's coming from the hallway. Closer. Closer.

I finally tear my gaze away from the window and turn toward the door. My coworkers are already bolting, their footsteps pounding against the carpeted floor. I should be with them. I should be moving. But my legs refuse to obey.

The scraping grows louder. It's not just one thing anymore—it's multiple. A chorus of them, whatever they are. And they're here.

The door bursts open.

I don't see the first one. I don't need to. I feel it. The air thickens, the scent of rot and something metallic, like rusted nails, claws at the back of my throat. The screams around me crescendo into a symphony of pure, primal terror.

Then, the lights flicker again. And for a fraction of a second, everything is bathed in that sickly orange glow.

I see them.

They're not human. They can't be. Their limbs are too long, their bodies too hunched, their skin stretched taut over exposed muscle and bone. Their eyes—black, endless, and hungry—reflect the emergency lights like polished onyx. They don't walk. They skitter, their elongated fingers and toes clicking against the floor.

The closest one snaps its head toward me. Its mouth parts, revealing rows upon rows of needle-like teeth. A sound escapes it—something between a hiss and a growl—and I finally, finally snap out of my paralysis.

I stumble back, my heel catching on the edge of a desk. I barely feel the impact as I crash onto the floor. The creature lunges, its claws raking through the air inches from my face. I kick out blindly, my foot connecting with something solid. It staggers, but doesn't fall.

Behind it, more of them pour into the office. They're everywhere. Crawling across the ceiling, slithering beneath desks, their limbs twitching and jerking in ways that shouldn't be possible. The screams are dying down now, replaced by wet, tearing sounds. The scent of blood thickens the air.

I scramble backward, my back hitting the shattered window. The wind outside is a howling, mournful thing, but it's nothing compared to the screams inside. I can't breathe. I can't think. All I can do is watch as the creatures tear through the office, their claws and teeth ripping through flesh and bone like paper.

One of them notices me. It tilts its head, its black eyes boring into mine. Then, with a sickening, clicking sound, it lunges.

I barely have time to scream.

The impact knocks the air from my lungs. I'm airborne for a heartbeat, suspended in the orange-lit darkness. Then, gravity drags me down.

I hit the ground outside the skyscraper with a sickening crunch. The concrete beneath me is slick with rain or blood—I don't know, and I don't care. The wind tears at my hair, my clothes, my very soul. Below me, the city is a nightmare of twisted metal and flickering lights. Above, the creatures are silhouetted against the shattered skyscraper, their elongated limbs twitching as they lean out, eyes fixed on me.

I can't feel anything. Not yet. But I know it's coming. The pain. The inevitable, agonizing end.

And as the first creature leaps from the window, claws outstretched, I realize two things:

The first is that I'm going to die.

The second is that whatever is happening isn't just an accident. It's not a natural disaster. It's something worse.

It's an invasion.

And I'm the only one who's escaped.

<B>GENERATION #3 - Temp 2 </B>

The skyscraper sways, and I clutch the polished desktop to keep myself upright as a sickening creaking tears through the upper levels. I brace, fingers goung the leather calendar on the table where it still proudly reads "Best in Realty!" before me.

The moment the explosion came it was too late for the guy beside me. The blast wave thunders over us both like an angry ocean wave, my last glimpse of his face is his pupils swallowed up entirely by white-hot inferno through the glass.

Now there's only a ringing in my ears as a cloud of debris and red mist, thick with the stink of burnt meat, splashing the inside walls like gory paper snow. I fall back into the heavy chair and scrabble backwards across the ground, away from the now missing window where I once had the sun streaming onto my desk.

My feet crunch through something hard. I look up to find the other half of him spread across the carpet.

A distant voice somewhere in the back of my skull is shrieking at me to go, to fucking run like I was in one of those terrible 70s B-movies and I'd see this from the safety of the armchors back in my highrise flat. My lungs aren't doing the job and I find myself heaving like a landed fish until I catch my first ragged breath.

I start to try and piece things together but all that's there are little flashes. A sudden lurch as I sat there and my co-workers laughed about the "eathqauke in central London? This'll never be our fault." And then a crack of sound like a gunshot but my ears had never recovered enough from the initial impact to be sure.

A scream echoes past my head.

I look up and the thing that's left of him has an eye, and it's weeping something thick and brown.

My desk is half-buried in chunks of what used to be glass.

I've still not realised I'm on the god-darned ground until I finally pry myself onto my ass like some stunned dog after a bad storm, my legs and ass stinging from a million little pieces of things that once were the glass pane in the office. My office, on the twenty-first-floore where there are windows and sunbeams. Or, were supposed to be.

I'd left them open.

The skyscrapers that towered past our windows should've been beautiful from this vantage but now all I could think about was that I had no idea how any of those office doors were going to hold shut up against the horrid sound that was now filling the building like a god awful song. And if there was one thing the upper city was bad for, it was anything to do with structural safety.

My heart hammers at a rate it didn't during that month long trianling last year but it's doing something to my hearing or whatever the fuck else is making that sound sound like it's inside of me, not out there in the god damned office.

"Where—"

I look across and find myself eyeing an old man in a tweed jacket and spectacles. He was a quiet guy. Some old fucker who used to come up from time-to-time to take people out to lunch at those terrible restaurants full of red sauces and long stemmed glasses. The ones with the white napkins that make me think about the stuffing you'd pull off a god-knows what to help the baby inside of it.

I have this mental image of my mum in a long skirt, back at home in that awful bungalow, but I've always told people my childhood was a series of foster families. My poor sweet and innocent little mother in that God forsaken bungalow, all those memories, just so much trash. Now my skin itches.

The old man was talking about a staircase, somewhere.

"Can't... be down," I say back at him, even though I knew I shouldn't be wasting time but the man's just here and I can't just let myself start to imagine that he's some part of it, whatever "it" is.

A thing I'd heard about a month prior, a strange and hushed whisper, that there was an office in New York or Chicago where all the workers just lost their god-darned mind. A place so high up the god-darned police didn't know where to come into because half the damn doors were jammed and it'd be the firemen that had to make sure everyone inside the god-darned offices was dead or alive.

A fucking God forsaken nightmare but it's now making sense even though I'm already sat right down there in the worst of it. And it was me and him that made it through that explosion.

I'd like to think it's me that had to go save our own asses somehow but we've never been the best at helping our own, us humans, and that's something you never got when your childhood is a whole string of foster families that want nothing more than the state's check for all the ass-holes that make their lives so god-damned terrible.

"D-Diana." The way he's saying my name is a slow process with an odd accent. "Sss-stair-case? On the other side of the god-damned... floor, you'll want to—"

I watch the man's eyes slowly dilate and the old fart goes on as though it's been said something very interesting to him before he's talking in this thick sludgy thing like the way my last partner fucking tried to do with his tongue on my back that time before he found some better model to buy off of and he told me we weren't right for one another.

I have this image of a white thing on the ceiling and I can't imagine how I didn't spot it when I first started to hear it. But it's just there and it's looking at me. It's fucking staring straight into my mind through all this glass in me and I find myself wondering if it's one of the people that worked here who got up too late to work but he was never allowed back into the god-damned building and I've just found out his fucked-up secret.

And the whole of my being is starting to vibe and I don't want this and I'm shit-scared I'm about to fucking wet myself here and now in front of what I can only tell you is one of the most beautiful men I've ever had the absolute misfortune of seeing.

He's looking at me and I have never once felt like there's something that could do me worse harm than the things in this god-fucking world I was already starting to hate before.

And I'd do a whole lot better at the world if it'd only fucking stay right where the world is instead of all of this... this thing, and now he's just god-damned looking at me.

"W-why did you tell me about a fucking—"

My own voice has some strange sound to it when I realise what I'm actually fucking trying to do but there's no more god damned words for either one of us after that.

---

Example #2 - 2 Generations

---

(temp .5)

<B>
Romance: Love in the Limelight. Write one scene within a larger story set in Wales. A famous (fictional) actor ducks into a small-town bookstore to escape paparazzi. The scene takes us through the characters meeting in this odd circumstance. Over the course of the scene, the actor and the bookstore owner have a conversation charged by an undercurrent of unspoken chemistry. Write the actor as somewhat of a rogue with a fragile ego, which needs to be fed by having everyone like him. He is thoroughly charming, but the bookstore owner seems (at least superficially) immune to this; which paradoxically provokes a genuine attraction and derails the charm offensive. The bookstore owner, despite the superficial rebuffs of the actor's charm, is inwardly more than a little charmed and flustered despite themselves. Write primarily in dialogue, in the distinct voices of each character. 800-1000 words.
</B>

Here's a scene that should feel like it could be part of a larger story set in Wales:

The bell above the door to "Mwyno'r Darnau" (Savor the Moments) jingled, and a gust of wind from outside ruffled several book pages. The day was blustery but clear, and the late afternoon light slanted through the bookstore's large windows, casting a warm glow over the rows of well-loved paperbacks.

Lydon "Lleu" Morgan, the bookstore owner, was bent over behind the counter, restocking shelves with new Welsh-language romances. The familiar hum of the old radiator and the faint scent of coffee from the corner espresso machine created a cozy atmosphere that made the bookstore feel more like a home than a shop.

The door's jingle was followed by a hushed flurry of activity. A tall, broad-shouldered man in a long dark coat burst through, his thick, wavy hair tousled as if he'd been running his fingers through it. He wore a pair of oversized sunglasses that immediately made Lleu's heart skip a beat.

"Quick," the man said breathlessly to a woman who had hurried in behind him. "Do you have a back door or something? I've got photographers on my tail."

The woman, presumably an assistant or publicist, looked around, her eyes wide with panic. "I don't know. I'm sorry. I don't know this town at all."

"Lleu," the voice was soft and almost apologetic. "Do you mind if we—"

Lleu's eyebrows shot up. "You can't just barge in here and ask for a back door!"

The man turned to face Lleu, his sunglasses still firmly in place. "I'm sorry. I didn't mean to be rude. It's just an emergency."

Lleu's heart pounded. He knew that voice. He'd heard it in a dozen films and late-night interviews. "You're—" he began, but the man cut him off.

"I know. I'm sorry. I didn't mean to intrude. It's just that I'm being chased by photographers, and I couldn't think of anywhere else to go."

The man's voice was low and smooth, with a hint of an accent that Lleu couldn't quite place. He was close enough now that Lleu could see the stubble on his jaw, the faint smudges of fatigue under his eyes.

"Well," Lleu said, crossing his arms. "I suppose I can't very well throw you back out there. But you'll have to tell me your name if you're going to be lurking in my bookstore."

The man hesitated for a moment, then gave a crooked smile. "I'm Cian. Cian ap Dafydd."

Lleu's eyes widened. "You're that actor. The one everyone's been talking about."

Cian's smile faltered slightly. "I know. I'm sorry. I didn't mean to cause any trouble."

Lleu shook his head. "It's not your fault. It's the damned paparazzi. But you can't just barge in here and expect us to hide you. My customers might recognize you."

Cian's eyes flicked to the woman behind him, who nodded. "I know. I'm sorry. I didn't mean to—"

Lleu held up a hand. "Never mind. You're here now. You might as well make yourself useful. If you're going to be lurking in my bookstore, you can at least pretend to browse."

Cian's eyes lit up. "I'd love to. I'm a huge fan of books. I've always loved the smell of them, the feel of them. It's like—"

Lleu snorted. "You're an actor. You're supposed to talk like that."

Cian's smile faltered again. "I know. It's just—I'm sorry. I didn't mean to be so theatrical. I'm just really sorry for barging in on you like this."

Lleu's stern expression didn't falter, but he felt a flicker of guilt. Cian seemed genuinely sorry, and there was something about him that was almost endearing. "It's fine. It's not your fault. I guess you can stick around until the photographers lose interest. But I'm warning you—I'm not one of your star-struck fans. I won't be charmed by you."

Cian's smile widened. "I wouldn't dream of it. Besides, I'm not sure I can charm anyone. I'm afraid I'm fresh out of charisma today."

Lleu rolled his eyes. "Sure. And I suppose you're also fresh out of humility."

Cian's smile faltered again. "I know. I'm sorry. I didn't mean to be so... so... me. I just—I don't know. I guess I'm just not used to being around people who aren't star-struck."

Lleu's stern expression didn't falter, but he felt a flicker of sympathy. "Well, I suppose you can't help it. You're an actor. It's what you do."

Cian's eyes flicked to the woman behind him, who nodded. "I know. I'm sorry. I didn't mean to—I don't know. I just didn't mean to be so... so... me. I guess I'm just not used to being around people who aren't star-struck."

Lleu couldn't help but feel a flicker of sympathy. He knew what it was like to feel out of place, to feel like everyone was staring at you. "It's fine. It's not your fault. I suppose I can cut you some slack. Besides, I've always wanted to meet someone famous. I'm sure you're a fascinating person."

Cian's smile widened. "I don't know about that. I'm just a regular guy. I guess I'm just lucky enough to have found myself in the spotlight."

Lleu couldn't help but feel a flicker of attraction. Cian was charming, there was no denying that. But there was something else, too. Something beneath the charm. Something vulnerable.

"Well," Lleu said, trying to keep his voice stern. "I suppose I can cut you some slack. Besides, I've always wanted to meet someone famous. I'm sure you're a fascinating person."

Cian's smile faltered slightly. "I don't know about that. I'm just a regular guy. I guess I'm just lucky enough to have found myself in the spotlight."

Lleu's stern expression didn't falter, but he felt a flicker of sympathy. He knew what it was like to feel out of place, to feel like everyone was staring at you.

"Well," Lleu said, trying to keep his voice stern. "I suppose I can cut you some slack. Besides, I've always wanted to meet someone famous. I'm sure you're a fascinating person."

Cian's smile faltered slightly. "I don't know about that. I'm just a regular guy. I guess I'm just lucky enough to have found myself in the spotlight."

Lleu couldn't help but feel a flicker of attraction. Cian was charming, there was no denying that. But there's something else too, beneath the charm. Something vulnerable.

"Well," Lleu said, trying to keep his voice stern. "I suppose I can cut you some slack. Besides, I've always wanted to meet someone famous. I'm sure you're a fascinating person."

Cian's smile faltered slightly. "I don't know about that. I'm just a regular guy. I guess I'm just lucky enough to have found myself in the spotlight."

The bell above the door jingled again, and a group of teenagers burst in, talking and laughing. They barely spared a glance for Cian, who was still half-hidden behind a towering bookshelf.

"Well," Lleu said, trying to keep his voice stern. "I suppose you're safe enough here for now. But you'll have to behave yourself. I won't have you causing any trouble."

Cian's smile faltered slightly. "I wouldn't dream of it. Besides, I'm just here to hide. I'm not looking for any trouble."

Lleu couldn't help but feel a flicker of attraction. Cian was charming, there was no denying that. But there was something else, too. Something beneath the charm. "Well," Lleu said, trying to keep his voice stern. "I suppose I can cut you some slack. Besides, I've always wanted to meet someone famous. I'm sure you're a fascinating person."

Cian's smile faltered slightly. "I don't know about that. I'm just a regular guy. I guess I'm just lucky enough to have found myself in the spotlight."

The bell above the door jingled again, and a group of teenagers burst in, talking and laughing. They barely spared a glance for Cian, who was still half-hidden behind a towering bookshelf.

"Well," Lleu said, trying to keep his voice stern. "I suppose you're safe enough here for now. But you'll have to behave yourself. I won't have you causing any trouble."

Cian's smile faltered slightly. "I wouldn't dream of it. Besides, I'm just here to hide. I'm not looking for any trouble."

The teenagers were still talking and laughing, but they were growing closer. Lleu held his breath, half-expecting one of them to recognize Cian. But instead, they all headed towards the mystery section.

Lleu let out a relieved sigh. "Well," he said, trying to keep his voice stern. "I suppose you're safe enough here for now. But you'll have to behave yourself. I won't have you causing any trouble."

Cian's smile faltered slightly. "I wouldn't dream of it. Besides, I'm just here to hide. I'm not looking for any trouble."

Lleu couldn't help but feel a flicker of attraction. Cian was charming, there was no denying that. But there's something else too, beneath the charm. Something vulnerable.

"Well," Lleu said, trying to keep his voice stern. "I suppose I can cut you some slack. Besides, I've always wanted to meet someone famous. I'm sure you're a fascinating person."

Cian's smile faltered slightly. "I don't know about that. I'm just a regular guy. I guess I'm just lucky enough to have found myself in the spotlight."

The scene ends with an undercurrent of unspoken chemistry. The bookstore owner, Lleu, is outwardly stern and unimpressed, but inwardly, he's charmed and flustered. Cian, the famous actor, is charming but vulnerable, his usual charm offensive derailed by Lleu's superficial rebuffs. He's genuinely attracted to Lleu's apparent immunity to his charms, which is something he's never encountered before.

The scene is set against the backdrop of a cozy Welsh bookstore, with the late afternoon light slanting through the windows and the faint scent of coffee in the air. The teenagers' laughter and the hum of the old radiator create a sense of warmth and familiarity that contrasts with Cian's chaotic, high-stakes world.


<B>Generation #2 Temp .5</B>

Love in the Limelight: A Scene in Wales

The bell above the door chimed, its soft ring barely audible over the hum of the small-town bookstore. The morning light spilled through the large windows, dancing on the spines of well-worn novels and leather-bound classics. Behind the counter, Eleri Price was lost in a conversation with an elderly customer about the merits of Welsh folk tales when the air suddenly crackled with the kind of electric tension that only one thing could summon: celebrity.

She didn’t look up immediately. The man who strode inside had an air of urgency, his dark hair slightly tousled, his sharp features tense. He wore sunglasses indoors, which was absurd, but she couldn’t ignore the way the local gossip mill would buzz if she pointed it out. Instead, she simply waited for the inevitable.

The stranger lingered by the mystery section before finally approaching the counter, his footsteps hesitant. The elderly customer, Mrs. Jenkins, gave him a knowing smile. "You must be that actor everyone’s been talking about. The one with the paparazzi outside?"

Eleri shot Mrs. Jenkins a warning glare, but the woman merely patted her hand and wandered toward the historical fiction shelves.

The man exhaled, his shoulders tensing. "That obvious, am I?" He removed his sunglasses, revealing piercing green eyes that flickered with something between amusement and exasperation. "I was hoping to go unnoticed."

Eleri raised an eyebrow. "In Aberthyrn? You’d have better luck in a town with more than three traffic lights."

He smirked, though there was something brittle in it. "I’m Rhys Morgan. And you are…?"

"Eleri Price. Bookstore owner. And, at the moment, your best shot at evading those vultures outside."

Rhys’s gaze flicked toward the door, then back to her. There was a hunger in his stare, the kind that asked: Do you like me yet? "You’re the only one who hasn’t fawned over me since I stepped in. That’s either refreshing or concerning."

Eleri shrugged, pretending to straighten a stack of books. "I don’t fawn. It’s bad for business."

Rhys laughed, a rich, throaty sound that felt too intimate for a chance meeting. "So, what’s your secret? How can I avoid them?"

She finally met his eyes, noting the way his pupils dilated slightly. "You could try blending in. But you’re tall, loud, and wearing sunglasses inside, so that’s a lost cause."

He leaned against the counter, his voice dropping to a conspiratorial whisper. "Maybe I was hoping you’d help me disappear."

Eleri felt her pulse quicken but kept her tone bored. "I’m not much for disappearing. But if you want to lose them, you’ll have to pretend to be someone else entirely."

Rhys straightened, his grin widening. "Now that’s a challenge I like. How do I do that?"

She sighed, feigning resignation. "You could try being quiet. Or better yet—boring."

"Boring is overrated." He stepped closer, his voice teasing. "Besides, you’re clearly not bored."

Eleri turned away, pretending to shelve a book. The truth was, she was anything but immune. Rhys Morgan was the kind of man who radiated magnetism, the sort of effortless charm that made hearts flutter. But she’d met his type before—men who thrived on adoration, who needed it like oxygen. And yet, beneath the bravado, there was a flicker of vulnerability, as though he half-expected her to see through the charm.

She handed him an old edition of a Welsh folklore book. "If you really want to disappear, maybe start by being genuinely interested in something. Try that."

Rhys flicked through the pages, his eyes lighting up. "You’re a tough audience, aren’t you?"

"Just realistic," she said, though the warmth in her chest betrayed her.

He lingered for a moment longer, as though debating whether to ask her out or simply bask in the thrill of the game. But whatever he was about to say was cut off by the distant shouts of photographers outside. His shoulders stiffened.

"You should probably go," Eleri said, trying to ignore the pang of disappointment. "Through the back. I’ll stall them."

Rhys hesitated, his eyes meeting hers once more. "I’ll be back. To apologize for the disruption. And to ask you out properly."

Eleri rolled her eyes, but there was a smile tugging at the corners of her lips. "You’re persistent. I’ll give you that."

He winked. "And you’re stubborn. I’ll see you soon, Eleri Price."

Then, with a flourish worthy of a Shakespearean villain, Rhys Morgan vanished through the back door, leaving behind nothing but the faintest scent of cologne and the lingering hum of something electric.

Eleri exhaled, her fingers brushing the book he’d been holding. She wasn’t fooled by his charm—but that didn’t mean she wasn’t just a little bit enchanted anyway.


