from huggingface_hub import HfApi
import json
import time

api = HfApi()

TASKS = [
    "text-generation",
    "feature-extraction",
    "sentence-similarity",
    "text-classification",
    "question-answering",
]

results = []

for task in TASKS:
    print(f"collecting: {task}")

    models = api.list_models(
        pipeline_tag=task,
        sort="downloads",
        limit=1000,
        full=True
    )

    for m in models:
        results.append({
            "model_id": m.id,
            "author": m.author,
            "pipeline_tag": m.pipeline_tag,
            "downloads": m.downloads,
            "likes": m.likes,
            "tags": m.tags,
            "last_modified": (
                m.last_modified.isoformat()
                if m.last_modified else None
            ),
            "gated": getattr(m, "gated", None),
        })

    time.sleep(1)

with open("hf_models.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"saved: {len(results)} models")