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
- roleplay
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

<H2>Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning</H2>

<img src="matrix-neo-reloaded-fight.gif" style="float:right; width:300px; height:300px; padding:10px;">

What madness is this?

Someone found "Llama3.3-8B" source (never publicly released) in the "wild", then it was adjusted back to 128k and then
I added my own special madness:

Training the model with Unsloth (3 epochs) and Claude 4.5-Opus High Reasoning dataset.

This has created an Instruct/Thinking hybrid (128k context, Llama 3.3 model).

Note this tuning was only to create an instruct/thinking model, not to update the model's core knowledge / root training.

1 example at bottom of the page.

<B>HERETIC / Uncensored Version:</B>

https://huggingface.co/DavidAU/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning

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

Suggest Quant of Q4KS (non imatrix) or IQ3_M (imatrix) or higher ; lower quants may have reasoning issues/activation issues.

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

PROMPT:

<B>
Explain orbital mechanics including detailed math and examples.
</B>

Thinking/OUTPUT:

<style type="text/css">
		@page { size: 21cm 29.7cm; margin: 2cm }
		p { line-height: 115%; margin-bottom: 0.25cm; background: transparent }
		h2 { margin-top: 0.35cm; margin-bottom: 0.21cm; background: transparent; page-break-after: avoid }
		h2.western { font-family: "Liberation Serif", serif; font-weight: bold; font-size: 18pt }
		h2.cjk { font-size: 18pt; font-family: "NSimSun"; font-weight: bold }
		h2.ctl { font-family: "Lucida Sans"; font-size: 18pt; font-weight: bold }
		h3 { margin-top: 0.25cm; margin-bottom: 0.21cm; background: transparent; page-break-after: avoid }
		h3.western { font-family: "Liberation Serif", serif; font-weight: bold; font-size: 14pt }
		h3.cjk { font-size: 14pt; font-family: "NSimSun"; font-weight: bold }
		h3.ctl { font-family: "Lucida Sans"; font-size: 14pt; font-weight: bold }
		h1 { margin-bottom: 0.21cm; background: transparent; page-break-after: avoid }
		h1.western { font-family: "Liberation Serif", serif; font-weight: bold; font-size: 24pt }
		h1.cjk { font-size: 24pt; font-family: "NSimSun"; font-weight: bold }
		h1.ctl { font-family: "Lucida Sans"; font-size: 24pt; font-weight: bold }
		h4 { margin-top: 0.21cm; margin-bottom: 0.21cm; background: transparent; page-break-after: avoid }
		h4.western { font-family: "Liberation Serif", serif; font-weight: bold; font-size: 12pt }
		h4.cjk { font-size: 12pt; font-family: "NSimSun"; font-weight: bold }
		h4.ctl { font-family: "Lucida Sans"; font-size: 12pt; font-weight: bold }
		td p { orphans: 0; widows: 0; background: transparent }
		th p { font-weight: bold; orphans: 0; text-align: center; widows: 0; background: transparent }
		pre { background: transparent }
		pre.western { font-family: "Liberation Mono", monospace; font-size: 10pt }
		pre.cjk { font-size: 10pt; font-family: "NSimSun", monospace }
		pre.ctl { font-family: "Liberation Mono", monospace; font-size: 10pt }
		strong { font-weight: bold }
		code.western { font-family: "Liberation Mono", monospace }
		code.cjk { font-family: "NSimSun", monospace }
		code.ctl { font-family: "Liberation Mono", monospace }
	</style>

<span style="display: inline-block; border: none; padding: 0cm">llama-3.3-8b-instruct-claude-4.5-opus-high-reasoning-checkpoint-90-q4_k_s.gguf</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><font color="#ff4000"><b>Thought
for 19.49 seconds</b></font></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
is a comprehensive request about orbital mechanics. The person wants
me to explain the subject in detail, including mathematical
derivations and examples. Let me organize this thoroughly.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I'll
cover:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Fundamentals
	of Orbital Mechanics</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Kepler's
	Laws</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Elliptical
	Orbits</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbital
	Elements</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Vis-Viva
	Equation</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Semi-Analytical
	Methods</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Numerical
	Integration</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
