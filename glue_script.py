import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, trim, upper, to_date, when

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# ===== ADD THIS PART IN MIDDLE =====
# READ from S3 Staging
df = spark.read.option("header", "true").option("inferSchema", "true").csv("s3://smartcare-staging-akash/patients.csv")

# CLEANING
df_clean = df.dropDuplicates()
df_clean = df_clean.filter(col("patient_id").isNotNull() & col("department").isNotNull())
df_clean = df_clean.withColumn("department", upper(trim(col("department"))))
df_clean = df_clean.withColumn("gender", upper(trim(col("gender"))))
df_clean = df_clean.withColumn("visit_date", to_date(col("visit_date"), "yyyy-MM-dd"))
df_clean = df_clean.withColumn("fees", when(col("fees").isNull() | (col("fees") < 0), 0).otherwise(col("fees")))

# WRITE to S3 DW
df_clean.write.mode("overwrite").option("header", "true").csv("s3://smartcare-dw-akash/cleaned/")
# ===== END =====

job.commit()