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

# Write directly to the local EC2 node storage
local_path = "file:/tmp/github_bundle_test_data"
df.write.format("delta").mode("overwrite").save(local_path)
print("Data written successfully directly to local EC2 driver node storage!")

# -------------------------------------------------------------
# NEW CODE: Read it back and print it out to see the output!
# -------------------------------------------------------------
print("Reading data back from local disk to verify:")
read_back_df = spark.read.format("delta").load(local_path)
read_back_df.show()

