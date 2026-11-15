---
license: gemma
library_name: transformers
base_model: google/gemma-3-12b-pt
language:
- en
- ko
- ja
- zh
- es
- ru
- ar
- hi
- id
- ml
- fr
- de
pipeline_tag: image-text-to-text
---

# Gemma3-R1984-12B

# Model Overview
Gemma3-R1984-12B is a robust Agentic AI platform built on Googls’s Gemma-3-12B model. It integrates state-of-the-art deep research via web search with multimodal file processing—including images, videos, and documents—and handles long contexts up to 8,000 tokens. Designed for local deployment on independent servers using NVIDIA L40s GPUs, it provides high security, prevents data leakage, and delivers uncensored responses.

# Key Features
Multimodal Processing:
Supports multiple file types such as images (PNG, JPG, JPEG, GIF, WEBP), videos (MP4), and documents (PDF, CSV, TXT).

Deep Research (Web Search):
Automatically extracts keywords from user queries and utilizes the SERPHouse API to retrieve up to 20 real-time search results. The model incorporates multiple sources by explicitly citing them in the response.

Long Context Handling:
Capable of processing inputs up to 8,000 tokens, ensuring comprehensive analysis of lengthy documents or conversations.

Robust Reasoning:
Employs extended chain-of-thought reasoning for systematic and accurate answer generation.

Secure Local Deployment:
Operates on independent local servers using NVIDIA L40s GPUs to maximize security and prevent information leakage.

**Experience the Power of Gemma3-R1984-12B**

- ✅ **Agentic AI Platform:** An autonomous system designed to make intelligent decisions and act independently.
- ✅ **Reasoning & Uncensored:** Delivers clear, accurate, and unfiltered responses by harnessing advanced reasoning capabilities.
- ✅ **Multimodal & VLM:** Seamlessly processes and interprets multiple input types—text, images, videos—empowering versatile applications.
- ✅ **Deep-Research & RAG:** Integrates state-of-the-art deep research and retrieval-augmented generation to provide comprehensive, real-time insights.

**Cutting-Edge Hardware for Maximum Security**

Gemma3-R1984-12B is engineered to operate on a dedicated **NVIDIA L40s GPU** within an independent local server environment. This robust setup not only guarantees optimal performance and rapid processing but also enhances security by isolating the model from external networks, effectively preventing information leakage. Whether handling sensitive data or complex queries, our platform ensures that your information remains secure and your AI interactions remain uncompromised.



# Use Cases
Fast-response conversational agents

Deep research and retrieval-augmented generation (RAG)

Document comparison and detailed analysis

Visual question answering from images and videos

Complex reasoning and research-based inquiries

# Supported File Formats
Images: PNG, JPG, JPEG, GIF, WEBP

Videos: MP4

Documents: PDF, CSV, TXT

# Model Details
Parameter Count: Approximately 12B parameters (estimated)

Context Window: Up to 8,000 tokens

Hugging Face Model Path: VIDraft/Gemma-3-R1984-12B

License: mit(Agentic AI) / gemma(gemma-3-12B)

# Installation and Setup
## Requirements
Ensure you have Python 3.8 or higher installed. The model relies on several libraries:

PyTorch (with bfloat16 support)

Transformers

Gradio

OpenCV (opencv-python)

Pillow (PIL)

PyPDF2

Pandas

Loguru

Requests


# Install dependencies using pip:

pip install torch transformers gradio opencv-python pillow PyPDF2 pandas loguru requests

# Environment Variables
Set the following environment variables before running the model:

## SERPHOUSE_API_KEY
Your SERPHouse API key for web search functionality.

Example:
export SERPHOUSE_API_KEY="your_api_key_here"

MODEL_ID
(Optional) The model identifier; default is VIDraft/Gemma-3-R1984-12B.

MAX_NUM_IMAGES
(Optional) Maximum number of images allowed per query (default is 5).

# Running the Model
Gemma3-R1984-12B comes with a Gradio-based multimodal chat interface. To run the model locally:

1. Clone the Repository:
Ensure you have the repository containing the model code.

2. Launch the Application:
Execute the main Python file:


python your_filename.py

This will start a local Gradio interface. Open the provided URL in your browser to interact with the model.

# Example Code: Server and Client Request
## Server Example
You can deploy the model server locally using the provided Gradio code. Make sure your server is accessible at your designated URL.

## Client Request Example
Below is an example of how to interact with the model using an HTTP API call:

```py

import requests
import json

# Replace with your server URL and token
url = "http://<your-server-url>:8000/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your_token_here"
}

# Construct the message payload
messages = [
    {"role": "system", "content": "You are a powerful AI assistant."},
    {"role": "user", "content": "Compare the contents of two PDF files."}
]

data = {
    "model": "VIDraft/Gemma-3-R1984-12B",
    "messages": messages,
    "temperature": 0.15
}

# Send the POST request to the server
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response from the model
print(response.json())
```

**Important Deployment Notice:**

For optimal performance, it is highly recommended to clone the repository using the following command. This model is designed to run on a server equipped with at least an NVIDIA A100 GPU. The minimum VRAM requirement is 53GB, and VRAM usage may temporarily peak at approximately 82GB during processing.

```bash
git clone https://huggingface.co/spaces/VIDraft/Gemma-3-R1984-12B
