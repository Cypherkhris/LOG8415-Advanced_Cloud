# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("SparkQuery").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    # Count of specific purchaser
    count = salesDataset.where(
        (col("country") == "CA") & 
        (col("gender") == "Female") & 
        (col("zone") == "zone7")
        ).select("member_id").distinct().count()

    print("Distinct Canadian female members who purchased an item from Zone7: " + str(count))
    # Answer = 16




