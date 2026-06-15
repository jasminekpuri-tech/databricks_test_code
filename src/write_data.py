# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Start the Spark engine
spark = SparkSession.builder.getOrCreate()

# Define the structure of the data
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

# Create the data rows in memory
data = [(1, "Bundle_Test_1"), (2, "Bundle_Test_2")]
df = spark.createDataFrame(data, schema)

# FIX: Write directly to a DBFS file path instead of a Metastore table
df.write.format("delta").mode("overwrite").save("dbfs:/tmp/github_bundle_test_data")
print("Data written successfully directly to DBFS path!")

