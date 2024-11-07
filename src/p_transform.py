from modules  import *

# Read CSV into Spark DataFrame
user_dataframe = spark.read.csv("users_data.csv", header=True, inferSchema=True)

user_dataframe = user_dataframe.withColumn("dob", to_date(col("dob")))

today = current_date()

user_dataframe = user_dataframe.withColumn(
    "age",
    (year(today) - year(col("dob"))) - 
    ((month(today) < month(col("dob"))).cast(IntegerType())) - 
    (((month(today) == month(col("dob"))) & (dayofmonth(today) < dayofmonth(col("dob")))).cast(IntegerType()))
)

# Clean phone numbers by removing non-numeric characters
user_dataframe = user_dataframe.withColumn("cleaned_Phone", regexp_replace(col("phone"), r"\D", ""))
user_dataframe = user_dataframe.drop("phone").withColumnRenamed("cleaned_Phone", "phone")

# Filter users by age (20 < age < 40)
user_dataframe = user_dataframe.filter((col("age") > 20) & (col("age") < 40))

# Replace 'example.com' with 'email.com' in email addresses
user_dataframe = user_dataframe.withColumn("email", regexp_replace(col("email"), "example.com", "email.com"))

# Convert 'registered_date' to TimestampType and apply timezone conversions
user_dataframe = user_dataframe.withColumn("registered_date", to_timestamp(col("registered_date")))


shape=user_dataframe.count(),len(user_dataframe.columns)

print(shape)



