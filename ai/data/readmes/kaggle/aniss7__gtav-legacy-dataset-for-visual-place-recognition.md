# GTA V Legacy Dataset for Visual Place Recognition

Images from Grand Theft Auto V Legacy for visual place recognition (GTAV-VPR)

The images of this dataset have been captured from the Legacy version of GTA, for the more detailed but heavier Enhanced version, please refer to [GTAV Enhanced Dataset for Visual Place Recognition](https://www.kaggle.com/datasets/reiper/gtav-enhanced-dataset-for-visual-place-recognition)
# GTA V Legacy Dataset for Visual Place Recognition (GTAV-VPR)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F25419313%2Fb027350b2c70bfa4cae99bc070860204%2F0.jpg?generation=1764527182679271&alt=media)
This dataset is based on the original _[G2D: from GTA to Data](https://sites.google.com/view/g2d-software/home)_ dataset made on the legacy version of GTA V by [Anh-Dzung Doan](https://dzungdoan6.github.io/), Abdul Mohsi Jawaid, [Thanh-Toan Do](https://sites.google.com/view/thanhtoando/home), and [Tat-Jun Chin](https://cs.adelaide.edu.au/~tjchin/). For more technical details about their work, please refer to their [paper](https://arxiv.org/pdf/1806.07381).

The G2D tool creates a camera that follows a defined path and captures screenshots. This project contains the images and camera trajectories captured during the process. The tool was run over three different cycles in the Little Seoul area of GTA V.

This dataset contains the following:
1. Legacy Dataset: The original dataset made on the legacy version of GTA V.

The dataset was created on the legacy version of GTA V with the following game settings:
- Time: Daytime (12:00 PM)
- Weather: Clear
- Traffic Density: 0.0
- Pedestrian Density: 0.0

Images were captured under three different weather conditions:
- Clear and Rainy
- Day and Night
- Pedestrian Density: 0.0 and 1.0
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F25419313%2F9ad0549eca4609d638eca49c97d98d46%2F0.jpg?generation=1764527228131234&alt=media)

The dataset is organized as follows:
```
/Legacy/
    /images/
        /Area/
            /[TIME]_[WEATHER]_[PEDESTRIAN_DENSITY]/
                0.png
                1.png
                ...
            6dpose_list.txt
    /trajectories/
        /Area/
            trajectory.txt
    settings.xml
```

6dpose_list.txt contains the 6DOF camera poses for each image in the corresponding folder. The format of each line is as follows:
```image_filename tx ty tz qx qy qz qw```.

For more information about the trajectory folder, please refer to the original G2D repository.

Because G2D uses a free camera, we were unable to vary the car density settings without cars entering the camera's field of view. Additionally, even with the pedestrian density set to 1.0, very few pedestrians appear. This is because pedestrians are mainly loaded around the player, who remains stationary during the capture process.

# Mods and Tools Used
- [G2D: from GTA to Data](https://github.com/dzungdoan6/G2D/tree/master)
- [Script Hook V](http://www.dev-c.com/gtav/scripthookv/)

# Capture Environment
- Legacy Version:
    - Computer Specifications:
        - GPU : NVIDIA GeForce GTX 960
        - CPU : Intel Core i5-4600 CPU @ 3.50GHz
    - Game Settings:
        - Version : 1.0.3586.0
        - Resolution: 1920x1080

Full game settings can be found in the settings.xml file.

# Authors
- [Pierre Chhieng](https://www.kaggle.com/reiper)
- [Aniss Outaleb](https://www.kaggle.com/aniss7)

# License
The _GTA V Legacy Dataset for Visual Place Recognition_ and _G2D_ software are only for research and education purposes, any commercial uses are strictly prohibited. 

As a courtesy towards Take-Two Interactive and Rockstar Games, please purchase Grand Theft Auto V, if you use the software and data.

출처: Kaggle (aniss7/gtav-legacy-dataset-for-visual-place-recognition)
태그: video games, image, image classification, synthetic
라이선스: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
수정일: 2025-12-01T10:28:31.543Z