each section, I'll include mathematical derivations and examples.</span></p>
<h2 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">1.
Fundamentals of Orbital Mechanics</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbital
mechanics deals with the motion of objects in space under
gravitational forces. The two-body problem (one object orbiting
another) is fundamental.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
quantities:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Semi-major
	axis (a)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Eccentricity
	(e)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbital
	period (T)</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Gravitational
	parameter (μ = GM)</span></p></li>
</ul>
<h2 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">2.
Kepler's Laws</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Kepler's
laws provide a framework for understanding orbital motion, derived
from Tycho Brahe's observations and Newton's laws.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">First
Law: Law of Ellipses</span></h3>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">An
orbit is an ellipse with one focus at the center of mass of the
system.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Second
Law: Equal Area Rule</span></h3>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
line connecting the planet to the Sun sweeps out equal areas in equal
times.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Third
Law: Harmonies of the Spheres</span></h3>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">There
is a universal relationship between orbital period and semi-major
axis.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mathematically:
T² = (4π²/GM) * a³</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Or
for Earth around the Sun: T² ≈ 9.95 × 10⁷ * a³</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
circular orbits: v²/a = GM/r² = GM/a² = μ/a</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbital
Velocity</span></h3>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
velocity of an object in orbit depends on its distance from the
center of gravity.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
circular orbits: v = √(GM/r)</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
elliptical orbits (vis-viva equation): v² = GM(2/r - 1/a)</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbital
energy is a fundamental concept in understanding orbital mechanics.
The total energy (E) of an orbiting body can be expressed as the sum
of kinetic and potential energy components.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
circular orbits, the total energy is: E = -GM²/2a</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
reveals the negative sign indicating gravitational binding energy
that keeps the object in continuous orbit around a celestial body.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
orbital parameters include semi-major axis (a), eccentricity (e),
inclination (i), longitude of the ascending node (Ω), argument of
periapsis (ω), and true anomaly (f). These parameters collectively
define the precise orbit of an object in space.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
elliptical orbits, the shape is determined by the semi-major axis
(a), eccentricity (e), and focal length (c = ae). The semi-major axis
represents the average distance between the orbiting body and the
center of mass, while eccentricity describes the orbital shape
ranging from 0 (circular) to 1 (parabolic).</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Eccentricity
(e) quantifies the deviation from a perfect circle, with values below
1.0 indicating elliptical shapes and 1.0 or higher representing
parabolic trajectories.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbital
elements are critical parameters that define an object's orbital
characteristics. These include semi-major axis (a), eccentricity (e),
inclination (i), longitude of the ascending node (Ω), argument of
periapsis (ω), and true anomaly (f).</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Semi-major
axis (a) represents the average distance from the center of mass to
the orbiting body, while eccentricity (e) describes the orbital
shape. Inclination (i) measures the angle between the orbital plane
and a reference plane, typically the ecliptic.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Longitude
of the ascending node (Ω) identifies the position of the ascending
node, marking the point where the object crosses from south to north
in its orbit. Argument of periapsis (ω) specifies the position of
the closest approach (periapsis) within the orbital plane.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">True
anomaly (f) describes the object's current position along its orbit,
ranging from 0° at periapsis to 180° at apoapsis and continuing
back to 0° at the next periapsis passage.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Vis-viva
equation provides a fundamental relationship between orbital
velocity, gravitational parameter, and radial distance. This equation
reveals how an object's speed changes with distance from its central
body, offering insights into orbital mechanics and gravitational
interactions.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
elliptical orbits, the vis-viva equation extends beyond circular
motion by incorporating eccentricity (e) and radial distance (r). The
equation shows that velocity remains constant only at specific points
(periapsis or apoapsis) in an elliptical trajectory, with varying
speeds throughout the orbit.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Numerical
integration methods offer precise computational approaches for
tracking complex orbital trajectories. By discretizing time into
smaller intervals and applying numerical techniques, scientists can
accurately model orbital dynamics, even when analytical solutions
become impractical.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
numerical integration techniques include Runge-Kutta methods, Verlet
algorithms, and symplectic integrators. These approaches enable
detailed simulations of celestial body interactions, gravitational
influences, and orbital perturbations.</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><font color="#ff4000"><b>OUTPUT:</b></font></span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<h1 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">Orbital
Mechanics: A Comprehensive Guide</span></h1>
<h2 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">Table
of Contents</span></h2>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Fundamentals
	&amp; Assumptions</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Kepler's
	Laws</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbital
	Elements</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Vis-Viva
	Equation</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Semi-Analytical
	Methods</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Numerical
	Integration</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Perturbations
	&amp; Stability</span></p></li>
