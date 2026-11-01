# COVID-19 latent period computational experiment

Results of SEIR model fitting with different latent periods

# Abstract

The incubation period for the COVID-19 is reported [many times](https://www.kaggle.com/covid-19-contributions#Incubation%20period). We can't say the same for the latent period (the period since the person is infected but does not spread the infection yet), which is vital characteristic of every infectious disease. Knowing the latent period gives an ability to run simulations which are far more accurate. In this study I try to estimate the latent period for COVID-19 caused by SARS-CoV-2 virus via computational simulations using SEIR model with different values controlling the latent period length (e.g. latent period parameter sweep). I try to fit all other parameters to match the observed statistics the best. I do such modelling for 5 different locations worldwide which are currently experiencing different stages of the epidemic.

As a result, Europe locations suggest that latent period is between 2 and 4 days: Austria case suggests the value of 48-96 hours, Italy case suggests the value greater than 48 hours. While China cases suggest shorter latent period.

# Introduction

## The data

I use the time series data (infected count, recovered count and deaths count) published by the [John Hopkins University](https://github.com/CSSEGISandData/COVID-19) as ground truth observations.

I experiment with these 5 locations:
* Austria (infection peak has passed)
* Beijing, China (there were 2 peaks)
* Heilongjiang, China (two more distinct peaks)
* Italy (Peak is approaching)
* South Korea (single peak passed long ago)

## The model

I use SEIR model defined as 
![SEIR equations](https://idmod.org/docs/hiv/_images/math/5c34ba7654b6b1031ac83c60ea98007456d22ee3.png)

## Latent period estimation

Latent period can be estimated as reciprocal to sigma parameter. Thus `latent period = 1.0 / sigma`

## The parameter fitting procedure

I let the optimizer to fit the following parameters:
* Infection start date
* number of the exposed people count on the first day of infection
* number of the infected people count on the first day of infection
* beta (separate value per week) - infection rate
* gamma - recovery rate

The loss function is RMSE.

For every location and every value of sigma (reciprocal of latent period) I use several runs of Nelder-Mead optimizer and BFGS optimizer runs starting at different random initial conditions and take the best fit.

The full computational experiment code is published [on the GitHub](https://github.com/dgrechka/covid19-global-forecasting/tree/master/sigmaEvaluation).

출처: Kaggle (dgrechka/covid19-latent-period-computational-experiment)
태그: computer science, software
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2020-04-19T11:07:25.703Z
