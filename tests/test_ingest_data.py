import unittest

import pandas as pd
from pyspark.sql import SparkSession

from data_ingestion.ingest_data import create_spark_dataframe, load_data


class TestDataIngestion(unittest.TestCase):
    def test_load_data(self):
        """
        Test to check if load_data returns the expected Pandas DataFrame.
        """
        df = load_data()

        # Check if the result is a DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # Check the DataFrame shape
        self.assertEqual(df.shape, (3, 2))  # 3 rows, 2 columns

        # Check the content of the DataFrame verify
        expected_data = {"Name": ["Alice", "Bob", "Cathy"], "Age": [25, 30, 22]}
        pd.testing.assert_frame_equal(df, pd.DataFrame(expected_data))

    def test_create_spark_dataframe(self):
        """
        Test to check if create_spark_dataframe returns the expected PySpark DataFrame.
        """
        # Create a Spark session (if not already active)
        spark = (
            SparkSession.builder.master("local").appName("PySpark Test").getOrCreate()
        )

        # Call the function to test
        df = create_spark_dataframe()

        # Check if the result is a PySpark DataFrame
        self.assertEqual(df.count(), 3)  # Check number of rows
        self.assertEqual(len(df.columns), 2)  # Check number of columns

        # Check the content of the DataFrame
        expected_data = [("Alice", 25), ("Bob", 30), ("Cathy", 22)]
        expected_df = spark.createDataFrame(expected_data, ["Name", "Age"])
        self.assertEqual(df.collect(), expected_df.collect())  # Compare data


if __name__ == "__main__":
    unittest.main()
