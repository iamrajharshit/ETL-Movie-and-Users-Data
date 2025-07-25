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
def extract_movies_to_df():
    ##read table from db using spark jdbc
    movies_df = spark.read \
    .format("jdbc") \
    .option("url", DB_URL) \
    .option("dbtable", "movies") \
    .option("user", USER) \
    .option("password", PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()
    return movies_df

##read users table from db using spark
def extract_users_to_df():
    ##read table from db using spark jdbc
    users_df = spark.read \
    .format("jdbc") \
    .option("url", DB_URL) \
    .option("dbtable", "users") \
    .option("user", USER) \
    .option("password", PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()
    return users_df


def transform_avg_ratings(movies_df, users_df):
    ## transforming tables
    avg_rating = users_df.groupBy("movie_id").mean("rating")
    df = movies_df.join(
    avg_rating,
    movies_df.id == avg_rating.movie_id
    )
    df = df.drop("movie_id")
    return df


##load transformed dataframe to the database
def load_df_to_db(df):
    mode = "overwrite"
    url = DB_URL
    properties = {"user": USER,
                  "password": PASSWORD,
                  "driver": "org.postgresql.Driver"
                  }
    df.write.jdbc(url=url,
                  table = "avg_ratings",
                  mode = mode,
                  properties = properties)



if __name__ == "__main__":
    movies_df = extract_movies_to_df()
    users_df = extract_users_to_df()
    ##pass the dataframes to the transformation function
    ratings_df = transform_avg_ratings(movies_df, users_df)
    ##load the ratings dataframe 
    load_df_to_db(ratings_df)

