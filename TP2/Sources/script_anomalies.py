from pyspark.sql.functions import regexp_extract
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkAnomalies").getOrCreate()

data = spark.read.option("header","true").csv("data_dump.csv")

## member_id
r = data.select(regexp_extract('member_id', '[0-9]{6}', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## date
r = data.select(regexp_extract('date', '[0-9]{4}-[0-9]{2}-[0-9]{2}', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## country
r = data.select(regexp_extract('country', '([A-Z]{2})', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## gender
r = data.select(regexp_extract('gender', '(Male|Female)', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## ip_address
r = data.select(regexp_extract('ip_address', '(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(25[0-4]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## amount
r = data.select(regexp_extract('amount', '(([1-9]?[0-9])*(,))*([1-9]?[0-9]*)\.[0-9]{2}', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## vip
r = data.select(regexp_extract('vip', 'true|false', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## product_id
r = data.select(regexp_extract('product_id', '[0-9]{6}', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## card_type
r = data.select(regexp_extract('card_type', '[a-z]+(-[a-z]+)*', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## serial
r = data.select(regexp_extract('serial', '[0-9]{3}-[0-9]{2}-[0-9]{4}', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()

## zone
r = data.select(regexp_extract('zone', 'zone[1-9][0-9]*', 0).alias('regex'))
r2 = r.withColumn('index', monotonically_increasing_id())
anomalies = r2.filter(r2.regex == '')
anomalies.show()
