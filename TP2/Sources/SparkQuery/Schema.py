# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("SparkSchema").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    salesDataset.printSchema()

    '''
        root
        |-- member_id: string (nullable = true)
        |-- date: string (nullable = true)
        |-- country: string (nullable = true)
        |-- gender: string (nullable = true)
        |-- ip_address: string (nullable = true)
        |-- amount: string (nullable = true)
        |-- vip: string (nullable = true)
        |-- product_id: string (nullable = true)
        |-- card_type: string (nullable = true)
        |-- serial: string (nullable = true)
        |-- zone: string (nullable = true)
    '''




