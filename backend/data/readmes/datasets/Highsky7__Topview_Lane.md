---
license: mit
size_categories:
- 1K<n<10K
task_categories:
- image-segmentation
language:
- en
- ko
pretty_name: BevLane
tags:
- autonomous
- robot
- selfdriving
- lanesegmentation
- bev
---
# Dataset Card for BevLane

## Dataset Details

### Dataset Description

BevLane is a dataset for lane segmentation from a Bird's-Eye-View (BEV) perspective. It consists of top-down transformed images of road scenes and their corresponding pixel-level lane annotations. This dataset is designed to facilitate the development and evaluation of lane detection and segmentation algorithms, which are crucial components for autonomous driving systems and robotics navigation. The BEV perspective simplifies the lane detection problem by removing perspective distortion, making it easier to model lane geometry accurately.

- **Curated by:** [Highsky7](https://huggingface.co/Highsky7)
- **Language(s) (NLP):** English, Korean
- **License:** MIT

### Dataset Sources [optional]

- **Repository:** [https://huggingface.co/datasets/Highsky7/Topview_Lane](https://huggingface.co/datasets/Highsky7/Topview_Lane)
- **Demo:** [https://github.com/Highsky7/YOLOTL](https://github.com/Highsky7/YOLOTL)

## Uses

### Direct Use

This dataset is intended for training and evaluating models for semantic segmentation, specifically for lane detection in a BEV space. It can be directly used for:
- Training deep learning models for lane segmentation.
- Benchmarking the performance of different lane detection algorithms.
- Research in autonomous driving, particularly perception and localization tasks.

### Out-of-Scope Use

This dataset is not intended for direct use in production-level, safety-critical systems without extensive further validation and testing. The models trained on this dataset may not generalize to all driving scenarios, weather conditions, or geographic locations. Using this dataset for any application other than its intended purpose (e.g., object detection, scene classification) is out-of-scope.

## Dataset Structure

The dataset is composed of image files and their corresponding segmentation masks. A typical data point consists of an `image` and its `mask`.

- `image`: A PNG/JPG file of the road scene transformed into a Bird's-Eye-View.
- `mask`: A single-channel PNG file where each pixel value corresponds to a class label (e.g., 0 for background, 1 for lane).

The data is likely split into `train`, `validation`, and `test` sets to facilitate standard model development workflows.

## Dataset Creation

### Curation Rationale

The primary motivation for creating BevLane was to provide the research community with a high-quality, publicly available dataset for BEV lane segmentation. While forward-facing camera datasets are common, BEV datasets offer a unique advantage by presenting lane information in a metrically accurate top-down view, which is highly beneficial for path planning and control modules in self-driving vehicles.

### Source Data

#### Data Collection and Processing

The source data was likely collected from a forward-facing camera mounted on a vehicle. The video frames were then processed using an Inverse Perspective Mapping (IPM) technique to transform them from the perspective view to the BEV. This process requires camera calibration parameters (intrinsic and extrinsic) to be known.

#### Who are the source data producers?

The data was collected and processed by the dataset curator, Highsky7.

### Annotations

#### Annotation process

The lane markings in the BEV images were manually or semi-automatically annotated with roboflow. Annotators were likely instructed to draw precise pixel-level masks for all visible lane lines. An annotation tool like Labelbox, CVAT, or a custom-built tool might have been used for this process. The annotations were then validated to ensure quality and consistency.

#### Who are the annotators?

The annotations were created by Highsky7 and roboflow auto labeling tool.

#### Personal and Sensitive Information

The dataset transformation to a BEV significantly reduces the likelihood of containing personally identifiable information (PII) such as faces or license plates, as these are typically not visible from a top-down perspective. However, users are advised to verify this for their specific use case.

## Bias, Risks, and Limitations

The dataset may contain biases inherent to the data collection process. These could include:
- **Geographic Bias:** The data might have been collected in a specific city or country, meaning it may not represent road markings, driving conventions, or road conditions from other parts of the world.
- **Environmental Bias:** The data was likely collected under specific weather and lighting conditions (e.g., clear, sunny days). Models trained on this data may not perform well in adverse conditions like rain, snow, fog, or at night.
- **Hardware Bias:** The data is specific to the sensor suite (ABKO APC 850 webcam) used for collection.

### Recommendations

Users of this dataset should be aware of its limitations. To build a robust system, it is recommended to:
- Perform extensive testing and validation on a diverse set of real-world data.
- Employ data augmentation techniques to improve model generalization.
- Consider fine-tuning models on data from the target domain if it differs significantly from the source domain of this dataset.

## Citation

If you use this dataset in your research, please consider citing it.

**BibTeX:**

@misc{highsky7_2024_bevlane,
  author = {Highsky7},
  title = {BevLane: A Bird's-Eye-View Lane Segmentation Dataset},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{[https://huggingface.co/datasets/Highsky7/Topview_Lane](https://huggingface.co/datasets/Highsky7/Topview_Lane)}}
}

**APA:**

Highsky7. (2024). BevLane: A Bird's-Eye-View Lane Segmentation Dataset. Hugging Face. Retrieved from https://huggingface.co/datasets/Highsky7/Topview_Lane

## Glossary

BEV (Bird's-Eye-View): A top-down view of a scene, as if viewed from directly above.

IPM (Inverse Perspective Mapping): A mathematical transformation used to convert an image from a perspective view to a top-down (BEV) view.

Lane Segmentation: The task of identifying and classifying pixels in an image that belong to lane markings.

## Dataset Card Authors

This dataset card was created by Highsky7.

## Dataset Card Contact

For any questions or feedback regarding this dataset, please contact Highsky7 on the Hugging Face platform or send an email to albert31115@gmail.com