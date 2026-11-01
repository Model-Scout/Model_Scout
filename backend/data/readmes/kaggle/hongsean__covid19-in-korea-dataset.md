# COVID-19 in Korea dataset

daily confirmed case with demographic and geographic information

### Context

- A new coronavirus designated 2019-nCoV was first identified in Wuhan, the capital of China's Hubei province
- People developed pneumonia without a clear cause and for which existing vaccines or treatments were not effective
- The virus has shown evidence of human-to-human transmission
- Korea has defended well against coronavirus until summer, but it increased many confirmed cases from fall
- As of 24th Dec. approximately 53K cases have been confirmed, and daily around 1K cases are getting confirmed 
- This datasets are prepared to cheer Korea up fighting against coronavirus

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F4837224%2Ff829b8bd45aacf4c63b17e0116cb52c9%2Fcover_photo.PNG?generation=1608792447857317&alt=media)



### Content

- 3 files attached which are 1) COVID Korea Status 2) COVID Korea Demo 3) COVID Korea Geo 

- 1) COVID Korea Status : General daily update
   . STATE_DT : standard date
   . STATE_TIME : standard time
   . DECIDE_CNT : confirmed cases 
   . CLEAR_CNT : clear cases after hospitalization
   . EXAM_CNT : examination cases 
   . DEATH_CNT : death counts 
   . CARE_CNT : counts on care 
   . RESUTL_NEG_CNT : negative results after examination 
   . ACC_EXAM_CNT : accumulative examination counts 
   . ACC_EXAM_COMP_CNT: accumulative examination completes count
   . ACC_DEF_RATE : accumulative confirmed rate 
   . CREATE_DT : posted date and time 
   . UPDATE_DT : updated date and time 

- 2) COVID Korea Demo : Updates with demographic information 
  . GUBUN : classified by gender and age 
  . CONF_CASE : confirmed cases 
  . CONF_CASE_RATE : confirmed case rate 
  . DEATH : death counts 
  . DEATH_RATE : death rate 
  . CRITICAL_RATE : critical rate 
  . CREATE_DT : created date and time 
  . UPDATE_DT : updated date and time 

- 3) COVID Korea Geo : Updates with geographic information  
  . CREATE_DT : created date and time  
  . DEATH_CNT : death counts    
  . GUBUN : city name      
  . GUBUN_CN : city name in Chinese    
  . GUBUN_EN : city name in English     
  . INC_DEC : increase/decrease vs. past day     
  . ISOL_CLEAR_CNT : clear counts from isolation      
  . QUR_RATE : confirmed rate per 100K people      
  . STD_DAY : standard day      
  . UPDATE_DT : updated date and time     
  . DEF_CNT : confirmed cases      
  . ISOL_ING_CNT : isolated cases     
  . OVER_FLOW_CNT : confirmed cases from foreign countries       
  . LOCAL_OCC_CNT : domestic confirmed cases 

### Acknowledgements

- http://www.kdca.go.kr/cdc/
- https://data.go.kr/index.do

If these are useful, I will frequently update. Thanks.

출처: Kaggle (hongsean/covid19-in-korea-dataset)
태그: social science, covid19, korea
라이선스: CC0: Public Domain
수정일: 2020-12-28T07:38:53.887Z
