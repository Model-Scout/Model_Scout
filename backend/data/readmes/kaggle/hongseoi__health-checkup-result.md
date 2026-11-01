# Health Checkup Result

Health Checkup Result  of 19,000,000 people in South Korea, 2002~2020

# Health Checkup Result
## Health Checkup Result of 19,000,000 people in South Korea, 2002~2020

- [GitHub Link](https://github.com/hongseoi/KaggleDatasets/tree/main/Health%20Checkup%20Result)
- [Source Link](https://www.data.go.kr/data/15112444/fileData.do)

In Korea, everyone is compulsorily required to join the National Health Insurance. The National Health Insurance Service (NHIS), which manages national health insurance, provides basic health checkups to subscribers every year.

This dataset is the result of a random sampling of 1 million people per year from 2002 to 2021 among those who underwent basic health checkups provided by the NHIS.

Missing values are those that have not been selectively tested by individuals.

This dataset consists of a total of 19 csv files for each year, and each csv file contains only the health checkup results for that year. There are differences in the features of the dataset by year.

1. Difference in the number of columns
- There are features that have been excluded or added by year.
<a href="https://ibb.co/XX5FDvx"><img src="https://i.ibb.co/5Tjskfh/feature-stat.jpg" alt="feature-stat"></a>


2. Difference in AREA_CODE
- After 2012, a new area, 'SEAJONG' was named and a new area code, 36, was added.
<a href="https://ibb.co/L83d6R5"><img src="https://i.ibb.co/xDNqGLH/AREA-CODE.jpg" alt="AREA-CODE"></a><br><a target="_blank" href="https://whatsmyscreenresolution.com/"></a>

3. Categorization differences in AGE_GROUP
- There is a difference in age categorization criteria between 2002 and 2013 and the dataset after 2014.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/d2gCQRJ/AGE-GROUP.jpg" alt="AGE-GROUP"></a>

A description of each column is as follows.

### Feature Description

| feature name | description | form of expression | range |
|:---------:|----------|-------------|------------|
| YEAR | Base year of the information|YYYY|2002~2020|
|IDV_ID|Serial number assigned to subscriber |N|1~1,000,000|
|AREA_CODE|Residency code of examinee|N||
|SEX|Gender|N |1: male, 2:female|
|AGE_GROUP|A code that categorizes the examinee's age into 5-year-olds based on the year. Refer to the table below for details.|N|2002~2013: 1~14, 2014~: 1~18|
|HEIGHT|Examiner's height (in units of 5 cm)|N/cm||
|WEIGHT|Examiner's weight (in units of 5 kg)|N/Kg||
|WAIST|examiner's waist circumference|N/Kg||
|SIGHT_LEFT|Eyesight of the examinee's left eye|N|(0.1~2.5, eyesight &lt; 0.1 == 0.1, blind==9.9)|
|SIGHT_RIGHT|Eyesight of the examinee's right eye|N|(0.1~2.5, eyesight &lt; 0.1 == 0.1, blind==9.9)|
|BP_HIGH|The examiner's systolic blood pressure|N/mmHg||
|BP_LWST|Diastolic blood pressure of examinee|N/mmHg||
|BLDS|Pre-meal blood glucose of the examinee. The concentration of glucose per 100 ml of blood|N/mg/dL||
|TOT_CHOLE|Sum of ester and non-ester cholesterol in serum. Normal values are 150 to 250 mg/dL|mg/dL||
|TRIGLYCERIDE|Amount of simple lipids or neutral lipids. Normal values are 30 to 135 mg/dL|mg/dL||
|HDL_CHOLE|The amount of cholesterol contained in HDL. Normal values are 30 to 65 mg/dL.|mg/dL||
|LDL_CHOLE|The amount of cholesterol contained in LDL. If it is 170 mg/dL or higher, hyper-LDLemia is diagnosed.|mg/dL||
|CREATININE|Serum concentration of creatinine, the dehydration of creatine. Increases and decreases in creatinine are not related to food, but to muscle development and exercise. Normal values are 0.8 to 1.7 mg/dL.|mg/dL||
|HMG| It is a pigment-protein present in blood and blood cells, composed of globin and heme, and plays a role as an oxygen carrier in the blood.|N/g/dL||
|OLIG_PROTE_CD|excretion of protein in the urine|N|1(-), 2(±), 3(+1), 4(+2), 5(+3), 6(+4)|
|SGOT_AST|Levels on blood tests that indicate liver function. Concentrations increase when liver cells, heart, kidney, brain, and muscle cells are damaged. Normal value is 0~40IU/L|N/IU/L||
|SGPT_ALT| Levels in blood tests that indicate liver function. ALT mainly exists only in hepatocytes, and its concentration increases when hepatocytes are damaged. Normal values are 0 to 40 IU/L| N/IU/L|
|GAMMA_GTP|Levels in blood tests that indicate liver function. Gamma GTP is an enzyme mainly present in the bile duct in the liver, and blood concentration increases when bile excretion disorder or hepatocellular disorder occurs. Normal values are 11 to 64 IU/L for men and 8 to 35 IU/L for women.|N/IU/L||
|SMK_STAT|Whether or not the examinee's smoking status|N|1 (don't smoke) / 2 (smoked before, but quit) / 3 (currently smokes)|
|DRK_YN|Whether or not the examinee's drinking status|N|0,N (don't drink) / 1,Y (drinking)|
|HCHK_CE_IN|Whether or not the examinee chose oral examination.|N| 0,N (not tested)/1,Y (tested)|
|CRS_YN|Whether or not the examinee has dental caries|N|0 (none) / 1 (present)|
|TTH_MSS_YN|Existence of missing teeth of the examinee|N|0 (none) / 1 (present)|
|ODT_TRB_YN|Whether or not the examinee has dental abrasion|N|0 (none) / 1 (present)|
|WSDM_DIS_YN|Whether or not the examinee has wisdom teeth|N|0 (none) / 1 (present)|
|TTR_YN|Whether or not the examinee has calculus||0,N (none) / 1,Y (present)|
|DATE|Date the data was created|YYYY-MM-DD||

출처: Kaggle (hongseoi/health-checkup-result)
태그: asia, healthcare, health, health conditions, korea
라이선스: Unknown
수정일: 2023-02-27T16:29:39.303Z
