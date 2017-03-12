# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession
from pyspark.sql import functions

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("SparkQuery").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    pattern = "yyyy-MM-dd"

    # Converting to unix timestamp for ordering
    convertedDataset = salesDataset.withColumn("timestampDate", functions.unix_timestamp("date", pattern).cast("timestamp"))
    
    # Order the dataset
    sortedDate = convertedDataset.orderBy("timestampDate")

    # Get the first purchase
    sortedDate.select("date").show(1)
    # Answer = 2007-12-02




