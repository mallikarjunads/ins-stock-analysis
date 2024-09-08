import pandas as pd
from pyspark.sql import SparkSession


def load_data():
    """
    Function to create a Pandas DataFrame from a dictionary.

    Returns:
        pd.DataFrame: A DataFrame with example data.
    """
    data = {"Name": ["Alice", "Bob", "Cathy"], "Age": [25, 30, 22]}

    df = pd.DataFrame(data)
    return df


def create_spark_dataframe():
    """
    Function to create a simple PySpark DataFrame.

    Returns:
        pyspark.sql.DataFrame: A PySpark DataFrame.
    """
    # Initialize a Spark session
    spark = SparkSession.builder.appName("PySpark Test").getOrCreate()

    # Example data
    data = [("Alice", 25), ("Bob", 30), ("Cathy", 22)]
    columns = ["Name", "Age"]

    # Create a PySpark DataFrame
    df = spark.createDataFrame(data, columns)

    return df
