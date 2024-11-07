from modules import *
spark = SparkSession.builder.appName("RandomUserAPI").getOrCreate()

# Function to fetch data from the API
def fetch_user_data_p(num_users):
    response = requests.get(f"https://randomuser.me/api/?results={num_users}")
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to create Spark DataFrame from fetched data
def create_spark_dataframe(num_users):
    data = fetch_user_data_p(num_users)
    
    if data:
        # Convert the list of dictionaries to an RDD
        rdd = spark.sparkContext.parallelize(data)
        
        # Convert RDD to DataFrame; PySpark will infer the schema automatically
        df = spark.read.json(rdd)
        return df
    else:
        # Return an empty DataFrame with an empty schema
        return spark.createDataFrame([], schema=None)