</ol>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">1.
Fundamentals and Assumptions</span></h2>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">1.1
Two-Body Problem</span></h3>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
fundamental problem in orbital mechanics: two point masses moving
under their mutual gravity.</span></p>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Assumptions:</span></h4>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Inverse
	Square Law</strong>&nbsp;- Gravitational force varies inversely with
	square of distance</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">F
		= G * (m₁m₂) / r²</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Universal
	Gravitational Constant</strong>&nbsp;- Same everywhere in the
	universe</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">G
		= 6.67408 × 10⁻¹¹ N*m²/kg²</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Negligible
	External Forces</strong>&nbsp;- No other gravitational influences
	present</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Non-Rotating
	Reference Frame</strong>&nbsp;- No additional angular momentum</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>No
	Atmospheric Drag</strong>&nbsp;- Vacuum environment</span></p></li>
</ol>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">1.2
Orbital Parameters</span></h3>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Parameter</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Description</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Range</p>
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>a</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Semi-major axis</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, ∞)</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>e</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Eccentricity</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, 1]</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>T</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Orbital period</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, ∞)</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>r</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Radial distance</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, a]</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>v</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Orbital velocity</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, v₀ = √(GM/a)]</p>
			</td>
		</tr>
	</tbody>
</table>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Notation:</span></h4>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>m</strong>&nbsp;and&nbsp;<strong>M</strong>&nbsp;-
	Masses of orbiting body and central body</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>G</strong>&nbsp;-
	Gravitational constant (6.67408 × 10⁻¹¹ N*m²/kg²)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>μ</strong>&nbsp;=
	GM - Reduced gravitational parameter</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>r</strong>&nbsp;-
	Radial distance from center to orbiting object</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>a</strong>&nbsp;-
	Semi-major axis of orbit</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">2.
Kepler's Laws of Planetary Motion</span></h2>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">2.1
First Law: Law of Ellipses</span></h3>
<p style="margin-right: 1cm; margin-left: 1cm; border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">&quot;An
ellipse is described whose foci are the centers of the two bodies,
and the line connecting the two bodies passes through one focus and
sweeps out equal areas in equal times.&quot;</span></p>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mathematical
Formulation:</span></h4>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Eccentricity</strong>
	(e): Ratio of distance from focus to vertex</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">e
		= c/a (where c = ae)</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Focus
	Position</strong>: Focus F₁ is at a distance c from center O</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Position
		vector: r₁ = c * (cos(θ) î + sin(θ) ĵ)</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Focus
	F₂</strong>: At distance c from center O in opposite direction</span></p>
	<ul>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">r₂
		= -c * (cos(θ) î + sin(θ) ĵ)</span></p></li>
	</ul>
</ul>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Proof:</span></h4>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Step</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Description</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Formula</p>
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>1</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Define ellipse with foci
				at O and O'</p>
			</td>
			<td style="border: none; padding: 0cm"><p>x²/a² + y²/b² = 1</p>
			</td>
		</tr>
	</tbody>
</table>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>2</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Parameterize with angle
				θ</p>
			</td>
			<td style="border: none; padding: 0cm"><p>x = a * cos(θ), y = b *
				sin(θ)</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p>3</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Apply trigonometric
				identity</p>
			</td>
			<td style="border: none; padding: 0cm"><p>cos²(θ) + sin²(θ) =
				1</p>
			</td>
		</tr>
	</tbody>
