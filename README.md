# LSTM_Finance
Walks through the process of extracting finance data and running LSTM for prediction

This shows the step by step process for making a Lont Short Term Memory prediction in Python. This contains 4 Files. The first file [Total Process for Prediction](https://github.com/akniels/LSTM_Finance/blob/main/Total%20Process%20for%20Prediction.ipynb) shows the data ETL and prediction in a Jupyter Notebook. This file utilizes and walkthrough data cleansing in spark and predictions done in scikit learn. The second file [ETL_extraction](https://github.com/akniels/LSTM_Finance/blob/main/etl.py) extracts the data using the yfinance plugin using the [nasdaq_screener](https://github.com/akniels/LSTM_Finance/blob/main/nasdaq_screener.csv) in a pythonic object oriented way. The Nasdaq screeener can be found [here](https://www.nasdaq.com/market-activity/stocks/screener). The spark ETL cleans and prepares the data using spark for LSTM prediction in an object oriented way. The data is front filled for missing data and any data with null values are removed. Additional fields are added (7 and 20 day moving average and Bollinger™ bands and a five day lead close which is what we are trying to predict). Visualizations are created to show the the trend for PFG and AIG (Principal Financial Group and American International Group).The Data is then joined to the nasdaq screener to see if any coorelations exist with the sector and industry. Data is then transferred to pandas and prepared for machine learning with the min max scaler and then an LSTM is ran for prediction.

## Blog Posts

Here are the blog posts that walk through the data engineering and Machine learning process. 

* [Finance Predictions: Part 1](https://datasciencetipsandtricks.com/?p=299)
* [Finance Predictions: Part 2](https://datasciencetipsandtricks.com/?p=312)
* [Finance Predictions: Part 3](https://datasciencetipsandtricks.com/?p=324)

## Acknowledgements
Yfinance code examples
* https://github.com/ranaroussi/yfinance

Spark Code examples
* https://towardsdatascience.com/create-your-first-etl-pipeline-in-apache-spark-and-python-ec3d12e2c169
* https://www.udacity.com/course/learn-spark-at-udacity--ud2002
* https://sparkbyexamples.com/spark/spark-dataframe-union-and-union-all/
* https://sparkbyexamples.com/spark/spark-read-csv-file-into-dataframe/
* https://stackoverflow.com/questions/54489344/apply-a-function-to-all-cells-in-spark-dataframe
* https://sparkbyexamples.com/spark/spark-add-new-column-to-dataframe/
* https://sparkbyexamples.com/spark/spark-sql-distinct-multiple-columns/#:~:text=Spark%20doesn't%20have%20a,DataFrame%20with%20duplicate%20rows%20removed
* https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html
* https://stackoverflow.com/questions/43114445/how-to-use-first-and-last-function-in-pyspark
* https://sparkbyexamples.com/spark/spark-sql-aggregate-functions/
* https://stackoverflow.com/questions/40671206/using-spark-dataframe-and-window-functions-to-calculate-the-rolling-average-retu
* https://stackoverflow.com/questions/36725353/applying-a-window-function-to-calculate-differences-in-pyspark
* https://riptutorial.com/apache-spark/example/22861/window-functions---sort--lead--lag---rank---trend-analysis
* https://docs.azuredatabricks.net/_static/notebooks/gbt-regression.html

Plotly
* https://plotly.com/python/ipython-notebook-tutorial/
* https://plotly.com/python/line-charts/

