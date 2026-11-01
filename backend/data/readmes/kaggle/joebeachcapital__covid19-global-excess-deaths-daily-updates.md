# Covid19 Global Excess Deaths (daily updates)

Daily updates of the Economist's Covid19 Global Excess Deaths data

Daily updates of Covid-19 Global Excess Deaths from the Economist's GitHub repository: https://github.com/TheEconomist/covid-19-the-economist-global-excess-deaths-model

**Interpreting estimates**

Estimating excess deaths for every country every day since the pandemic began is a complex and difficult task. Rather than being overly confident in a single number, limited data means that we can often only give a very very wide range of plausible values. Focusing on central estimates in such cases would be misleading: unless ranges are very narrow, the 95% range should be reported when possible. The ranges assume that the conditions for bootstrap confidence intervals are met. Please see our tracker page and methodology for more information.

**New variants**

The Omicron variant, first detected in southern Africa in November 2021, appears to have characteristics that are different to earlier versions of sars-cov-2. Where this variant is now dominant, this change makes estimates uncertain beyond the ranges indicated. Other new variants may do the same. As more data is incorporated from places where new variants are dominant, predictions improve.

**Non-reporting countries**

Turkmenistan and the Democratic People's Republic of Korea have not reported any covid-19 figures since the start of the pandemic. They also have not published all-cause mortality data. Exports of estimates for the Democratic People's Republic of Korea have been temporarily disabled as it now issues contradictory data: reporting a significant outbreak through its state media, but zero confirmed covid-19 cases/deaths to the WHO.

**Acknowledgements**

A special thanks to all our sources and to those who have made the data to create these estimates available. We list all our sources in our methodology. Within script 1, the source for each variable is also given as the data is loaded, with the exception of our sources for excess deaths data, which we detail in on our free-to-read excess deaths tracker as well as on GitHub. The gradient booster implementation used to fit the models is aGTBoost, detailed here.

Calculating excess deaths for the entire world over multiple years is both complex and imprecise. We welcome any suggestions on how to improve the model, be it data, algorithm, or logic. If you have one, please open an issue.

The Economist would also like to acknowledge the many people who have helped us refine the model so far, be it through discussions, facilitating data access, or offering coding assistance. A special thanks to Ariel Karlinsky, Philip Schellekens, Oliver Watson, Lukas Appelhans, Berent Å. S. Lunde, Gideon Wakefield, Johannes Hunger, Carol D'Souza, Yun Wei, Mehran Hosseini, Samantha Dolan, Mollie Van Gordon, Rahul Arora, Austin Teda Atmaja, Dirk Eddelbuettel and Tom Wenseleers.

All coding and data collection to construct these models (and make them update dynamically) was done by Sondre Ulvund Solstad. Should you have any questions about them after reading the methodology, please open an issue or contact him at sondresolstad@economist.com.

**Suggested citation**
The Economist and Solstad, S. (corresponding author), 2021. The pandemic’s true death toll. [online] The Economist. Available at: https://www.economist.com/graphic-detail/coronavirus-excess-deaths-estimates [Accessed ---]. First published in the article "Counting the dead", The Economist, issue 20, 2021.

출처: Kaggle (joebeachcapital/covid19-global-excess-deaths-daily-updates)
태그: global, diseases, business, economics, mortality, time series analysis, covid19
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-10-31T06:19:54.510Z
