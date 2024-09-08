# Import the functions from the data_ingestion module
from data_ingestion.ingest_data import create_spark_dataframe, load_data

# Call the Pandas function and display the DataFrame
df_pandas = load_data()
print("Pandas Data Ingested:")
print(df_pandas)

# Call the PySpark function and display the DataFrame
df_spark = create_spark_dataframe()
print("PySpark DataFrame Ingested:")
df_spark.show()
