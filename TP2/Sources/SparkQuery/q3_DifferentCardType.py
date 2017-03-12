# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("DistincMember").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    # Count distinc card (alternative way to do)
    count = salesDataset.select("card_type").distinct().count()

    print("Distinct card type: " + str(count))
    # Answer = 16




