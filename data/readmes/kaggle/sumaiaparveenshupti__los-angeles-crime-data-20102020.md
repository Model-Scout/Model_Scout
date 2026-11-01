# Los Angeles Crime Data 2010-2020

Public Safety Data released by the LAPD

### Context

This dataset reflects incidents of crime in the City of Los Angeles dating back from 2010 to 2020. This data is transcribed from original crime reports that are typed on paper and therefore there may be some inaccuracies within the data. Some location fields with missing data are noted as (0°, 0°). Address fields are only provided to the nearest hundred block in order to maintain privacy. This data is as accurate as th the data in the database.


### Attribute Description

**DR_NO**: Division of Records Number: Official file number made up of a 2 digit year, area ID, and 5 digits.
**API Field Name**: MM/DD/YYYY.
**DATE OCC**: MM/DD/YYYY.
**TIME OCC**: In 24 hour military time.
**AREA**: The LAPD has 21 Community Police Stations referred to as Geographic Areas within the department. These Geographic Areas are sequentially numbered from 1-21.
**AREA NAME**: The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles.
**Rpt Dist No**: A four-digit code that represents a sub-area within a Geographic Area. All crime records reference the "RD" that it occurred in for statistical comparisons.
**Crm Cd**: Indicates the crime committed. (Same as Crime Code 1)
**Crm Cd Desc**: Defines the Crime Code provided.
**Mocodes**: Modus Operandi: Activities associated with the suspect in commission of the crime.
**Vict Age**: Two character numeric.
**Vict Sex**: F - Female M - Male X - Unknown.
**Vict Descent**: Descent Code: A - Other Asian B - Black C - Chinese D - Cambodian F - Filipino G - Guamanian H - Hispanic/Latin/Mexican I - American Indian/Alaskan Native J - Japanese K - Korean L - Laotian O - Other P - Pacific Islander S - Samoan U - Hawaiian V - Vietnamese W - White X - Unknown Z - Asian Indian.
**Premis Cd**: The type of structure, vehicle, or location where the crime took place.
**Premis Desc**: Defines the Premise Code provided.
**Weapon Used Cd**: The type of weapon used in the crime.
**Weapon Desc**: Defines the Weapon Used Code provided.
**Status**: Status of the case. (IC is the default).
**Status DEsc**: Defines the Status Code provided.
**Crm Cd 1**: Indicates the crime committed. Crime Code 1 is the primary and most serious one. Crime Code 2, 3, and 4 are respectively less serious offenses. Lower crime class numbers are more serious.
**Crm Cd 2**: May contain a code for an additional crime, less serious than Crime Code 1.
**Crm Cd 3**: May contain a code for an additional crime, less serious than Crime Code 1.
**Crm Cd 4**: May contain a code for an additional crime, less serious than Crime Code 1.
**LOCATION**: Street address of crime incident rounded to the nearest hundred block to maintain anonymity.
**Cross Street**: Cross Street of rounded Address.
**LAT**: Latitude.
**LON**: Longitude.

### Acknowledgements

Los Angeles Police Department

출처: Kaggle (sumaiaparveenshupti/los-angeles-crime-data-20102020)
태그: united states, crime, beginner, tabular, public safety
라이선스: CC0: Public Domain
수정일: 2021-06-22T20:09:10.940Z
