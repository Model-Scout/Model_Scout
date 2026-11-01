# Fama-French 5 Factor Model, South Korea

from september. 2006 to april 2022, including KOSPI and KOSDAQ

This dataset is a intermediate result for research with Professor Jay M. Chung, Soongsil Univ. 
This dataset consist of 6 columns: Mrt-Rf, HML, SMB, CMA, RMW, and RF. 

RF is the investment return of 91 day monetary stabilization bond of South Korea, works as risk-free rate in South Korean stock market.

For calculating the other factors I use the same or similar method of Fama&French (2015).
I will leave the link for the original paper.
[Link](https://www.sciencedirect.com/science/article/abs/pii/S0304405X14002323?casa_token=EG7l1rU5mvsAAAAA:fnfakptgEtHCrtEIn9FPme5-VLZB_mrKW3OxUhqDcDGjAyVdlMmjGBgBCA9fpEoNUD1chwLvjJE)

This data could be use to evaluate the performance or style of South Korean stock portfolios using the linear regression model that have HML, SMB, CMA, and RMW, Mrt-RF as independent vairables and Monthly portfolio return - RF as dependent variables. I will make a introductory notebook both in English and Korean.


The dataset's caveat is as follows.

- Historal RF is quite short, as  91 day monetary stabilization bond is a quite recent risk free asset. 
- I did not exclude financial firms or other non-standard firms while constructing the portfolios.
- Currently the factors contradicts with some previous studies.

출처: Kaggle (hyeonjunkim/fama-french-5-factor-model-south-korea)
태그: investing
라이선스: CC0: Public Domain
수정일: 2023-04-29T03:39:00.877Z
