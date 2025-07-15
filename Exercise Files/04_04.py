##import required libraries
import pyspark
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DB_URL = os.getenv('DB_URL')

##create spark session
spark = pyspark.sql.SparkSession \
   .builder \
   .appName("Python Spark SQL basic example") \
   .config('spark.driver.extraClassPath', "C:/Users/Admin/Downloads/postgresql-42.2.18.jar") \
   .getOrCreate()


##read table from db using spark jdbc
##read table from db using spark jdbc
movies_df = spark.read \
   .format("jdbc") \
   .option("url", DB_URL) \
   .option("dbtable", "movies") \
   .option("user", USER) \
   .option("password", PASSWORD) \
   .option("driver", "org.postgresql.Driver") \
   .load()
   
##add code below
user_df = spark.read \
   .format("jdbc") \
   .option("url", DB_URL) \
   .option("dbtable", "users") \
   .option("user", USER) \
   .option("password", PASSWORD) \
   .option("driver", "org.postgresql.Driver") \
   .load()

##print the users dataframe
print(user_df.show())




