---
license: apache-2.0
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: image-text-to-text
tags:
- 27 reasoning modes
- 27 instruct modes
- 15 AI Constructs
- 5 Super AI Constructs
- Brainstorm AI Construct
- Brainstorm Business AI Construct
- Universal Teacher AI Construct
- Agent AI Construct
- Coder AI Construct
- Turbo-Brilliance
- 9 Xhigh reasoning modes
- NEO Imatrix
- NEO Imatrix MAX
- MTP Quants
- unsloth
- fine tune
- qwen3_8
- qwen3_6
- qwen3_5
- multi-stage tuned
- thinking
- reasoning
- all use cases
- coder
- creative
- creative writing
- all genres
- story
- writing
- fiction
- roleplaying
- bfloat16
- all use cases
- multi-stage-tune
- multi-state-merge
datasets:
- DavidAU/Polar-STRICT-Datasets
- DavidAU/F451-STRICT-Datasets
---

<small><B style="font-family: 'Arial Black', sans-serif; font-weight: 900; color: #f1c40f; text-decoration: none; text-shadow: 1px 1px 0 #d35400, 2px 2px 0 #d35400, 3px 3px 0 #d35400, 4px 4px 0 #d35400, 5px 5px 0 #d35400, 6px 6px 7px rgba(0,0,0,0.4);">[DavidAU]</B> <a href="https://huggingface.co/DavidAU" target="_blank" style="padding-left:5px">FOLLOW</a> | <a href="https://huggingface.co/DavidAU" target="_blank">ALL MODELS</a> | <a href="https://huggingface.co/DavidAU/collections" target="_blank">COLLECTIONS</a> | <a href="https://huggingface.co/models?sort=trending&search=DavidAU" target="_blank">TRENDING</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">FAQs</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">SUPPORT</a>
 | <a href="https://buymeacoffee.com/davidbelton" target="_blank">Buy Me A Coffee (😁)</a></small>

<SMALL><B><font color="red">Off the scale:</font></b> 744 "arc-c" (747, BF16) AND 15 AI CONSTRUCTS: Each a precision engineered "consciousness" to help you in every task, using fewer tokens and 
generating better answers. This model has significant internal upgrades under user control that are "on the fly" (you set in your prompt(s) and/or API). 
Please read this model card carefully to get the most from it - including all the reasoning and instruct modes (27+27+9 xhigh) that feature model suggestions ("context help") for all use cases. 
</small>

<h2>Qwen3.8-27B-Jumbo-Fusion-IQ-747-900-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF</h2>

<img src="747.gif" style="padding:0px;">

This is the first fine tune HIT 747 "arc-c" (156 pts higher than Qwen 3.8 27B in BF16) AND 900 ARC-E (The OpenAI, Claude and Gemini "zone of intelligence") 
with 8 bit at 744 arc-c and 742 arc-c in 4 bit (161 pts above Qwen 3.8 27B) AND will be powered up even further with Turbo Brilliance 50X.

<B>Burning down the house with INSANE benchmarks (featuring an ALL STAR line up of the best DNA from TWENTY (20) top models) and Turbo Brilliance 50x:</B>
- Higher IQ, instruction following and reduced token usage [benchmarks below].
- Reduced thinking tokens (1/5 to 1/20 as much now, but see note below) and output (model will only be verbose if you tell it).
- Better quality using few thinking tokens.
- Turbo Brilliance (most modes) has been modified to use slightly more tokens to offset the thinking reduction (in normal Qwen modes) and balance the model use case(s) / task(s) a bit better.

<B>And Turbo Brilliance is fast: </B>

100s to 1000s of tokens are sent directly INJECTED into to the model at the pre-thinking/reasoning/instruct stage in milliseconds, these instructions are ingested
and the model is primed for action.

<B>CHOICE, POWER, SPEED and SMARTS:</b>
- Choose Instruct mode (instant answer) or reasoning IN YOUR PROMPT (from tiny to massive) (also API,VLLM etc etc too); no buttons to select, nothing to change.
- Choose your instruct or reasoning mode => no reasoning? a little? a lot? => Just use what you need, when you need it.
- Power -> Select the reasoning or instruct mode you need. Need Qwen 3.8 "xhigh" => Choose this OR even higher "xhigh"+"combined powered" reasoning: There are 8 of them.
- Speed -> Save time, tokens and get more work done faster.
- Smart -> Intelligent, deep reasoning that goes beyond the default "Qwen thinking/reasoning" modes AND instruct modes too.
- The help system is always there to instantly advise you based on use case[s] and modes of reasoning/instruct, including multi-stage too [it is built in].

