---
task_categories:
- object-detection
- text-classification
- feature-extraction
language:
- ko
tags:
- homecam
- video
- audio
- npy
size_categories:
- 100B<n<1T
viewer: false 
---

## Dataset Overview

- The dataset is designed to support the development of machine learning models for detecting daily activities, violence, and fall down scenarios from combined audio and video sources.
- The preprocessing pipeline leverages audio feature extraction, human keypoint detection, and relative positional encoding to generate a unified representation for training and inference.
	- Classes:
	    - 0: Daily - Normal indoor activities
	    - 1: Violence - Aggressive behaviors
	    - 2: Fall Down - Sudden falls or collapses
	- Data Format:
	    - Stored as `.npy` files for efficient loading and processing.
	    - Each `.npy` file is a tensor containing concatenated audio and video feature representations for a fixed sequence of frames.
- Data preprocessing code: [GitHub data-preprocessing](https://github.com/silverAvocado/silver-data-processing)

## Dataset Preprocessing Pipeline
![Data Preprocessing](./pics/data-preprocessing.png)
- The dataset preprocessing consists of a multi-step pipeline to extract and align audio features and video keypoints. Below is a detailed explanation of each step:

### Step 1: Audio Processing
1. WAV File Extraction:
	- Audio is extracted from the original video files in WAV format.
2. Frame Splitting:
	- The audio signal is divided into 1/30-second segments to synchronize with video frames.
3.	MFCC Feature Extraction:
	- Mel-Frequency Cepstral Coefficients (MFCC) are computed for each audio segment.
	- Each MFCC output has a shape of 13 x m, where m represents the number of frames in the audio segment.

### Step 2: Video Processing
1.	YOLO Object Detection:
	- Detects up to 3 individuals in each video frame using the YOLO model.
	- Outputs bounding boxes for detected individuals.
2.	MediaPipe Keypoint Extraction:
	- For each detected individual, MediaPipe extracts 33 keypoints, each represented as (x, y, z, visibility), where:
	    - x, y, z : Spatial coordinates.
	    - visibility : Confidence score for the detected keypoint.
3.	Keypoint Filtering:
	- Keypoints 1, 2, and 3 (eyebrow-specific) are excluded.
	- Keypoints are further filtered by visibility threshold(0.5) to ensure reliable data.
    - Visibility property is excluded in further calculations.
4.	Relative Positional Encoding:
	- For the remaining 30 keypoints, relative positions of the 10 most important keypoints are computed.
	- These relative positions are added as additional features to improve context-aware modeling.
5. Feature Dimensionality Adjustment:
	- The output is reshaped to (n, 30*3 + 30, 3), where n is the number of frames.

### Step 3: Audio-Video Feature Concatenation
1. Expansion:
	- Video keypoints are expanded to match the audio feature dimensions, resulting in a tensor of shape (1, 1, 4).
2.	Concatenation:
	- Audio (13) and video (12) features are concatenated along the feature axis.
	- The final representation has a shape of (n, 120, 13+12), where n is the number of frames.

### Data Storage
- The final processed data is saved as `.npy` files, organized into three folders:
	- `0_daily/`: Contains data representing normal daily activities.
	- `1_violence/`: Contains data representing violent scenarios.
	- `2_fall_down/`: Contains data representing falling events.

## Dataset Descriptions

- This dataset provides a comprehensive representation of synchronized audio and video features for real-time activity recognition tasks. 
- The combination of MFCC audio features and MediaPipe keypoints ensures the model can accurately detect and differentiate between the defined activity classes.

- Key Features:
	1.	Multimodal Representation:
	    - Audio and video modalities are fused into a single representation to capture both sound and motion dynamics.
	2.	Efficient Format:
	    - The `.npy` format ensures fast loading and processing, suitable for large-scale training.
	3.	Real-World Applications:
	    - Designed for safety systems, healthcare monitoring, and smart home applications.
        - Adaptation in `SilverAssistant` project: [HuggingFace Silver-Multimodal Model](https://huggingface.co/SilverAvocado/Silver-Multimodal)

- This dataset enables the development of robust multimodal models for detecting critical situations with high accuracy and efficiency.

## Data Sources
- Source 1: [시니어 이상행동 영상 AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=167)
- Source 2: [이상행동 cctv 영상 AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=171)
- Source 3: [멀티모달 영상](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=58)

