# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession
from pyspark.sql import functions

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("DistincMember").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    # Count distinc member
    count = salesDataset.agg(functions.countDistinct("member_id"))

    count.show()
    # Answer = 2500