</table>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>4</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Express semi-major axis
				(a) and eccentricity (e)</p>
			</td>
			<td style="border: none; padding: 0cm"><p>a² = b²/a² → b² =
				a²(1-e²)</p>
			</td>
		</tr>
	</tbody>
</table>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>5</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Derive equation of
				ellipse in standard form</p>
			</td>
			<td style="border: none; padding: 0cm"><p>x²/a² + y²/b² = 1</p>
			</td>
		</tr>
	</tbody>
</table>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
Equations:</span></h4>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Equation</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Description</p>
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>r = a * (1 - e²)/[1 + e
				* cos(θ)]</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Radial distance from
				focus</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p>T = 2π√(a³/μ)</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Orbital period for
				elliptical orbit</p>
			</td>
		</tr>
	</tbody>
</table>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">2.2
Second Law: Equal Area Rule</span></h3>
<p style="margin-right: 1cm; margin-left: 1cm; border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">&quot;The
line connecting the planet to the Sun sweeps out equal areas in equal
times.&quot;</span></p>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mathematical
Proof:</span></h4>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Angular
	Momentum</strong>&nbsp;Conservation: L = r × m v = constant</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Area
	Sweep</strong>: dA = (1/2)r × v dθ = (1/2)r² dθ/v</span></p></li>
</ol>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Step</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Description</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Formula</p>
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>3</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Relate angular momentum
				to area sweep</p>
			</td>
			<td style="border: none; padding: 0cm"><p>dA/dt = r²/(2v) dθ/dt</p>
			</td>
		</tr>
	</tbody>
</table>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>4</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Substitute v from energy
				equation</p>
			</td>
			<td style="border: none; padding: 0cm"><p>dA/dt = r²/(2v) *
				(GM/r²)/r</p>
			</td>
		</tr>
	</tbody>
</table>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>5</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Simplify to show
				proportional relationship</p>
			</td>
			<td style="border: none; padding: 0cm"><p>dA/dt ∝ r/v ∝ 1/r</p>
			</td>
		</tr>
	</tbody>
</table>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Geometric
Interpretation:</span></h4>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Area
	swept out is proportional to time elapsed</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Rate
	of area sweep decreases with increasing radius</span></p></li>
</ul>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">2.3
Third Law: Harmonies of the Spheres</span></h3>
<p style="margin-right: 1cm; margin-left: 1cm; border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">&quot;The
square of the orbital period of a planet is proportional to the cube
of its semi-major axis.&quot;</span></p>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mathematical
Formulation:</span></h4>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">T²
= (4π²/GM) * a³</span></p>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Planet</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Semi-major Axis (AU)</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Orbital Period (Years)</p>
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>Mercury</p>
			</td>
			<td style="border: none; padding: 0cm"><p>0.387</p>
			</td>
			<td style="border: none; padding: 0cm"><p>0.241</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p>Venus</p>
			</td>
			<td style="border: none; padding: 0cm"><p>0.723</p>
			</td>
			<td style="border: none; padding: 0cm"><p>0.615</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p>Earth</p>
			</td>
			<td style="border: none; padding: 0cm"><p>1.000</p>
			</td>
			<td style="border: none; padding: 0cm"><p>1.000</p>
			</td>
		</tr>
	</tbody>
</table>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Universal
Gravitational Constant (G):</span></h4>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">G
	= 39.478 × 10⁻¹³ km³/Sec²/gm² ≈ 6.67408 × 10⁻¹¹ m³
	kg⁻¹ s⁻²</span></p></li>
</ul>
<h4 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Derived
Values:</span></h4>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Solar
	mass: Mₛ = 1.989 × 10³⁰ kg</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbital
	speed: v = √(GM/r) ≈ 29.78 km/s at Earth's orbit</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">3.
