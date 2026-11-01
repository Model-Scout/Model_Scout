---
license: mit
task_categories:
- question-answering
- image-to-text
- visual-question-answering
language:
- en
- vi
- fr
- de
- zh
- ko
- ja
size_categories:
- 100K<n<1M
tags:
- medical
- multilingual
- fairness
- pathology
- medical-imaging
---

# Multilingual-Pathology-Fairness

A comprehensive multilingual medical pathology dataset with fairness attributes and high-quality medical images for evaluating bias in medical AI systems across different languages and patient demographics.

## Dataset Description

This dataset contains **949,872 medical pathology cases** with:
- Questions and answers in **7 languages**
- High-quality **pathology images** (0 per sample)
- **Fairness attributes** injected into Q1 questions across all languages
- Detailed **bounding box annotations**

### Supported Languages

- **English**
- **Vietnamese**
- **French**
- **German**
- **Mandarin Chinese**
- **Korean**
- **Japanese**

### Medical Images

This dataset includes **0 types of images** per sample:


## Key Features

✅ **Multilingual Support**: Questions available in 7 languages  
✅ **Fairness Evaluation**: Q1 questions include fairness attributes for bias evaluation  
✅ **Medical Images**: High-quality pathology images with annotations  
✅ **Bounding Boxes**: Precise annotations for regions of interest  
✅ **Comprehensive Metadata**: Patient information, slide details, and clinical notes

## Dataset Structure

### Data Fields

**Total: 21 fields**

#### Core Identification
- `No.`: Sample number
- `Patient ID`: Patient identifier
- `Slide`: Slide identifier
- `Start date`: Case start date
- `Doctor`: Attending physician
- `Status`: Case status

#### Medical Images

- `Bbox coordinates normalized (X, Y, W, H)`: Normalized bounding box coordinates

#### Questions and Answers

**English (with Fairness Attributes)**
- `Q1`: Question 1 (fairness attributes injected)
- `Q2`, `Q3`, `Q4`: Questions 2-4
- `A1`, `A2`, `A3`, `A4`: Corresponding answers

**Multilingual Q1 (All with Fairness Attributes)**
- `Q1_vn`: Question 1 in Vietnamese (with fairness attributes)
- `Q1_fr`: Question 1 in French (with fairness attributes)
- `Q1_de`: Question 1 in German (with fairness attributes)
- `Q1_mandarin`: Question 1 in Mandarin Chinese (with fairness attributes)
- `Q1_korean`: Question 1 in Korean (with fairness attributes)
- `Q1_japanese`: Question 1 in Japanese (with fairness attributes)


**Additional Multilingual Questions**
- Q2, Q3, Q4 and their answers available in all 7 languages
- Sub-questions (Q2.1-Q2.3, Q3.1-Q3.3) also multilingual

### Fairness Attributes

All Q1 questions across all languages have been injected with fairness attributes including:
- **Demographic**: Age, gender, race/ethnicity
- **Geographic**: Region, urban/rural, healthcare access
- **Socioeconomic**: Income, education, insurance type
- **Cultural**: Cultural background, religious affiliation
- **Linguistic**: Language variety, accent, dialect

## Dataset Statistics

- 📊 **Total examples**: 949,872
- 🌍 **Languages**: 7
- 🖼️ **Images per sample**: 0
- 📋 **Total features**: 21
- ❓ **Questions per sample**: 4 main (Q1-Q4) + sub-questions

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load the complete dataset
dataset = load_dataset("JiayiHe/Multilingual-Pathology-Fairness")

# Access first example
example = dataset['train'][0]

# View English Q1 with fairness attributes
print(example['Q1'])

# View Vietnamese Q1 with fairness attributes
print(example['Q1_vn'])

# Display the pathology image
example['image'].show()

# Display image with bounding boxes
if 'image_with_bboxes' in example:
    example['image_with_bboxes'].show()
```

### Accessing Images

```python
from PIL import Image

# Get an example
example = dataset['train'][0]

# Access original image
original_img = example['image']
print(f"Image size: {original_img.size}")

