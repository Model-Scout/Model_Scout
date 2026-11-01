# Sepsis Survival Prediction

110,204 admissions of 84,811 hospitalized subjects between 2011 - 2012 in Norway

The dataset consists of 110,204 admissions of 84,811 hospitalized subjects between 2011 and 2012 in Norway who were diagnosed with infections, systemic inflammatory response syndrome, sepsis by causative microbes, or septic shock. The prediction task is to determine whether a patient survived or is deceased at a time of about 9 days after collecting their medical record at the hospital. This is an important prediction problem in clinical medicine. Sepsis is a life-threatening condition triggered by an immune overreaction to infection, leading to organ failure or even death. Sepsis is associated with immediate death risk, often killing patients within one hour. This renders many laboratory tests and hospital analyses impractical for timely diagnosis and treatment. Being able to predict the survival of patients within minutes with as few and easy-to-retrieve medical features as possible is very important.

**What do the instances in this dataset represent?**

For the primary cohort, they represent records of patients affected by sepsis potential preconditions (ante Sepsis-3 definition); for the study cohort, they represent only the patients’ admissions defined by the novel Sepsis-3 definition.

**Are there recommended data splits?**

No recommendation, standard train-test split could be used. Can use three-way holdout split (i.e., training, validation/development, testing) when doing model selection.

**Does the dataset contain data that might be considered sensitive in any way?**

Yes. It contains information about the gender and age of the patient.

**Was there any data preprocessing performed?**

All the categorical variables have been encoded (so no preprocessing is necessary).

**Additional Information**

**Primary cohort from Norway:**
- 4 features for 110,204 patient admissions
- file: 's41598-020-73558-3_sepsis_survival_primary_cohort.csv'

**Study cohort (a subset of the primary cohort) from Norway:**
- 4 features for 19,051 patient admissions
- file: 's41598-020-73558-3_sepsis_survival_study_cohort.csv'

**Validation cohort from South Korea:**
- 4 features for 137 patients
- file: 's41598-020-73558-3_sepsis_survival_validation_cohort.csv'

The validation cohort from South Korea was used by Chicco and Jurman (2020) as an external validation cohort to confirm the generalizability of their proposed approach. 

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F2003977%2Ff3ff5773d5e02d2938b3ac4a0fa23e17%2FScreenshot%20from%202023-10-19%2010-05-33.png?generation=1697673946566777&alt=media)

출처: Kaggle (joebeachcapital/sepsis-survival-minimal-clinical-records)
태그: universities and colleges, health
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2023-10-19T00:01:34.700Z
