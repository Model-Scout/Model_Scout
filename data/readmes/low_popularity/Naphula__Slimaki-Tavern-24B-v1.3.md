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
base_model:
- DarkArtsForge/Morax-24B-v2
- MuXodious/Maginum-Cydoms-24B-absolute-heresy
- Naphula/Slimaki-24B-v1.2
library_name: transformers
tags:
- mergekit
- merge
- multi-step_merge
- mistral
- Mistral-Small
- Magistral-Small
- 24B
- multi_fusion
- arcee_fusion
- karcher
- sce
- della
- model_stock
- python
- roleplay
- role play
- rp
- erp
- creative writing
- storytelling
- conversational
- cosmic chat
- science fiction
- horror
- romance
- story generation
- vivid prose
- swearing
- abliterated
- heretic
- uncensored
- kobold
- sillytavern
widget:
  - text: "Ślimaki Tavern 24B v1.3"
    output:
      url: https://cdn-uploads.huggingface.co/production/uploads/6a3cc6bb193d1eead33b8629/O9i6ltb8wMZi37YAjvcmE.png

---
> [!CAUTION]
> <span style="color:red; font-weight:bold">⚠️ Warning:</span> This model can produce narratives and RP that contain violent and graphic erotic content. Adjust your system prompt accordingly, and use **Mistral Tekken** or **ChatML** chat template.
>

# 🐌 Ślimaki Tavern 24B v1.3

![Slimaki_Tavern](https://cdn-uploads.huggingface.co/production/uploads/6a3cc6bb193d1eead33b8629/O9i6ltb8wMZi37YAjvcmE.png)

This is an **uncensored** merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit). It's designed for roleplay use although you may have to experiment with different sampler settings.

## Merge Details
### Merge Method

