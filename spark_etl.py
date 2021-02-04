#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:46:53 2021

@author: akniels1
"""
import findspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import desc, stddev_samp, stddev_pop
from pyspark.sql.functions import asc, col,avg, last
from pyspark.sql.functions import sum as Fsum
import pandas as pd
from pyspark.sql.window import Window
import sys


## Initialize a class for the fin_dataet
class fin_data:
    def __init__(self, list_of_csv = ["nasdaq.csv"] ):
        self._list_of_csv = list_of_csv
    
## initialize spark
    def initspark(self):
        spark = SparkSession \
            .builder \
            .appName("Python Fin Data") \
            .config("local") \
            .getOrCreate()
        return spark
## Read data from csv to spark dataframes         
    def read_csv_to_spark(self, spark):
        list_of_spark =  []
        names_of_tables = []
        for item in self._list_of_csv:
            names_of_tables.append(str(item[:-4]))
            app =  spark.read.format("csv").option("header", "true").load(item)
            list_of_spark.append( app )
        return list_of_spark, names_of_tables
    
## union the data together
    
    def Spark_union(self,sprk_list, table_names, spark):
        spark_string = ''
        for i in range(len(sprk_list)):
            sprk_list[i].createOrReplaceTempView(table_names[i])
            if i == (len(sprk_list)-1):
                spark_string += 'Select * from '+ table_names[i]
            else:
                spark_string +='Select * from '+ table_names[i]+ ' Union All '
        
        union_all = spark.sql(spark_string)
        return union_all
 ## fron fill the data and remove any NAN values   
    def ffill_and_remove(self, sparktable):
        # define the window
        window = Window.partitionBy('ticker')\
                       .orderBy('Date')\
                       .rowsBetween(-sys.maxsize, 0)

        # define the forward-filled column
        clean_open = last(sparktable['Open'], ignorenulls=True).over(window)
        clean_high = last(sparktable['High'], ignorenulls=True).over(window)
        clean_low = last(sparktable['Low'], ignorenulls=True).over(window)
        clean_close = last(sparktable['Close'], ignorenulls=True).over(window)
        clean_adj_close = last(sparktable['Adj Close'], ignorenulls=True).over(window)
        clean_volume = last(sparktable['Volume'], ignorenulls=True).over(window)

        # do the fill
        spark_df_filled = sparktable.withColumn('Open', clean_open)
        spark_df_filled = spark_df_filled.withColumn('High', clean_high)
        spark_df_filled = spark_df_filled.withColumn('Low', clean_low)
        spark_df_filled = spark_df_filled.withColumn('Close', clean_close)
        spark_df_filled = spark_df_filled.withColumn('Adj Close', clean_adj_close)
        spark_df_filled = spark_df_filled.withColumn('Volume', clean_volume)

        #remove items that are blank (beforestock inception)
        
        spark_df_filled.na.drop('any')
        
        return spark_df_filled




        
    
    def add_additional_fields(self,table):
        days = lambda i: i * 86400

        
        windowSpec = Window.partitionBy("ticker").orderBy(col("Date").cast('long')).rangeBetween(-days(7), 0)
        
        windowSpec20 = Window.partitionBy("ticker").orderBy(col("Date").cast('long')).rangeBetween(-days(20), 0)
        
        
        union_table = table.withColumn('rolling_seven_day_average', avg("Close").over(windowSpec)) 
        
        union_table = union_table.withColumn('rolling_20_day_average', avg("Close").over(windowSpec20)) 
        
        union_table = union_table.withColumn('stdev', stddev_pop("Close").over(windowSpec20))
        
        union_table = union_table.withColumn('Upper', union_table['rolling_20_day_average'] + (union_table['stdev']*2) )
        
        union_table = union_table.withColumn('Lower', union_table['rolling_20_day_average'] - (union_table['stdev']*2) )
        
        return union_table
    
    def get_distinct_tickers(self, sparkframe):
         
        
        return [i.ticker for i in sparkframe.select('ticker').distinct().collect()]
        
if __name__ == "__main__":
    fin = fin_data()    
    spark = fin.initspark()   
    list_spark , table_name = fin.read_csv_to_spark(spark)
    union_all = fin.Spark_union(list_spark, table_name,spark)
    clean_data = fin.ffill_and_remove(union_all)
    final_dataset = fin.add_additional_fields(clean_data)
    distinct_tickers = fin.get_distinct_tickers(final_dataset)