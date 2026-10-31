# Los Angeles Crime Data

Insights and Considerations from the Los Angeles Crime Data

The dataset captures instances of criminal activities within the **City of Los Angeles**, spanning from **2020 onwards**. The information originates from handwritten crime reports and, consequently, might contain certain inaccuracies. Instances of *missing data in location fields* are indicated as *(0°, 0°)*. To uphold privacy, address details are generalized to the closest hundred-block level. It's important to note that the accuracy of this dataset is comparable to the accuracy of the database.

Below are the details of various columns in the dataset:

| Column Name | Data Type | Description  | Type |
| ----- | ----- |
| DR_NO |Text | Division of Records Number: Official file number made up of a 2 digit year, area ID, and 5 digits | Plain Text |
| Date Rptd | Floating Timestamp |  MM/DD/YYYY | Date & Time |
| DATE OCC | Floating Timestamp | MM/DD/YYYY |	Date & Time |
| TIME OCC | Text | In 24 hour military time. |	Plain Text |
| AREA | Text | The LAPD has 21 Community Police Stations referred to as Geographic Areas within the department. These Geographic Areas are sequentially numbered from 1-21. | Plain Text |
| AREA NAME	| Text | The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles. | Plain Text |
| Rpt Dist No | Text | A four-digit code that represents a sub-area within a Geographic Area. All crime records reference the "RD" that it occurred in for statistical comparisons. Find LAPD Reporting Districts on the LA City GeoHub at&nbsp;http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4 | Plain Text |
| Part 1-2 | Number | Number | |
|Crm Cd |Text | Indicates the crime committed. (Same as Crime Code 1) | Plain Text |
| Crm Cd Desc | Text | Defines the Crime Code provided. |	Plain Text |
| Mocodes | Text | Modus Operandi: Activities associated with the suspect in commission of the crime. | Plain Text |
| Vict Age |Text | Two character numeric | Plain Text |
|Vict Sex	| Text | F - Female M - Male X - Unknown | Plain Text |
| Vict Descent| Text | Descent Code: A - Other Asian B - Black C - Chinese D - Cambodian F - Filipino G - Guamanian H - Hispanic/Latin/Mexican I - American Indian/Alaskan Native J - Japanese K - Korean L - Laotian O - Other P - Pacific Islander S - Samoan U - Hawaiian V - Vietnamese W - White X - Unknown Z - Asian Indian | Plain Text |
| Premis Cd |Number | The type of structure, vehicle, or location where the crime took place. | Number |
| Premis | Desc | Text | Defines the Premise Code provided. |	Plain Text |
| Weapon Used Cd | Text | The type of weapon used in the crime. | Plain Text |
| Weapon Desc | Text | Defines the Weapon Used Code provided. | Plain Text |
| Status |	Text	| Status of the case. (IC is the default) | Plain Text |
| Status Desc	| Text | Defines the Status Code provided. |	Plain Text |
| Crm Cd 1 | Text | Indicates the crime committed. Crime Code 1 is the primary and most serious one. Crime Code 2, 3, and 4 are respectively less serious offenses. Lower crime class numbers are more serious. | Plain Text |
| Crm Cd 2 |Text | May contain a code for an additional crime, less serious than Crime Code 1. | Plain Text |
| Crm Cd 3 | Text | May contain a code for an additional crime, less serious than Crime Code 1. | Plain Text |
| Crm Cd 4 | Text | May contain a code for an additional crime, less serious than Crime Code 1. | Plain Text |
| LOCATION |	Text | Street address of crime incident rounded to the nearest hundred block to maintain anonymity. | Plain Text |
| Cross Street | Text | Cross Street of rounded Address | Plain Text |
| LAT |Number | Latitude | Number |
| LON | Number | Longtitude | Number |



This is a pdf file [link for Mocode's](https://data.lacity.org/api/views/2nrs-mtv8/files/787064ac-a2f2-4cf3-a474-45036b7da937?download=true&filename=UCR-COMPSTAT062618.pdf) reference feel free to download

출처: Kaggle (zeeshanarif7/la-city-crime-data)
태그: crime
라이선스: CC0: Public Domain
수정일: 2023-08-18T05:50:26.783Z