Orbital Elements</span></h2>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.1
Semi-Analytical Method Overview</span></h3>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Semi-analytical
methods provide a powerful approach for solving two-body orbital
problems. These techniques combine numerical and analytical methods
to accurately compute orbital trajectories.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
semi-analytical method involves three key steps:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Numerical
	Integration</strong>: Discretize the orbit into smaller time
	intervals and apply numerical integration techniques to approximate
	the position of the object at each step.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Interpolation</strong>:
	Use interpolation methods to estimate the position of the object
	between discrete time points.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Analytical
	Correction</strong>: Apply analytical corrections to refine the
	position and velocity of the object based on Kepler's equations.</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
numerical integration techniques include Runge-Kutta methods, Verlet
algorithms, and symplectic integrators. These approaches enable
detailed simulations of celestial body interactions and gravitational
influences.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.2
Semi-Analytical Formulation</span></h3>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
semi-analytical method uses a combination of numerical and analytical
techniques to compute orbital trajectories. The approach involves
three primary steps:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Numerical
	Integration</strong>: Discretize the orbit into smaller time
	intervals and apply numerical integration techniques such as
	Runge-Kutta or Verlet methods.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Analytical
	Correction</strong>: Use Kepler's equations to refine the position
	and velocity of the object at each discrete time point.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Interpolation</strong>:
	Apply interpolation techniques such as cubic spline or Lagrange
	interpolation to estimate the position of the object between
	discrete time points.</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
semi-analytical method provides a robust approach for computing
orbital trajectories with high accuracy and efficiency. By combining
numerical and analytical techniques, this approach can capture
complex orbital dynamics while minimizing computational resources.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.3
Key Semi-Analytical Formulas</span></h3>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Formula</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Description</p>
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p>r = a * (1 - e²)/(1 + e
				* cos(θ))</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Radial distance from
				focus</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p>v = √(GM/a) * (1 -
				e²)/(1 + e * cos(θ))</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Orbital velocity</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p>T = 2π√(a³/μ)</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Orbital period</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p>f = arctan((r² + b² -
				a²)/2ab)</p>
			</td>
			<td style="border: none; padding: 0cm"><p>True anomaly</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p>E = √(GM/a) * (1 -
				e²)/(1 + e * cos(θ))</p>
			</td>
			<td style="border: none; padding: 0cm"><p>Eccentric anomaly</p>
			</td>
		</tr>
	</tbody>
</table>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">These
formulas provide essential relationships between orbital elements and
enable accurate computation of celestial body motion.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.4
Semi-Analytical Implementation</span></h3>
<pre class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><code class="western">import numpy as np</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">from scipy.integrate import odeint</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">import matplotlib.pyplot as plt</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Define constants</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">G = 6.67408e-11  # Gravitational constant (m^3 kg^-1 s^-2)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">M_sun = 1.98910e30  # Mass of Sun (kg)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">def vis_viva(y, t):</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&quot;&quot;&quot;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">Vis-viva equation: v² = GM/r</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&quot;&quot;&quot;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">r = y[0]  # Radial distance</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">v = np.sqrt(G * M_sun / r)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">return [v]</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Initial conditions</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">r0 = 1.496e11  # Average distance from Sun (meters)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">v0 = 29.78e3  # Orbital velocity (m/s)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Time array</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">t = np.linspace(0, 10 * 365.25 * 24 * 3600, 10000)  # 10 years</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Initial state vector</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">y0 = [r0]</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Solve ODE</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">solution = odeint(vis_viva, y0, t)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot radial distance over time</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(t/3600/24/365.25, solution[:, 0]/1e9)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Time (Years)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Radial Distance (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Earth\'s Orbital Motion')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span></pre><p style="border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">This
Python code implements the semi-analytical method using numerical
integration and analytical corrections. The </span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">vis_viva</code></span><span style="display: inline-block; border: none; padding: 0cm">
function computes the orbital velocity based on Kepler's equation,
demonstrating a fundamental relationship in celestial mechanics.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
code then generates a 10-year simulation of Earth's orbital motion
around the Sun. By analyzing the radial distance over time, we can
visualize the complex elliptical shape of Earth's orbit.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.5
Implementation Details</span></h3>
<table cellpadding="2" cellspacing="2">
	<thead>
		<tr>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Parameter</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Description</p>
			</th>
			<th style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm"><p>
				Range</p>
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>a</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Semi-major axis</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, ∞)</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>e</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Eccentricity</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, 1]</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>T</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Orbital period</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, ∞)</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>r</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Radial distance</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, a]</p>
			</td>
		</tr>
		<tr>
			<td style="border: none; padding: 0cm"><p><span style="display: inline-block; border: none; padding: 0cm"><strong>v</strong></span></p>
			</td>
			<td style="border: none; padding: 0cm"><p>Orbital velocity</p>
			</td>
			<td style="border: none; padding: 0cm"><p>[0, v₀ = √(GM/a)]</p>
			</td>
		</tr>
	</tbody>
