# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Start the Spark engine on the EC2 instance
spark = SparkSession.builder.getOrCreate()

# Define the structure of the data
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

# Create the data rows in memory
data = [(1, "Bundle_Test_1"), (2, "Bundle_Test_2")]
df = spark.createDataFrame(data, schema)

# Write out to the default managed table area
df.write.format("delta").mode("overwrite").saveAsTable("default.github_bundle_test")
print("Managed table written successfully via the DAB!")

