---
base_model:
- classla/xlm-r-parla
language:
- multilingual
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
tags:
- topic
- parliamentary
- agenda-topic
- CAP
pipeline_tag: text-classification
---

# Multilingual ParlaCAP model for CAP Topic Classification in Parliamentary Speeches

The ParlaCAP model is a text classification model that assigns topic categories to parliamentary speeches according 
to the [CAP (Comparative Agendas Project) schema](https://www.comparativeagendas.net/pages/master-codebook).

This classification model is based on the multilingual parliamentary [XLM-R-Parla](https://huggingface.co/classla/xlm-r-parla) BERT-like model, 
which is a XLM-RoBERTa-large model that was additionally pre-trained on texts of parliamentary proceedings.
To develop the ParlaCAP model, XLM-R-Parla was additionally fine-tuned on the [ParlaCAP-train dataset](http://hdl.handle.net/11356/2093): 29,779 instances (speeches) from 
29 [ParlaMint 4.1](http://hdl.handle.net/11356/1912) datasets
containing transcriptions of parliamentary debates of 29 European countries and autonomous regions. 
The speeches were automatically annotated with 22 CAP labels (21 major topics and a label "Other") using the GPT-4o model 
in a zero-shot prompting fashion 
following the [LLM teacher-student framework](https://ieeexplore.ieee.org/document/10900365). 
Evaluation of the GPT model has shown that its annotation performance is
comparable to those of human annotators. For more information, see the paper ["Supercharging Agenda Setting Research: 
 The ParlaCAP Dataset of 28 European Parliaments and a Scalable Multilingual LLM-Based Classification"](https://doi.org/10.48550/arXiv.2602.16516) (Kuzman Pungeršek et al., 2026).

The fine-tuned ParlaCAP model achieves 0.723 in macro-F1 on an English test set, 
0.686 in macro-F1 on a Croatian test set, 0.710 in macro-F1 on a Serbian test set and 0.646 in macro-F1 on a Bosnian test set
(app. 880 manually-annotated instances from ParlaMint-GB 4.1, ParlaMint-HR 4.1, ParlaMint-RS 4.1 and ParlaMint-BA 4.1, respectively, balanced by labels).

For end use scenarios, we recommend filtering out predictions based on the model's prediction confidence.

When the model was applied to the ParlaMint datasets, we annotated instances that were predicted with confidence below 0.60 as "Mix".

With this approach, we annotate as Mix 8.9% of instances in the English test set,
11.4% of instances in the Croatian test set, 11.1% of instances in the Serbian and Bosnian test sets.


Performance of the model on the remaining instances (all instances not annotated as "Mix"):

|    |   micro-F1 |   macro-F1 |   accuracy |
|:---|-----------:|-----------:|-----------:|
| en |   0.761 |   0.758 |   0.761 |
| sr |   0.749 |   0.743 |   0.749 |
| hr |   0.724 |   0.726 |   0.724 |
| bs |   0.686 |   0.680 |   0.686 |



## Use

To use the model:
```
from transformers import pipeline

# Load a multi-class classification pipeline
# if the model runs on CPU, comment out "device"
classifier = pipeline("text-classification", model="classla/ParlaCAP-Topic-Classifier", device=0, max_length=512, truncation=True)

# Example texts to classify
texts = [
    """I engage regularly with the CPS, and we recognise that this issue is a growing national priority.
      Prosecution rates have been rising year on year for knife crime.
      Between 2013-14 and 2017-18, there has been a 33% increase.
      The Offensive Weapons Bill now making its way through this House will tighten the law around the sale, delivery and possession of knives.""",
    """I appreciate that there are pressures in the hon. Gentleman’s constituency.
      I think most hon. Members would say that there are pressures in their constituency when it comes to general practice,
      so what have we done so far? Let me put it that way.
      This year, 3,157 medical school graduates will go on to specialise in general practice,
      which is the highest ever, but we still have to do more to improve the retention of GPs who are approaching retirement."""]

# Classify the texts
results = classifier(texts)

# Output the results
for result in results:
    print(result)

## Output
##{'label': 'Law and Crime', 'score': 0.9945019483566284}
##{'label': 'Health', 'score': 0.9890311360359192}

```

To apply the model to the text corpora in the ParlaMint TXT format
 (e.g., such as the corpora from [ParlaMint 4.1](http://hdl.handle.net/11356/1912)), 
 you can follow the step-by-step instructions with code
  published on the CLARIN.SI GitHub repository 
  "[ParlaMint-Annotation-with-CAP-Topics](https://github.com/clarinsi/ParlaMint-Annotation-with-CAP-Topics)".

## How to Cite

Please cite the paper presenting the model:

```
@article{pungersek2026parlacap-paper,
      title={{Supercharging Agenda Setting Research: The ParlaCAP Dataset of 28 European Parliaments and a Scalable Multilingual LLM-Based Classification}}, 
      author={Kuzman Punger{\v s}ek, Taja and Rupnik, Peter and {\v S}irini{\'c}, Daniela and Ljube{\v s}i{\'c}, Nikola},
      year={2026},
      eprint={2602.16516},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.16516},
    journal={arXiv preprint arXiv:2602.16516},
}
```

You can also cite the model as follows:

```
@misc{parlacap_model,
    author       = {Kuzman Punger{\v s}ek, Taja and Ljube{\v s}i{\'c}, Nikola},
    title        = {Multilingual ParlaCAP model for CAP Topic Classification in Parliamentary Speeches},
    year         = 2025,
    url          = {https://huggingface.co/classla/ParlaCAP-Topic-Classifier},
	doi          = { 10.57967/hf/6684 },
    publisher    = { Hugging Face }
}

```

The authors acknowledge the OSCARS project - and its ParlaCAP cascading grant project -, which has received funding from the European Commission’s Horizon Europe Research and Innovation programme under grant agreement No. 101129751.

## CAP Label definition

We use 21 [CAP](https://www.comparativeagendas.net/) majortopics + category "Other" - 22 labels.

The label description:

```python

label_list = ["Education", "Technology", "Health", "Environment", "Housing", "Labor", "Defense", "Government Operations", "Social Welfare", "Other", "Macroeconomics", "Domestic Commerce", "Civil Rights", "International Affairs", "Transportation", "Immigration", "Law and Crime", "Agriculture", "Foreign Trade", "Culture", "Public Lands", "Energy"]


majortopics_description = {
 'Macroeconomics - issues related to domestic macroeconomic policy, such as the state and prospect of the national economy, economic policy, inflation, interest rates, monetary policy, cost of living, unemployment rate, national budget, public debt, price control, tax enforcement, industrial revitalization and growth.': 1,
 'Civil Rights - issues related to civil rights and minority rights, discrimination towards races, gender, sexual orientation, handicap, and other minorities, voting rights, freedom of speech, religious freedoms, privacy rights, protection of personal data, abortion rights, anti-government activity groups (e.g., local insurgency groups), religion and the Church.': 2,
 'Health - issues related to health care, health care reforms, health insurance, drug industry, medical facilities, medical workers, disease prevention, treatment, and health promotion, drug and alcohol abuse, mental health, research in medicine, medical liability and unfair medical practices.': 3,
 'Agriculture - issues related to agriculture policy, fishing, agricultural foreign trade, food marketing, subsidies to farmers, food inspection and safety, animal and crop disease, pest control and pesticide regulation, welfare for animals in farms, pets, veterinary medicine, agricultural research.': 4,
 'Labor - issues related to labor, employment, employment programs, employee benefits, pensions and retirement accounts, minimum wage, labor law, job training, labor unions, worker safety and protection, youth employment and seasonal workers.': 5,
 'Education - issues related to educational policies, primary and secondary schools, student loans and education finance, the regulation of colleges and universities, school reforms, teachers, vocational training, evening schools, safety in schools, efforts to improve educational standards, and issues related to libraries, dictionaries, teaching material, research in education.': 6,
 'Environment - issues related to environmental policy, drinking water safety, all kinds of pollution (air, noise, soil), waste disposal, recycling, climate change, outdoor environmental hazards (e.g., asbestos), species and forest protection, marine and freshwater environment, hunting, regulation of laboratory or performance animals, land and water resource conservation, research in environmental technology.': 7,
 'Energy - issues related to energy policy, electricity, regulation of electrical utilities, nuclear energy and disposal of nuclear waste, natural gas and oil, drilling, oil spills, oil and gas prices, heat supply, shortages and gasoline regulation, coal production, alternative and renewable energy, energy conservation and energy efficiency, energy research.': 8,
 'Immigration - issues related to immigration, refugees, and citizenship, integration issues, regulation of residence permits, asylum applications; criminal offences and diseases caused by immigration.': 9,
 'Transportation - issues related to mass transportation construction and regulation, bus transport, regulation related to motor vehicles, road construction, maintenance and safety, parking facilities, traffic accidents statistics, air travel, rail travel, rail freight, maritime transportation, inland waterways and channels, transportation research and development.': 10,
 'Law and Crime - issues related to the control, prevention, and impact of crime; all law enforcement agencies, including border and customs, police, court system, prison system; terrorism, white collar crime, counterfeiting and fraud, cyber-crime, drug trafficking, domestic violence, child welfare, family law, juvenile crime.': 12,
 'Social Welfare - issues related to social welfare policy, the Ministry of Social Affairs, social services, poverty assistance for low-income families and for the elderly, parental leave and child care, assistance for people with physical or mental disabilities, including early retirement pension, discounts on public services, volunteer associations (e.g., Red Cross), charities, and youth organizations.': 13,
 'Housing - issues related to housing, urban affairs and community development, housing market, property tax, spatial planning, rural development, location permits, construction inspection, illegal construction, industrial and commercial building issues, national housing policy, housing for low-income individuals, rental housing, housing for the elderly, e.g., nursing homes, housing for the homeless and efforts to reduce homelessness, research related to housing.': 14,
 'Domestic Commerce - issues related to banking, finance and internal commerce, including stock exchange, investments, consumer finance, mortgages, credit cards, insurance availability and cost, accounting regulation, personal, commercial, and municipal bankruptcies, programs to promote small businesses, copyrights and patents, intellectual property, natural disaster preparedness and relief, consumer safety; regulation and promotion of tourism, sports, gambling, and personal fitness; domestic commerce research.': 15,
 'Defense - issues related to defense policy, military intelligence, espionage, weapons, military personnel, reserve forces, military buildings, military courts, nuclear weapons, civil defense, including firefighters and mountain rescue services, homeland security, military aid or arms sales to other countries, prisoners of war and collateral damage to civilian populations, military nuclear and hazardous waste disposal and military environmental compliance, defense alliances and agreements, direct foreign military operations, claims against military, defense research.': 16,
 'Technology - issues related to science and technology transfer and international science cooperation, research policy, government space programs and space exploration, telephones and telecommunication regulation, broadcast media (television, radio, newspapers, films), weather forecasting, geological surveys, computer industry, cyber security.': 17,
 'Foreign Trade - issues related to foreign trade, trade negotiations, free trade agreements, import regulation, export promotion and regulation, subsidies, private business investment and corporate development, competitiveness, exchange rates, the strength of national currency in comparison to other currencies, foreign investment and sales of companies abroad.': 18,
 'International Affairs - issues related to international affairs, foreign policy and relations to other countries, issues related to the Ministry of Foreign Affairs, foreign aid, international agreements (such as Kyoto agreement on the environment, the Schengen agreement), international organizations (including United Nations, UNESCO, International Olympic Committee, International Criminal Court), NGOs, issues related to diplomacy, embassies, citizens abroad; issues related to border control; issues related to international finance, including the World Bank and International Monetary Fund, the financial situation of the EU; issues related to a foreign country that do not impact the home country; issues related to human rights in other countries, international terrorism.': 19,
 'Government Operations - issues related to general government operations, the work of multiple departments, public employees, postal services, nominations and appointments, national mints, medals, and commemorative coins, management of government property, government procurement and contractors, public scandal and impeachment, claims against the government, the state inspectorate and audit, anti-corruption policies, regulation of political campaigns, political advertising and voter registration, census and statistics collection by government; issues related to local government, capital city and municipalities, including decentralization; issues related to national holidays.': 20,
 'Public Lands - issues related to national parks, memorials, historic sites, and protected areas, including the management and staffing of cultural sites; museums; use of public lands and forests, establishment and management of harbors and marinas; issues related to flood control, forest fires, livestock grazing.': 21,
 'Culture - issues related to cultural policies, Ministry of Culture, public spending on culture, cultural employees, issues related to support of theatres and artists; allocation of funds from the national lottery, issues related to cultural heritage': 23,
 'Other - other topics not mentioning policy agendas, including the procedures of parliamentary meetings, e.g., points of order, voting procedures, meeting logistics; interpersonal speech, e.g., greetings, personal stories, tributes, interjections, arguments between the members; rhetorical speech, e.g., jokes, literary references.': 0
 }

 ```