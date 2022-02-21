# Databricks notebook source
#GLUE JOB TEST TO LOAD DATA FROM DATA CATALOG AND TRANSFORM DATA AND LOAD DATA INTO S3 AS CVS FORMAT

# IMPORTS
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

#SESSION CREATION
spark_context = SparkContext.getOrCreate()
glue_context = GlueContext(spark_context)
session = glue_context.spark_session

#VARIABLE DECLARATION
glue_db = "virtual"
glue_tbl = "input"
s3_write_path = "s3://glue-demo-de/output"

#READING DATA FROM DATA CATALOG
dynamic_frame_read = glue_context.create_dynamic_frame.from_catalog(database=glue_db, table_name=glue_tbl)
df = dynamic_frame_read.toDF()

#DATA TRANSFORMATION
df_transformed = df.groupBy("Industry_code_NZSIOC").count().sort("Industry_code_NZSIOC")

#CONVERTING BACK TO DYNAMIC FRAMES
df_transformed = df_transformed.repartition(1)
dynamic_frame_write = DynamicFrame.fromDF(df_transformed, glue_context, "data_frame_transformed")

#WRITING DATA BACK TO S3
glue_context.write_dynamic_frame.from_options(
    frame = dynamic_frame_write,
    connection_type = "s3",
    connection_options = {
      "path":s3_write_path
    },
    format = "csv"
)

# COMMAND ----------


