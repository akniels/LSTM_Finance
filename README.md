# LSTM_Finance
Walks through the process of extracting finance data and running LSTM for prediction

This shows the step by step process for making a Lont Short Term Memory prediction in Python. This contains 4 Files. The first file [Total Process for Prediction](https://github.com/akniels/LSTM_Finance/blob/main/Total%20Process%20for%20Prediction.ipynb) shows the data ETL and prediction in a Jupyter Notebook. This file utilizes and walkthrough data cleansing in spark and predictions done in scikit learn. The second file [ETL_extraction](https://github.com/akniels/LSTM_Finance/blob/main/etl.py) extracts the data using the yfinance plugin using the [nasdaq_screener](https://github.com/akniels/LSTM_Finance/blob/main/nasdaq_screener.csv) in a pythonic object oriented way. The Nasdaq screeener can be found [here](https://www.nasdaq.com/market-activity/stocks/screener). The spark ETL cleans and prepares the data using spark for LSTM prediction in an object oriented way. The data is front filled for missing data and any data with null values are removed. Additional fields are added (7 and 20 day moving average and Bollinger™ bands and a five day lead close which is what we are trying to predict). Visualizations are created to show the the trend for PFG and AIG (Principal Financial Group and American International Group).The Data is then joined to the nasdaq screener to see if any coorelations exist with the sector and industry. Data is then transferred to pandas and prepared for machine learning with the min max scaler and then an LSTM is ran for prediction.

## Acknowledgements
Yfinance code examples
* https://github.com/ranaroussi/yfinance
Spark Code examples
* https://towardsdatascience.com/create-your-first-etl-pipeline-in-apache-spark-and-python-ec3d12e2c169
* https://www.udacity.com/course/learn-spark-at-udacity--ud2002
* https://sparkbyexamples.com/spark/spark-dataframe-union-and-union-all/
* https://sparkbyexamples.com/spark/spark-read-csv-file-into-dataframe/