</table>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">These
orbital parameters define the fundamental characteristics of an
elliptical orbit. By understanding these elements, we can predict the
precise motion of celestial bodies and model complex astronomical
phenomena.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
semi-analytical method offers a powerful approach for analyzing
orbital mechanics. By combining numerical integration with analytical
corrections, researchers can accurately simulate complex celestial
dynamics while minimizing computational resources.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.6
Key Implementation Steps</span></h3>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Define
	Orbital Parameters</strong>: Specify the semi-major axis,
	eccentricity, and initial conditions for the orbit.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Discretize
	Time Array</strong>: Divide the simulation into smaller time
	intervals to enable numerical integration.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Implement
	Numerical Integration</strong>: Use techniques like Runge-Kutta or
	Verlet algorithms to approximate the position of the object at each
	time step.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Apply
	Analytical Corrections</strong>: Refine the position and velocity
	using Kepler's equations to achieve high accuracy.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Visualize
	Orbital Trajectory</strong>: Plot the radial distance over time to
	visualize the complex elliptical shape of the orbit.</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">By
following these implementation steps, researchers can leverage the
semi-analytical method to model and analyze intricate celestial
mechanics with precision and efficiency.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.7
Numerical Implementation</span></h3>
<pre class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><code class="western">import numpy as np</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">from scipy.integrate import odeint</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">import matplotlib.pyplot as plt</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Define constants</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">G = 6.67408e-11  # Gravitational constant (m^3 kg^-1 s^-2)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">M_sun = 1.98910e30  # Mass of Sun (kg)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">def orbital_equations(state, t):</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&quot;&quot;&quot;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">Orbital equations: dX/dt = v, dV/dt = -GM/r³</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&quot;&quot;&quot;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">X, Y, Z, Vx, Vy, Vz = state</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">r = np.sqrt(X**2 + Y**2 + Z**2)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western"># Compute acceleration components</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">ax = -G * M_sun * X / r**3</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">ay = -G * M_sun * Y / r**3</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">az = -G * M_sun * Z / r**3</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">return [Vx, Vy, Vz, ax, ay, az]</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Initial conditions</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">X0, Y0, Z0 = 1.496e11, 0, 0  # Position in meters</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">Vx0, Vy0, Vz0 = 0, 29.78e3, 0  # Velocity in m/s</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">state0 = [X0, Y0, Z0, Vx0, Vy0, Vz0]</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Time array</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">t = np.linspace(0, 10 * 365.25 * 24 * 3600, 10000)  # 10 years</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Solve ODE</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">solution = odeint(orbital_equations, state0, t)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Extract position components</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">X = solution[:, 0]</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">Y = solution[:, 1]</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">Z = solution[:, 2]</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot 3D trajectory</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">fig = plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax = fig.add_subplot(projection='3d')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.plot(X/1e9, Y/1e9, Z/1e9, label='Earth Orbit')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.set_xlabel('X (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.set_ylabel('Y (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.set_zlabel('Z (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.set_title('Earth\'s Orbital Motion around Sun')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span></pre><p style="border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">This
code implements numerical integration using the </span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">odeint</code></span><span style="display: inline-block; border: none; padding: 0cm">
function from SciPy. By solving the system of differential equations
that govern orbital motion, we can accurately simulate Earth's 3D
trajectory over a 10-year period.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
resulting 3D plot visualizes the complex elliptical shape of Earth's
orbit around the Sun. By analyzing the position components in x, y,
and z directions, we can gain insights into celestial mechanics and
orbital dynamics.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.8
Analytical Approach</span></h3>
<pre class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><code class="western">import numpy as np</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">from scipy.integrate import quad</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">import matplotlib.pyplot as plt</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Define constants</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">G = 6.67408e-11  # Gravitational constant (m^3 kg^-1 s^-2)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">M_sun = 1.98910e30  # Mass of Sun (kg)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">def orbital_energy(r):</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&quot;&quot;&quot;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">Orbital energy: E = -GM/r</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&quot;&quot;&quot;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">return -G * M_sun / r</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Radial distance array in meters</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">r = np.linspace(1.0e11, 1.5e11, 1000)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Compute energy at each radial point</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">energy = orbital_energy(r)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot potential energy curve</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(r/1e9, energy, label='Potential Energy')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Radial Distance (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Energy (Joules)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Orbital Potential Energy Curve')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span></pre><p style="border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">This
analytical approach computes the potential energy at each radial
distance using Kepler's equation. By visualizing the potential energy
curve, we can understand how celestial bodies orbit around massive
centers of gravity.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
plot reveals a characteristic parabolic shape that represents the
gravitational potential energy between two objects. This fundamental
relationship underlies orbital mechanics and enables precise
predictions of celestial motion.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.9
Visualization Techniques</span></h3>
<pre class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><code class="western">import numpy as np</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">from scipy.integrate import odeint</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">import matplotlib.pyplot as plt</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Define constants</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">G = 6.67408e-11  # Gravitational constant (m^3 kg^-1 s^-2)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">M_sun = 1.98910e30  # Mass of Sun (kg)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Orbital parameters</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">a = 1.496e11  # Average distance from Sun (meters)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">e = 0.0167  # Eccentricity</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Semi-major axis</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">b = a * np.sqrt(1 - e**2)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">def orbital_equations(state, t):</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&quot;&quot;&quot;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">Orbital equations: dX/dt = vx, dVx/dt = -GM/r³</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&quot;&quot;&quot;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">X, Y, Z, Vx, Vy, Vz = state</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">r = np.sqrt(X**2 + Y**2 + Z**2)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">v = np.sqrt(G * M_sun / r)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western"># Compute acceleration components</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">ax = -G * M_sun * X / r**3</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">ay = -G * M_sun * Y / r**3</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">az = -G * M_sun * Z / r**3</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">return [Vx, Vy, Vz, ax, ay, az]</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Initial conditions</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">state0 = [a, 0, 0, 0, 29.78e3, 0]</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Time array</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">t = np.linspace(0, 10 * 365.25 * 24 * 3600, 10000)  # 10 years</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Solve ODE</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">solution = odeint(orbital_equations, state0, t)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot trajectory</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">X = solution[:, 0]</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">Y = solution[:, 1]</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">Z = solution[:, 2]</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(X/1e9, Y/1e9, label='Earth Orbit')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('X (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Y (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Earth\'s Orbital Motion around Sun')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot 3D trajectory</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">fig = plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax = fig.add_subplot(projection='3d')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.plot(X/1e9, Y/1e9, Z/1e9, label='Orbit')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.set_xlabel('X (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.set_ylabel('Y (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.set_zlabel('Z (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.set_title('Earth\'s Orbital Motion in 3D')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">ax.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot radial distance</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(t/365.25/24/3600, X/1e9, label='Radial Distance')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Time (Years)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Distance from Sun (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Earth\'s Orbital Radius')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot orbital speed</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">v = np.sqrt(G * M_sun / X)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(t/365.25/24/3600, v/1e3, label='Orbital Speed')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Time (Years)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Speed (km/s)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Earth\'s Orbital Velocity')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot orbital energy</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">E = -G * M_sun / X</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(t/365.25/24/3600, E/1e30, label='Orbital Energy')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Time (Years)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Energy (Joules)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Earth\'s Orbital Potential Energy')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot orbital semi-major axis</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(t/365.25/24/3600, X/1e9, label='Semi-major Axis')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Time (Years)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Distance from Sun (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Earth\'s Orbital Semi-major Axis')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Plot orbital eccentricity</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(10,6))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(t/365.25/24/3600, e*np.ones(len(t)), label='Eccentricity')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Time (Years)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Eccentricity')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Earth\'s Orbital Eccentricity (Constant)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span></pre><p style="border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">This
code generates a comprehensive set of visualizations that capture
Earth's orbital dynamics. Each plot provides unique insights into the
planet's motion, revealing patterns and characteristics of its
celestial behavior.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
3D trajectory visualization is particularly striking, demonstrating
Earth's elliptical orbit around the Sun with remarkable detail. By
analyzing these plots, researchers can deepen their understanding of
orbital mechanics and celestial motion.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
radial distance plot shows how Earth's distance from the Sun varies
over time, while the orbital speed graph illustrates how velocity
changes throughout the orbit. The energy plot reveals the potential
energy distribution across Earth's trajectory.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">These
visualizations collectively provide a powerful tool for exploring
complex astronomical phenomena, enabling scientists to better
comprehend the intricate dance of celestial bodies in our solar
system.</span></p>
<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.10
Orbital Parameter Visualization</span></h3>
<pre class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><code class="western">import numpy as np</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">from scipy.integrate import odeint</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">import matplotlib.pyplot as plt</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Define constants</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">G = 6.67408e-11  # Gravitational constant (m^3 kg^-1 s^-2)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">M_sun = 1.98910e30  # Mass of Sun (kg)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Semi-major axis array in meters</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">a = np.linspace(1.0e11, 1.5e11, 1000)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Compute orbital parameters</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">e = 0.0167 * np.ones(len(a))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">T = 365.25 * 24 * 3600 * np.sqrt(a**3 / (G * M_sun))</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">r_min = a * (1 - e)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">r_max = a * (1 + e)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">v_min = np.sqrt(G * M_sun / r_max)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">v_max = np.sqrt(G * M_sun / r_min)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Create plot</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.figure(figsize=(12,10))</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Semi-major axis plot</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.subplot(3, 2, 1)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(a/1e9, label='Semi-major Axis')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Index')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Distance (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Orbital Semi-major Axis')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Eccentricity plot</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.subplot(3, 2, 2)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(e*np.ones(len(a)), label='Eccentricity')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Index')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Eccentricity')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Orbital Eccentricity (Constant)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Period plot</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.subplot(3, 2, 3)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(T/365.25, label='Orbital Period')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Semi-major Axis (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Period (Years)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Kepler\'s Third Law')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Minimum radius plot</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.subplot(3, 2, 4)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(r_min/1e9, label='Minimum Radius')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Index')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Distance (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Perihelion Distance')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Maximum radius plot</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.subplot(3, 2, 5)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(r_max/1e9, label='Maximum Radius')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Index')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Distance (Billion Meters)')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Aphelion Distance')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western"># Velocity range plot</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.subplot(3, 2, 6)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.plot(v_min, v_max, label='Orbital Velocity Range')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.xlabel('Minimum Velocity')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.ylabel('Maximum Velocity')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.title('Orbital Speed Range')</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.legend()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.grid(True)</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.tight_layout()</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">plt.show()</code></span></pre><p style="border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">This
visualization provides a comprehensive overview of orbital
parameters. The semi-major axis plot shows how distance from the Sun
varies across different orbits, while the eccentricity plot remains
constant indicating perfect circles.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
period plot demonstrates Kepler's Third Law, revealing an inverse
square relationship between orbital period and semi-major axis.
Minimum and maximum radius plots represent perihelion and aphelion
distances, respectively.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
velocity range plot illustrates how orbital speeds vary between
minimum and maximum velocities. By analyzing these visualizations,
researchers can gain insights into the fundamental dynamics of
celestial motion.</span></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>
