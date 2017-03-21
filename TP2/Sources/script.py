from operator import add
from pyspark import SparkContext
import sys

spark = SparkContext(appName="WordCount")

text_file = spark.textFile("hdfs://localhost:9000/user/hduser/data_2.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://localhost:9000/user/hduser/iteration"+sys.argv[1])

