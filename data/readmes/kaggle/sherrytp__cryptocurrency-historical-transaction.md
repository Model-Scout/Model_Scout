# CryptoCurrency Historical Transactions

2020 Huobi Cryptocurrencies Past Transactions by second

### Context

The dataset is scrapped from [huobi website](https://www.huobi.vc/zh-cn/), used to develop our own models and trading strategies. Other than business use, since scrapping timely transactions for a certain period of past is available to the public, we figure that the Kaggle community could also benefit from using a parse of the datasets. [Huobi](https://en.wikipedia.org/wiki/Huobi), one of the cryptocurrency trading websites, is founded in China and then moves to have offices in Hong Kong, Korea, Japan, Singapore (now Singapore-based), and the United States, which works safely and easily to buy & sell, we have Bitcoin, Ethereum & Litecoin for everyone. Any information you find on this dataset is scrapped timely from the website-shown exchange, feel free to use that data, but any interpretation should not be subject to the dataset contributor or the provider (Huobi). We are pleased to get credited for any citations of research and project, but not responsible to answer questions or help in any kinds. 

### Content

The dataset contains files naming by the types of currency and date. The currency includes only BCH, ETC, and LTC; the date covers September 2020. The simple explanation of columns is the following: 
* tradeid: unique IDs for every single transaction made on the exchange website 
* symbol: (category) type of currency, relatively to USDT **NOTE**: there are also exceptions not linking to USDT. 
* ts: timestamp of that certain transaction made 
* price
* amount: transaction size 
* direction: (category) sell or buy 

### Acknowledgements

We wouldn't be here without the help of others. If you owe any attributions or thanks, include them here along with any citations of past research.

출처: Kaggle (sherrytp/cryptocurrency-historical-transaction)
태그: time series analysis, investing, currencies and foreign exchange
라이선스: Database: Open Database, Contents: © Original Authors
수정일: 2020-11-05T23:40:38.207Z