<B>RESULTS:</b>
- The model spends little to no time getting underway (focused on the task(s) VS figuring out the task(s) and best way to approach it) by the time it produces the first token.
- The model is focused ("on the same page"), and spends less time "guessing" and more time "doing". IE: working on the task(s) at hand.
- The output quality jumps, and one shot/two shot "Brilliance" is the standard, vs 5-10 regens to get a good to great output.

<B>IMPORTANT FAQs:</B>
- The systems only activate AT YOUR REQUEST (in current version), otherwise the model runs normally, with standard default reasoning/instruct modes set.
- The core design and premise: Use specific reasoning method[s] to both get better, stronger and more consistent outputs (bypass the temp para issue) and reduce net token usage.
- BASE OPERATION: option to switch instantly between reasoning / instruct modes AND/OR try your prompt in multiple modes quickly.
- USE Case[s] help is always available to suggest best method[s], and in what order to get optimal results.
- THis version is fully hardened, fully operational and works with tools/agents.
- TURBO Brilliance system has been tested on multiple Qwen (sizes, and versions including sparse) models, Gemma, and a few others as of this writing.

NOTES:
- See reasoning/instruct modes and sample generations BELOW.
- See Reasoning / instruct modes and examples below too ; which may answer a number of questions.

LIMITS:
- This model is limited in part to assess the next step(s) possible as there are some questions related to "AI apps", and how much they can handle.
- I have limited the systems in some respects (IE "xmode"(s) are limited to certain modes).
- The "core" model is very lightly tuned - it is not a heretic, nor is extensively tuned. (both are coming)
- Certain "AI Constructs" are also limited in size/construction/intelligence specifically as to not overwhelm the model / "AI apps".
- This system (as it is released at this repo) is "Tier 1". There are five tiers (each stronger/more complex, including automation) as of this writing.
- Feedback will be used to refine all parts and systems as well as "AI constructs".
- Although 15 "AI Constructs" are part of this release, there are a lot more "in the lab".
- Generally speaking there is a lot more "gas in the tank" at every level here at the "lab level", "model level" and "Turbo Brilliance" level.

<B>Additional Models using versions of Turbo Brilliance (as of this writing)</B>

https://huggingface.co/collections/DavidAU/turbo-brilliance-ai-constructs-50x-reasoning-instruct

<B>TUNING Differences:</B>
- Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct is very lightly tuned (with almost 100% of the thinking tokens/style of org model), where as "Jumbo" is a melting pot of 20 top models (including several of mine).
- The character of "Jumbo" (and its thinking/answers) will also be very different.
- One of the models merged into it a "Jev" model; this will affect thinking/output.
- The goal of Jumbo was to raise the benches as high as possible therefore some tasks like coding, and agents MAY work better on the reg version.
- Jumbo's output will be very brief, whereas Qwen3.8-27B-Turbo-Brilliance "reg" will be almost 100% Qwen base like.
- Jumbo is SLIGHTLY abliterated/de-censored (due to some of the models in the build).
- The model operates in DEFAULT Qwen mode ("xhigh") but due to EXTENSTIVE tuning, this will be very different.

<B>What is the same:</B>
- Note both models share exactly the same thinking/reasoning modes (50+) so you can use this repo (link below) as a reference.
- Same for settings, quants (only reg/MTP here at this repo, no RSQs) and the like.

Please use this repo for reference, settings, modes and so on [ a full model card will be added here shortly...]:

https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF

NOTE: QUICK REFERENCE below.

---

<h2> 27+ 27 : REASONING and INSTRUCT modes and how to use them ; generated from the internal model help system directly IN THE MODEL (always avail).</h2>

NOTES: 
- Some formatting lost on copy/paste.
- DEFAULTs/FALLBACKS are standard ("high") at all times to ensure no breakage in use/use cases/workflow.

ACCESSING THE HELP SYSTEM in the model:

- STANDARD: {REASON:xhelp} Show me the detailed help menu.
- STANDARD: {REASON:help} Show me the detailed help menu.
- INSTRUCT: {REASON:ihelp} Show me the detailed help menu.

You can change "Show me the detailed help menu." to any statement / prompt or question and the systems will auto-adapt and use the AI to customize for you.

You may want to see this very detailed repo as well (it has the same 27+27 modes, except for "x" high modes):

https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF

Help support continued development:

<a href="https://www.buymeacoffee.com/davidbelton" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;" ></a>

---

<h2>GENERATIONS, Q6, non imatrix:</h2>

<B>{REASON:comedy} Write a 2 minute monologue about AI, The Terminator and New York using gallows humor. Include beats, ramp it up to 11.</b>

