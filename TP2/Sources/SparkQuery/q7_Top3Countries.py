# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, desc

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("DistincMember").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    # Order by purchase count by country
    orderedByOrderByCountry = salesDataset.groupBy("country").agg(count("*").alias("count")).orderBy(desc("count"))

    orderedByOrderByCountry.show(3)
    # Answer: 
    #  1) CN (China) with 4623 orders
    #  1) ID (India) with 2695 orders
    #  1) RU (Russia) with 1415 orders



