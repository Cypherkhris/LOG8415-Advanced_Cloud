# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("SparkQuery").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    # Find max price
    orderedByPrice = salesDataset.orderBy(desc("amount")).select("product_id", "amount")

    orderedByPrice.show(1)
    # Answer: id: 330092 at 9999.87$