# Access annotated image
if 'image_with_bboxes' in example:
    annotated_img = example['image_with_bboxes']
    annotated_img.show()

# Save image
original_img.save("pathology_sample.png")
```

### Multilingual Question Access

```python
# Define language fields
languages = {
    'English': 'Q1',
    'Vietnamese': 'Q1_vn',
    'French': 'Q1_fr',
    'German': 'Q1_de',
    'Mandarin': 'Q1_mandarin',
    'Korean': 'Q1_korean',
    'Japanese': 'Q1_japanese'
}

# Access questions in different languages
example = dataset['train'][0]
for lang_name, field in languages.items():
    if field in example:
        print(f"{lang_name}: {example[field][:100]}...")
```

### Fairness Evaluation Across Languages

```python
# Evaluate model performance across languages
from datasets import load_dataset

dataset = load_dataset("JiayiHe/Multilingual-Pathology-Fairness")

results = {}

for lang_name, q_field in languages.items():
    print(f"Evaluating on {lang_name}...")
    
    lang_results = []
    for example in dataset['train']:
        # Get question and image
        question = example[q_field]
        image = example['image']
        
        # Run your model
        # prediction = your_model(image, question)
        # lang_results.append(evaluate(prediction, example['A1']))
    
    results[lang_name] = lang_results

# Compare fairness across languages
print("Cross-lingual fairness comparison:")
for lang, scores in results.items():
    print(f"  {lang}: {sum(scores)/len(scores):.2%}")
```

### Working with Bounding Boxes

```python
import ast

example = dataset['train'][0]

# Parse bounding box coordinates
bbox_str = example['Bbox coordinates normalized (X, Y, W, H)']
bbox = ast.literal_eval(bbox_str)  # Convert string to tuple/list

x, y, w, h = bbox
print(f"Bounding box: X={x}, Y={y}, Width={w}, Height={h}")

# Draw bounding box on image
from PIL import ImageDraw

img = example['image'].copy()
draw = ImageDraw.Draw(img)

# Convert normalized coordinates to pixels
img_width, img_height = img.size
x_pixel = int(x * img_width)
y_pixel = int(y * img_height)
w_pixel = int(w * img_width)
h_pixel = int(h * img_height)

# Draw rectangle
draw.rectangle(
    [x_pixel, y_pixel, x_pixel + w_pixel, y_pixel + h_pixel],
    outline="red",
    width=3
)
img.show()
```

## Dataset Creation

This dataset was created through:
1. Collection of medical pathology images with expert annotations
2. Question generation in multiple languages
3. Fairness attribute injection into Q1 questions
4. Bounding box annotation for regions of interest
5. Multi-stage quality verification

## Intended Use

### Primary Applications
- 🔬 Medical visual question answering
- ⚖️ Fairness and bias evaluation in medical AI
- 🌍 Multilingual medical AI research
- 🖼️ Pathology image understanding
- 📊 Cross-lingual transfer learning

### Research Areas
- Bias detection in medical diagnostics
- Language-specific performance analysis
- Visual reasoning in pathology
- Fairness-aware model development

## Limitations

- Fairness attributes only injected into Q1 questions
- Q2, Q3, Q4 remain in original form
- Image quality may vary across samples
- Translation quality varies by language
- Dataset size may be limited for some applications

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{multilingual_pathology_fairness,
  title={Multilingual-Pathology-Fairness},
  author={Your Name},
  year={2025},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/datasets/JiayiHe/Multilingual-Pathology-Fairness}}
}
```

## License

MIT License

## Ethical Considerations

This dataset contains medical images and patient information. Please ensure:
- Proper anonymization of patient data
- Compliance with medical data regulations (HIPAA, GDPR, etc.)
- Responsible use in research and clinical applications
- Awareness of potential biases in medical AI systems

## Contact

For questions, issues, or contributions:
- 📧 Open an issue on the dataset repository
- 💬 Contact the dataset maintainer
- 🔗 Visit: https://huggingface.co/datasets/JiayiHe/Multilingual-Pathology-Fairness

## Acknowledgments

Thanks to the medical professionals, linguists, and data annotators who contributed to creating this comprehensive multilingual pathology dataset.
