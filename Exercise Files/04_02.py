##import required libraries
import pyspark
from dotenv import load_dotenv
import os

##create spark session
spark = pyspark.sql.SparkSession \
   .builder \
   .appName("Python Spark SQL basic example") \
   .config('spark.driver.extraClassPath', "C:/Users/Admin/Downloads/postgresql-42.2.18.jar") \
   .getOrCreate()

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DB_URL = os.getenv('DB_URL')


##read table from db using spark jdbc
movies_df = spark.read \
   .format("jdbc") \
   .option("url", DB_URL) \
   .option("dbtable", "movies") \
   .option("user", USER) \
   .option("password", PASSWORD) \
   .option("driver", "org.postgresql.Driver") \
   .load()

##print the movies_df
print(movies_df.show())





