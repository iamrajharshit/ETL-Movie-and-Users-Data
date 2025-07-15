##import required libraries
import pyspark.sql
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

##read movies table from db using spark
##read table from db using spark jdbc
movies_df = spark.read \
   .format("jdbc") \
   .option("url", DB_URL) \
   .option("dbtable", "movies") \
   .option("user", USER) \
   .option("password", PASSWORD) \
   .option("driver", "org.postgresql.Driver") \
   .load()

##read users table from db using spark
users_df = spark.read \
    .format("jdbc") \
    .option("url", DB_URL) \
    .option("dbtable", "users") \
    .option("user", USER) \
    .option("password", PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()

## transforming tables
avg_rating = users_df.groupBy("movie_id").mean("rating")

##join the movies_df and avg_ratings table on id
df = movies_df.join(avg_rating, movies_df.id == avg_rating.movie_id)


##print all the tables/dataframes
print(movies_df.show())
print(users_df.show())
print(df.show())