This model was merged in 2 stages using the [`multi_fusion`](https://huggingface.co/Naphula/Slimaki-Tavern-24B-v1.3/blob/main/multi_fusion.py) merge method.

This method extends upon the `arcee_fusion` method by offering alternate importance metrics, inspired from other methods.

**Papers:**
- [`arcee_fusion`](https://www.arcee.ai/blog/meet-mergekit-v0-1-arcee-fusion-expanded-model-support-multi-gpu-acceleration)
- [`della`](https://arxiv.org/abs/2406.11617)
- [`model_stock`](https://arxiv.org/abs/2403.19522)
- [`sce`](https://arxiv.org/abs/2408.07990)
- [`karcher`](https://arxiv.org/abs/2603.04972)

The chosen approach for this merge was to replace kl_div (from `arcee_fusion`) with delta_mag (from `generalized_task_arithmetic`) and cosine_sim (from `model_stock`).

### Models Merged

The following models were included in the merge:
- [DarkArtsForge/Morax-24B-v2](https://huggingface.co/DarkArtsForge/Morax-24B-v2)
- [MuXodious/Maginum-Cydoms-24B-absolute-heresy](https://huggingface.co/MuXodious/Maginum-Cydoms-24B-absolute-heresy)
- [Naphula/Slimaki-24B-v1.2](https://huggingface.co/Naphula/Slimaki-24B-v1.2)

### Configuration

The following YAML configurations were used to produce this model:

#### Stage 1
```yaml
architecture: MistralForCausalLM
base_model: B:\24B\MuXodious--Maginum-Cydoms-24B-absolute-heresy
models:
  - model: B:\24B\MuXodious--Maginum-Cydoms-24B-absolute-heresy
  - model: B:\24B\DarkArtsForge--Morax-24B-v2
merge_method: multi_fusion # v1
parameters:  
  tukey_fence: 1.5
  importance_metric: "delta_mag" # kl_div, delta_mag, cosine_sim, fisher_grad, topk_var
dtype: float32
out_dtype: bfloat16
tokenizer:
  source: union
chat_template: auto
name: 👹 Morax Cydoms 24B
```

#### Stage 2
```yaml
architecture: MistralForCausalLM
base_model: B:\24B\Morax-Cydoms-24B
models:
  - model: B:\24B\Morax-Cydoms-24B
  - model: B:\24B\Naphula--Slimaki-24B-v1.2
merge_method: multi_fusion # v1
parameters:  
  tukey_fence: 1.5
  importance_metric: "cosine_sim" # kl_div, delta_mag, cosine_sim, fisher_grad, topk_var
dtype: float32
out_dtype: bfloat16
tokenizer:
  source: union
chat_template: auto
name: 🐌 Ślimaki Tavern 24B v1.3
```

---

## 🐍 Python Notes

I have expanded the `arcee_fusion` script into a custom `multi_fusion` with various options.

<details>

## Comparison of the 4 Importance Metrics

| Metric | Formula | Characteristics | Use Case |
|--------|---------|-----------------|----------|
| **kl_div** | `diff * KL_div(softmax(params), softmax(base))` | Combines magnitude with distributional divergence | When parameter direction matters probabilistically |
| **delta_mag** | `abs(params - base_params)` | Pure magnitude of parameter differences | Simple, widely used (TIES/DARE/DELLA) |
| **cosine_sim** | `abs(delta) * (1 + abs(cosine_sim(delta, base)))` | Magnitude weighted by alignment with base | When preserving base-aligned changes is important |
| **fisher_grad** | `variance(delta) + eps` | Variance along last dimension only | When parameter variability indicates importance |

### Detailed Analysis

**kl_div** computes the KL divergence between softmax distributions, then multiplies by the absolute difference <cite repo="arcee-ai/mergekit" path="docs/merge_methods.md" start="357-369" />. This captures both how much parameters changed and how much their output distributions diverged.

**delta_mag** is the simplest metric - just the absolute difference between parameters <cite repo="arcee-ai/mergekit" path="docs/merge_methods.md" start="153-170" />. It's the standard approach used by TIES, DARE, and DELLA methods.

**cosine_sim** computes cosine similarity between the delta and base parameters, then uses it to weight the magnitude: `importance = delta.abs() * (1 + cosine_sim.abs())` <cite repo="arcee-ai/mergekit" path="docs/merge_methods.md" start="320-336" />. This prioritizes changes that are aligned with the base model's direction in parameter space.

**fisher_grad** uses variance along the last dimension as a proxy for Fisher information <cite repo="arcee-ai/mergekit" path="docs/merge_methods.md" start="257-279" />. The current implementation uses variance directly (SCE-style) rather than combining it with magnitude.

## Notes

- The `fisher_grad` metric uses variance directly rather than variance * magnitude (commented out in the code), which follows the SCE approach.

</details>

The fisher_grad section is incomplete and for now uses SCE variance (select_topK) instead of Karcher metrics.

Prototype script below. To use this custom method, add this to `registry.py`.

```py
from mergekit.merge_methods.arcee_fusion import ArceeFusionMerge
from mergekit.merge_methods.multi_fusion import MultiFusionMerge

STATIC_MERGE_METHODS: List[MergeMethod] = [
    LinearMerge(),
    SlerpMerge(),
    NuSlerpMerge(),
    PassthroughMerge(),
    ModelStockMerge(),
    ArceeFusionMerge(),
    MultiFusionMerge(),
    KarcherMerge(),
```

You then can experiment with different importance metrics and tukey_fence values (lower = more donor influence, 1.5 = ~12.5%, 0.75 = ~25%, etc). `kl_div` should be identical to `arcee_fusion`.

<details>

`multi_fusion.py`
```py
# Copyright (C) 2025 Arcee AI
# SPDX-License-Identifier: LGPL-3.0-only  
  
from typing import Any, Dict, List, Optional  
  
import torch  
import torch.nn.functional as F  
from typing_extensions import override  
  
from mergekit.architecture import WeightInfo  
from mergekit.common import ModelReference  
from mergekit.graph import Task  
from mergekit.merge_methods.base import (  
    ConfigParameterDef,  
    MergeMethod,  
    MergeTensorInput,  
)  
from mergekit.merge_methods.rectify_embed import rectify_embed_sizes  
  
  
class DynamicThresholdFusion:  
    def approximate_quantiles(self, tensor, q):  
        # Flatten the tensor  
        flat_tensor = tensor.view(-1)  
  
        # If tensor is too large, sample it  
        if flat_tensor.numel() > 1e6:  
            flat_tensor = flat_tensor[torch.randperm(flat_tensor.numel())[:1000000]]  
  
        # Sort the (possibly sampled) tensor  
        sorted_tensor, _ = torch.sort(flat_tensor)  
  
        # Compute quantile indices  
        quantile_indices = (q * (sorted_tensor.numel() - 1)).long()  
  
        # Return quantiles  
        return sorted_tensor[quantile_indices]  
  
    def calculate_dynamic_threshold(self, importance_scores, tukey_fence=1.5):  
        # Approximate median and quantiles  
        median = self.approximate_quantiles(importance_scores, torch.tensor([0.5]))[0]  
        q1, q3 = self.approximate_quantiles(  
            importance_scores, torch.tensor([0.25, 0.75])  
        )  
  
        # Calculate IQR  
        iqr = q3 - q1  
  
        # Set threshold as median + tukey_fence * IQR  
        dynamic_threshold = median + tukey_fence * iqr  
  
        return dynamic_threshold
  
    def compute_fusion_mask(self, importance_scores, tukey_fence=1.5):  
        threshold = self.calculate_dynamic_threshold(importance_scores, tukey_fence)  
        fusion_mask = (importance_scores >= threshold).float()  
        return fusion_mask, threshold 
  
  
class MultiFusionMergeTask(Task[torch.Tensor]):  
    gather_tensors: MergeTensorInput  
    base_model: ModelReference  
    weight_info: WeightInfo  
    importance_metric: str = "delta_mag"  
    tukey_fence: float = 1.5
  
    def uses_accelerator(self) -> bool:  
        return True  
  
    def arguments(self) -> Dict[str, Task]:  
        return {"tensors": self.gather_tensors}  
  
    def execute(self, tensors: Dict[ModelReference, torch.Tensor]) -> torch.Tensor:  
        if len(tensors) == 1:  
            return list(tensors.values())[0]  
        elif len(tensors) != 2:  
            raise RuntimeError("MutliFusion merge expects exactly two models")  
        elif self.base_model not in tensors:  
            raise RuntimeError("Base model not in input tensors")  
  
        [a, b] = list(tensors.items())  
        if a[0] != self.base_model:  
            [a, b] = [b, a]  
        prepped_tensors = [a[1], b[1]]  
  
        rectify_embed_sizes(self.weight_info, prepped_tensors)  
  
        importance_scores = self._compute_importance(  
            prepped_tensors[1], prepped_tensors[0]  
        )  
        dynamic_threshold_fusion = DynamicThresholdFusion()  
        fusion_mask, _threshold = dynamic_threshold_fusion.compute_fusion_mask(  
            importance_scores, tukey_fence=self.tukey_fence   
        )  
  
        delta = prepped_tensors[1] - prepped_tensors[0]  
        masked_delta = delta * fusion_mask  
        fused = prepped_tensors[0] + masked_delta  
  
        return fused  
  
    def _compute_importance(  
        self, params: torch.Tensor, base_params: torch.Tensor, eps: float = 1e-8  
    ) -> torch.Tensor:  
        if self.importance_metric == "kl_div":  
            return self._compute_kl_div_importance(params, base_params, eps)  
        elif self.importance_metric == "delta_mag":  
            return self._compute_delta_mag_importance(params, base_params)  
        elif self.importance_metric == "cosine_sim":  
            return self._compute_cosine_sim_importance(params, base_params)  
        elif self.importance_metric == "fisher_grad":  
            return self._compute_fisher_grad_importance(params, base_params)  
        else:  
            raise ValueError(f"Unknown importance metric: {self.importance_metric}")  
  
    def _compute_kl_div_importance(  
        self, params: torch.Tensor, base_params: torch.Tensor, eps: float = 1e-8  
    ) -> torch.Tensor:  
        diff = (params - base_params).abs()  
        p = F.softmax(params, dim=-1) + eps  
        q = F.softmax(base_params, dim=-1) + eps  
        kl_div = torch.sum(p * torch.log(p / q), dim=-1)  
        return diff * kl_div.unsqueeze(-1)  
  
    def _compute_delta_mag_importance(  
        self, params: torch.Tensor, base_params: torch.Tensor  
    ) -> torch.Tensor:  
        # Magnitude of delta - used by TIES/DARE/DELLA  
        delta = params - base_params  
        return delta.abs()  
  
    def _compute_cosine_sim_importance(  
        self, params: torch.Tensor, base_params: torch.Tensor  
    ) -> torch.Tensor:  
        # Cosine similarity based - inspired by Model Stock  
        delta = params - base_params  
        delta_flat = delta.view(-1)  
        base_flat = base_params.view(-1)  
          
        # Compute cosine similarity between delta and base  
        dot_product = torch.dot(delta_flat, base_flat)  
        norm_delta = torch.norm(delta_flat)  
        norm_base = torch.norm(base_flat)  
          
        # Avoid division by zero  
        if norm_delta == 0 or norm_base == 0:  
            return torch.zeros_like(delta)  
          
        cosine_sim = dot_product / (norm_delta * norm_base)  
        # Convert similarity to importance (higher similarity = more important)  
        importance = delta.abs() * (1 + cosine_sim.abs())  
        return importance.view_as(delta)  
  
    def _compute_fisher_grad_importance(  
        self, params: torch.Tensor, base_params: torch.Tensor  
    ) -> torch.Tensor:  
        # Fisher/gradient-based importance - inspired by Karcher/Fisher information  
        # Since we don't have access to gradients/data, we use a proxy based on  
        # the magnitude and variance of the delta  
        delta = params - base_params  
          
        # Compute variance along the last dimension as a proxy for Fisher information  
        if delta.dim() > 1:  
            variance = torch.var(delta, dim=-1, keepdim=True)  
        else:  
            variance = delta.var().unsqueeze(0)  
          
        ## # Importance combines magnitude and variance  
        ## importance = delta.abs() * (variance + 1e-8)  
        ## return importance  
        
        # Use variance directly as importance (SCE-style) rather than variance * magnitude  
        importance = variance + 1e-8  
        return importance
  
class MultiFusionMerge(MergeMethod):  
    def name(self) -> str:  
        return "multi_fusion"  
  
    @override  
    def pretty_name(self) -> Optional[str]:  
        return "Multi Fusion"  
  
    @override  
    def reference_url(self) -> Optional[str]:  
        return "https://huggingface.co/Naphula/Slimaki-Tavern-24B-v1.3"  
  
    def parameters(self) -> List[ConfigParameterDef]:  
        return [  
            ConfigParameterDef(  
                name="importance_metric",  
                required=False,  
                default_value="delta_mag",  
            ),  
            ConfigParameterDef(  
                name="tukey_fence",  
                required=False,  
                default_value=1.5,  
            )  
        ] 
  
    def make_task(  
        self,  
        output_weight: WeightInfo,  
        tensors: MergeTensorInput,  
        base_model: Optional[ModelReference],  
        parameters: Dict[str, Any],  
        **kwargs,  
    ) -> Task[torch.Tensor]:  
        return MultiFusionMergeTask(  
            gather_tensors=tensors,  
            weight_info=output_weight,  
            base_model=base_model,  
            importance_metric=parameters["importance_metric"],  
            tukey_fence=parameters["tukey_fence"]
        )
```

</details>