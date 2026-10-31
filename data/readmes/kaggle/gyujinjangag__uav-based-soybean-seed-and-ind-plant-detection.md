# UAV-Based Soybean Seed and Ind-Plant Detection



Overview
This dataset provides UAV-acquired RGB imagery of soybean (Glycine max L.) plants at the reproductive stage, annotated at two levels: seed-level point annotations and individual plant-level bounding boxes. It was developed to support individual plant-level (IPL) soybean phenotyping and yield mapping research.

Image Acquisition
Images were captured using a DJI Mavic 3 equipped with dual RGB cameras — a wide-angle camera (4/3" CMOS, 24 mm equivalent focal length) and a telephoto camera (1/2" CMOS, 162 mm equivalent focal length), both at 4000×3000 pixel resolution. Unlike most UAV phenotyping datasets that rely on wide-angle imagery, this dataset was collected primarily with the telephoto camera, flown at an altitude of approximately 5–6 m with the gimbal tilted at 50°, to resolve individual soybean seeds with sufficient visual clarity for reliable annotation and detection — a level of detail wide-angle imagery cannot capture.

Images were acquired under two lighting conditions to account for row orientation (Korean soybean fields are typically oriented west–east): front-lit (camera facing north) and backlit (camera facing south), both perpendicular to the crop rows.

Study Sites
Data were collected in 2025 at two locations in the Republic of Korea: Seoul National University Farm, Suwon, A commercial farm, Goisan

Annotations
651 images, manually annotated using Labelme
5,553 bounding boxes — individual plant-level annotations
503,363 point annotations — individual seed-level annotations

Intended Use
This dataset supports research in UAV-based crop phenotyping, object detection/counting, multi-task deep learning (joint point + box detection), and individual plant-level yield estimation in precision agriculture and plant breeding applications.

출처: Kaggle (gyujinjangag/uav-based-soybean-seed-and-ind-plant-detection)
태그: 
라이선스: CC BY-SA 4.0
수정일: 2026-10-02T04:06:10.063Z
