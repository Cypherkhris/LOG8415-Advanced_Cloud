# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("SparkQuery").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    # Get latest order of every member
    latestOrderDateByMember = salesDataset.groupBy("member_id").agg(max("date").alias("date"))
    latestORderByMember = salesDataset.join(latestOrderDateByMember, ["member_id", "date"])

    # Count the number of distinc member who is VIP
    count = latestORderByMember.where((col("vip") == "true")).select("member_id").distinct().count()

    print("Distinct vip: " + str(count))
    # Answer = 1245




