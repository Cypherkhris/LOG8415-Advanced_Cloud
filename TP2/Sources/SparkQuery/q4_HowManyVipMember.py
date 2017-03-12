# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("SparkQuery").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    # Count the number of distinc member who is VIP
    # TODO: Is a user always VIP??? (doesn't seem so because number of not VIP is 2489)
    count = salesDataset.where((col("vip") == "true")).select("member_id").distinct().count()

    print("Distinct vip: " + str(count))
    # Answer = 2486




