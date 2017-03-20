# Comprend un SparkSession mais aussi SparkContext que avant
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc, sum

if __name__ == "__main__": 

    spark = SparkSession.builder.appName("SparkQuery").getOrCreate()

    # Convert data to Spark Dataset
    salesDataset = spark.read.option("header","true").csv("hdfs:////user/maria_dev/tp-data/data_dump.csv")

    # Convert column to float
    saledDatasetConverted = salesDataset.withColumn("intAmount", salesDataset.amount.cast("float") )

    # Sum command valur for each product
    sumByProduct = saledDatasetConverted.groupBy("product_id").agg(sum("intAmount").alias("sum"))

    # Order by sum
    highestSum = sumByProduct.orderBy(desc("sum")).select("product_id", "sum")

    highestSum.show(1)
    # Answer: id: 330111 at 1 559 315.79$



