# VIP CUP 2020



## IEEE Video and Image Processing Cup (VIP Cup) 

The Video and Image Processing Cup (VIP Cup) competition encourages teams of students work together to solve real-world problems using video and image processing methods and techniques. Three final teams are chosen to present their work during ICIP to compete for the US$5,000 grand prize!

Technical Committees interested in submitting a call for proposal for upcoming VIP Cup competitions, please visit the Technical Committees page for more information.

### Introduction

With the increasing growth of urbanization, it introduces traffic jams and congestion in several locations around the city. Apart from accidents, that may result in drastic average travel time increase from point A to point B in a city. Especially junctions are critical since delays and accidents tend to be concentrated at these places. Under these circumstances, intelligent traffic systems are unavoidable that are capable of tasks such as vehicle detection, tracking, violation detection and congestion control.

The 2020 VIP-cup challenge focuses on fisheye cameras mounted into street lamps at junctions and vehicle detection and tracking to be used for a junction management system to optimize the flow of traffic and synchronize with other junctions to obtain bottleneck performances throughout the city. Fisheye cameras are used since they tend to be promising in terms of reliability and scene coverage at a chosen junction. They provide 360 degrees of observation view, thus introducing key changes in traffic management.

Although fish eye cameras have a key role in junction management systems, accompanying challenges come with them as well, such as : High distortion ratios, Different scales of same target object moving in different parts of the image, Day/night views variance (night view suffers from low quality related to surrounding lightning conditions), Exposure introduced with vehicle lights (night view). A dataset of traffic videos from several junctions at different times during the day/night is provided with the annotation for training and validation ([icip2020.issd.com.tr](http://icip2020.issd.com.tr/)). The evaluation will be performed based on separate test datasets.
                               ![](https://signalprocessingsociety.org/sites/default/files/uploads/images/community_involvement/vip_cup_2020.jpg)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3574256%2Fb348e879d9c0bc19dca2482f384e7e67%2Fvip%20cup%202020.PNG?generation=1594841925511299&alt=media)


### Schedule

    - 30 June 2020: Initial Training Dataset released
    - 30 July 2020: Test Dataset 1 released
    - 30 August 2020: Submission deadline
    - 15 September 2020: Finalists (best three teams) announced
    - 25 October 2020: Competition on Test Dataset 2 virtually at ICIP 2020

### Registration

Register: [VIP Cup 2020 Registration Page](https://www2.securecms.com/VIPCup/VIPRegistration.asp)

### Eligibility Criteria

#### Each team must be composed of:

    1. One faculty member (the Supervisor);
    2. At most one graduate student (the Tutor);
    3 At least three but no more than ten undergraduate students (the Team Members)
    4. At least three of the undergraduate team members must be either IEEE Signal Processing Society (SPS) members or SPS student members.
    5. The VIP-Cup is a competition for undergraduate students and therefore Master’s students, regardless of the duration of their Bachelor’s degree, cannot participate as regular Team Members.
    6. Participants are expected to have basic knowledge of machine learning/deep learning concepts.

### Tasks to Execute and Expected Outcomes

    1. Detection of vehicles with high average accuracy and low false positives
    2. (Extra-1) Innovate new ideas to track vehicle flow from entering junction until exiting it

### Datasets (Training, Validation, Testing datasets)

The dataset is composed of` &gt;25k (twenty-five thousand) images for training + validation, 2k (two thousand) images for testing`. Images varies from day to night, collected at different junctions with different environment and installation conditions.

`Dataset is labeled in a standard COCO format. You may parse it the way you like.`

### Evaluation Criteria (Scores for Tasks, Outcomes and Overall)

   1.  Detection speed (20 point): Resulting algorithms will be benchmarked on a selected device for best performance.
   2.  Detection of vehicles accuracy (80 point):
   3. Assuming the detected vehicle is bounded by exact required size of bounding box as a detection indication. Final evaluation is done by ISSD with a separate dataset by averaging:
       i.  False positive detection is penalized by (-1point/per image)
       ii. Failure to detect is penalized by (-2point/per image)
   4. This score applies for each image, then averaged over the chosen set:
   5. Extra-1 (20 point): Estimation of correct path for vehicle entering junction until leaving it

### Submission guidelines

    1. Teams are required to submit there model inference evaluation via an intermediate representation, will be provided (30 July)
    2. Evaluation scripts (mAP, Average Recall, Average inference-time) will be provided (30 July) to teams in order to assess their work iteratively
    3. Best 3 teams in the leaderboard will be asked to submit their source code so we can reproduce the model (all copyrights are preserved)
    4. Extra-1 will have different qualification than the detection model itself (released on July 30)
    5. After model reproduction on our target machines winner will be announced
    6. Use of online available model would NOT be accepted and team would be disqualified

### Registration Guidelines

    1. Get familiar with the problem
    2. Get familiar with submission guidelines
    3. Register form through webpage icip2020.issd.com.tr

### Bibliography

    1. M. Bertozzi, L. Castangia, S. Cattani, A. Prioletti and P. Versari, "360° Detection and tracking algorithm of both pedestrian and vehicle using fisheye images," 2015 IEEE Intelligent Vehicles Symposium (IV), Seoul, 2015, pp. 132-137, doi: 10.1109/IVS.2015.7225675.
    2. Honghong Yang, Shiru Qu," Real-time vehicle detection and counting in complex traffic scenes using background subtraction model with low-rank decomposition", Engineering, 2017.
    3. Shokrolah Shirazi, Mohammad & Morris, Brendan," Vision-based vehicle queue analysis at junctions”, 2015, 10.1109/AVSS.2015.7301732.
    4. Wang, W. & Gee, Tim & Price, Jeff & Qi, Hairong. (2015). Real Time Multi-vehicle Tracking and Counting at Intersections from a Fisheye Camera. Proceedings - 2015 IEEE Winter Conference on Applications of Computer Vision, WACV 2015. 17-24. 10.1109/WACV.2015.10.
    5. Shokrolah Shirazi, Mohammad & Morris, Brendan. (2014). Vision-based turning movement counting at intersections by cooperating zone and trajectory comparison modules. 2014 17th IEEE International Conference on Intelligent Transportation Systems, ITSC 2014. 10.1109/ITSC.2014.6958188.
    6. Shokrolah Shirazi, Mohammad & Morris, Brendan. (2016). Looking at Intersections: A Survey of Intersection Monitoring, Behavior and Safety Analysis of Recent Studies. IEEE Transactions on Intelligent Transportation Systems. PP. 1-21. 10.1109/TITS.2016.2568920.

출처: Kaggle (awsaf49/vip-cup-2020)
태그: universities and colleges, arts and entertainment, sports, automobiles and vehicles
라이선스: CC0: Public Domain
수정일: 2020-08-02T18:30:26.807Z
