# BTS youtube channel dataset (+ thumnails img)

classification problem

## **Context**
BTS (a seven-member South Korean boy band debuted in 2013-06-13) started YOUTUBE channel at 2012-12-17. 
Until 2021-09-21 , They published 1,368 YOUTUBE videos on the channel. Using YOUTUBE API, scrap video's data.
     
     
     
      
##**Content**

**The tabular data contains 16 columns** 


- kind : video kind ( youtube api parameter)        
- etag : video etag ( youtube api parameter)        
- items : video items (api return values)        
- pageInfo :video pageInfo ( youtube api parameter)        
- pub : video publish Time ( utc + 9:00 Asis/Seoul)        
- id : video id (orgin_url :  https://www.youtube.com/watch?v={id})                                                             
- title : video title.             
- description : video description.        
- thumbnails : thumbnais url        
- tags : video tags         
- duration: video duration time        
- viewCount : viewcount of video (at 2021-09-21)        
- likeCount : likeCount of video (at 2021-09-21)        
- dislikeCount : dislikeCount of video (at 2021-09-21)        
- commentCount : commentCount of video (at 2021-09-21)        
- image_path : thumbnails image_path         
- category : BB : bangtan bomb , CG : choreography , RV : review , EP : episode, vlog : daily vlog , FESTA :FESTA , NA : else         
        
        
        
        

##**Additional information**
category column is createed by my standards. 
        
        

     

##**Data Source**
rawa data from [channel](https://www.youtube.com/channel/UCLkAepWjdylmXSltofFvsYQ) by YOUTUBE AP

출처: Kaggle (kukuroo3/bts-youtube-channel-dataset-thumnails-img)
태그: music, classification, tabular, multiclass classification, multilabel classification
라이선스: CC0: Public Domain
수정일: 2021-12-18T03:44:23.907Z
