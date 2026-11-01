# USA Big City Crime Data

Crime Data of different large US Cities

This dataset contains different collected datasets with crime data of many large cities. Below are the descriptions for each seperate dataset. Note: Dataset properties and column may differ from each other since the information was collected by the local police in different styles and situations. 

1. Los Angeles

The Los Angeles dataset has the collected data on different crimes that happened in Los Angeles from 2000 up until May 2024. The columns are as follows:

- DR_NO - Division of Records Number: Official file number made up of a 2 digit year, area ID, and 5 digits

- Date Rptd - The date when the police found out about the crime

- Date OCC - The actual date of the crime

- Time OCC - In military time

- Area - The LAPD has 21 Community Police Stations referred to as Geographic Areas within the department. These Geographic Areas are sequentially numbered from 1-21.

- Area Name - The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles.

- Rpt Dist No - A four-digit code that represents a sub-area within a Geographic Area. All crime records reference the "RD" that it occurred in for statistical comparisons. Find LAPD Reporting Districts on the LA City GeoHub at [http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4](http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4)

- Crm Cd - Indicates the crime committed. (Same as Crime Code 1)

- Crm Cd Desc - Defines the Crime Code provided.

- Mocodes - Modus Operandi: Activities associated with the suspect in commission of the crime.

- Vict Age - The age of the victim

- Vict Sex - The gender of the victim. They are as follows:
 - M - Male
 - F - Female
 - X - Unknown 

- Vict Descent - Descent Code: 
 - A - Other Asian 
 - B - Black 
 - C - Chinese 
 - D - Cambodian
 - F - Filipino 
 - G - Guamanian 
 - H - Hispanic/Latin/Mexican 
 - I - American Indian/Alaskan Native 
 - J - Japanese 
 - K - Korean 
 - L - Laotian 
 - O - Other 
 - P - Pacific Islander 
 - S - Samoan 
 - U - Hawaiian 
 - V - Vietnamese 
 - W - White 
 - X - Unknown 
 - Z - Asian Indian

- Premis Cd - The type of structure, vehicle, or location where the crime took place.

- Premis Desc - Defines the Premise Code provided.

- Weapon Used Cd - The type of weapon used in the crime.

- Status - Status of the case. (IC is the default)

- Status Desc - Defines the Status Code provided.

- Crm Cd 1 - Indicates the crime committed. Crime Code 1 is the primary and most serious one. Crime Code 2, 3, and 4 are respectively less serious offenses. Lower crime class numbers are more serious.

- Crm Cd 2 - May contain a code for an additional crime, less serious than Crime Code 1.

- Crm Cd 3 - May contain a code for an additional crime, less serious than Crime Code 1.

- Crm Cd 4 - May contain a code for an additional crime, less serious than Crime Code 1.

- Location - Street address of crime incident rounded to the nearest hundred block to maintain anonymity.

- Cross Street - Cross Street of rounded Address

- LAT - Latitude

- LON - Longitude

This dataset has 28 columns and 944K rows. I hope you will find it useful. God bless you

2. Chicago

This dataset contains crime data on Chicago, from 2001 to present. The columns are as follows:

- ID - Unique Identifier for the record

- Case Number - The Chicago Police Department RD Number (Records Division Number), which is unique to the incident.

- Date - Date when the incident occurred. this is sometimes a best estimate.

- Block - The partially redacted address where the incident occurred, placing it on the same block as the actual address.

- IUCR - The Illinois Unifrom Crime Reporting code. This is directly linked to the Primary Type and Description. See the list of IUCR codes at [https://data.cityofchicago.org/d/c7ck-438e.](https://data.cityofchicago.org/d/c7ck-438e).

- Primary Type - The primary description of the IUCR code.

- Description - The secondary description of the IUCR code, a subcategory of the primary description.

- Location Description - Description of the location where the incident occurred.

- Arrest - Indicates whether an arrest was made.

- Domestic - Indicates whether the incident was domestic-related as defined by the Illinois Domestic Violence Act.

- Beat - Indicates the beat where the incident occurred. A beat is the smallest police geographic area – each beat has a dedicated police beat car. Three to five beats make up a police sector, and three sectors make up a police district. The Chicago Police Department has 22 police districts. See the beats at [https://data.cityofchicago.org/d/aerh-rz74](https://data.cityofchicago.org/d/aerh-rz74).

- District - Indicates the police district where the incident occurred.

- Ward - The ward (City Council district) where the incident occurred.

- Community Area - Indicates the community area where the incident occurred. Chicago has 77 community areas.

- FBI Code - Indicates the crime classification as outlined in the FBI's National Incident-Based Reporting System (NIBRS).See the Chicago Police Department listing of these classifications at [https://gis.chicagopolice.org/pages/crime_details](https://gis.chicagopolice.org/pages/crime_details).

- X Coordinate - The x coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.

- Y Coordinate - The y coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.

- Year - Year the incident occurred

- Updated On - Date and time the record was last updated.

- Latitude - The latitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.

- Longitude - The longitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.

- Location - 	The location where the incident occurred in a format that allows for creation of maps. This location is shifted from the actual location for partial redaction but falls on the same block.

This dataset has 22 columns and 8.07M rows. I hope you will find it useful. God bless you

출처: Kaggle (middlehigh/los-angeles-crime-data-from-2000)
태그: crime
라이선스: CC0: Public Domain
수정일: 2024-05-28T18:56:36.147Z
