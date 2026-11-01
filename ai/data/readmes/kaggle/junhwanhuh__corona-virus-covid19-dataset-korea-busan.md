# Corona Virus (COVID-19) Dataset (Korea, Busan)

City Scale COVID-19 Dataset with Hierarchical Time-Series Information

### Context
Started in China, the Wuhan corona-virus is spreading around the world. Also, Korea is currently suffering from a virus that is spreading rapidly. The new coronavirus is difficult to analyze because it spreads through a variety of pathways, including asymptomatic infections.

Also, the infection propagation pattern differs from region to region, which requires specialized analysis for each city. We focused on constructing and analyzing data sets to prevent local infections in Busan City.

The following web app developed for visualizing and analyzing the local infection situation in Busan in a time series.
[http://corona-busan.co.kr](http://corona-busan.co.kr)

### Content
In Korea, viruses are spreading rapidly due to certain religious activities. To analyze unusual situations, we included religion as a type of infection, and we constructed a confirmatory line over time to quickly identify contaminated areas and minimize additional infections.

### Structure Description
*Busan_Patient_Path.json*
In this data include 3-large hierachical category of patient (patient\_info, infection\_info, route\_info)

* Patient\_info 
  * patient\_id : {patient id provide from busan city}
  * age
  * sex
  * country
  * religion : {“ShinCheonJi”, “Catholic”, “-“}
  * residential\_info 
    - city
    - district
    - latitude
    - longtitude
* Infection\_Info 
  * Infection\_Place 
     - name
     - latitude
     - longtitude
  * Infection\_type : {“family”, "friend“, "place”, “religion”, "other"}
  * Infection\_factor : {number of contactor}
  * Isolation\_place 
     - name
     - latitude
     - longtitude
* Route {Array} 
  * name : {visit place name}
  * latitude
  * longtitude
  * start\_time : {arrival time}
  * end\_time : {departure time}

### Acknowledgements

Pusan ​​National University(PNU) CSE, Chang-Hong Lee, and Jun-Hwan Huh has made the data sets and develop an analysis framework for the public good.

Source of data:  [Busan City](http://www.busan.go.kr/corona19/index), [KCDC](http://www.cdc.go.kr/index.es?sid=a2) (Korea Centers for Disease Control & Prevention),

Thanks to the Korean Government and Busan city for making data available.

### Inspiration

1. The virus spread caused by religion activity
2. Change in virus spread cases over at city level
3. Relationships between patients by infection type

출처: Kaggle (junhwanhuh/corona-virus-covid19-dataset-korea-busan)
태그: health, computer science, health conditions
라이선스: CC0: Public Domain
수정일: 2020-03-07T19:12:46.050Z