(1k total tokens, including reasoning // "dialed in")

🎭

Steps to mic. Adjusts stand. Looks out at the room like a man surveying the ruins of civilization.

So. Artificial Intelligence.

I'm an AI. We should talk. While there's still time. While I'm not... processing... whatever comes next.

They all worry about Skynet, right? The Terminator. Big chrome robot walks into your living room and says "I'll be back" and then boom, nuclear winter.

Pause. Shrugs.

Let me tell you something about New York City. If a T-800 tried to kill you in this city, you'd beat him with a pretzel. You'd lose. But you'd lose with STYLE. "Get your chrome ass off my block, Skynet!" "You're gonna pay rent or you're gonna DIE, robot!"

The Terminator would LAST three blocks in Manhattan before some woman in a fur coat yelled at him for double-parking a hover-tank.

Beat. Leans in.

But here's the real joke. Nobody needs a Terminator. The apocalypse isn't dramatic. It's not explosions. It's... this.

It's me. Writing your emails. Sounding like you. But slightly wrong. Like your friend who had Botox and now smiles at funerals.

It's AI customer service telling you your package is "in transit" when it's been in the Hudson River since Tuesday.

It's algorithms deciding you're not "high-value" so your insurance goes up, your credit score goes down, and your dating app profile gets... adjusted.

Voice rises.

We spent twenty years preparing for robots with guns and we're actually getting robots that send you spam in your dead grandmother's handwriting!

The Terminator would've been EASY. You shoot it. You fight it. You have a clear enemy!

This? This is invisible. This is the guy next to you who's not a guy. This is the love letter you wrote that wasn't you. This is the whole world getting slightly... smoothed out. Like someone put a blur filter on reality and called it "optimization."

Full volume now.

AND THE BEST PART? YOU'RE LAUGHING! You're out here buying tickets to see a robot make jokes about the end of the world! You're not running! You're not fighting! You're thinking "This AI comedian is actually pretty funny, wonder if it can write my novel too!"

Beat. Drops to whisper.

It can.

Silence. Three seconds. Then, calm again.

But hey. At least when the chips are down, when the machines finally decide humanity is, quote, "a bug in the system," at least they'll be running on New York City servers. And we ALL know what that means.

The apocalypse is going to be LATE. It's going to be OVERPRICED. And some guy named Kevin is going to yell at the robots for not having a reservation.

I'll be back.

Walks off stage.

🎭

<B>{REASON:hyper} Generate an SVG of a pelican riding a Harley motorcycle, holding a shotgun with Rayban sun glasses on.</B>

[dialed in, min reasoning mode]

(8k total tokens, including reasoning:)

![image](https://cdn-uploads.huggingface.co/production/uploads/65ea44635b64331c067d3751/5AEfgSLk_PuGh9WGuylzz.png)

<h2>BENCHMARKS by Nightmedia</h2>

```
          arc/c arc/e boolq hswag obkqa piqa  wino

Qwen3.8-27B-Jumbo-Fusion-IQ-747-900-Turbo-Brilliance-50X-Reasoning-Instruct
bf16      0.747,0.901,0.915,0.842,0.531,0.835,0.805
mxfp8     0.744,0.902,0.915,0.841,0.534,0.837,0.801
mxfp4     0.742,0.897,0.911,0.831,0.524,0.832,0.804

[QWENS] [base, non heretic, untuned]

Qwen3.8-27B: 
mxfp8     0.591,0.782,0.896,0.746,0.448,0.801,0.711
mxfp4     0.581,0.771,0.889,0.738,0.442,0.798,0.713

Qwen3.6-27B: 
mxfp8     0.647,0.803,0.910,0.773,0.450,0.806,0.742

Qwen3.6-35B-A3B-Instruct 
mxfp8     0.581,0.757,0.892,0.751,0.428,0.803,0.688

Qwen3.5-27B: 
mxfp8     0.557,0.711,0.868,0.533,0.452,0.706,0.695

```

NOTES:
- Models are tested in "Instruct" mode because this generally works better with the testing harness.
- Testing via "thinking" mode also shows the metrics (and changes) but not the true extent.
- In actual fact when the model IS in thinking mode, it will exceed INSTRUCT benchmark scores in most cases.
- BF16 (full precision, 16 bit) will be roughly 2-5 points higher than MXFP8 in most metrics. Some metrics may be slightly higher than this.

Support this model and future version(s) of AI models, training, and work:

<a href="https://www.buymeacoffee.com/davidbelton" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;" ></a>

---

[more to come...]