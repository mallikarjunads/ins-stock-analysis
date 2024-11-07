from modules import *


#read dataframe
user_dataframe=pd.read_csv("users_data.csv")

# Calculate the current age based on the 'dob' column
user_dataframe['dob'] = pd.to_datetime(user_dataframe['dob'])
user_dataframe['registered_date'] = pd.to_datetime(user_dataframe['registered_date'])

today = pd.Timestamp(datetime.now().date())  # Get today's date
user_dataframe['age'] = user_dataframe['dob'].apply(lambda x: today.year - x.year - ((today.month, today.day) < (x.month, x.day)))

# Display the first few rows of the DataFrame with the new 'age' column

user_dataframe=user_dataframe.drop("Unnamed: 0",axis=1)
# Save the DataFrame to a CSV file
user_dataframe.to_csv("users_data_transform.csv")



print(user_dataframe["phone"].unique())

user_dataframe['cleaned_Phone'] = user_dataframe['phone'].str.replace(r'\D', '', regex=True)

print(user_dataframe["cleaned_Phone"].unique())

user_dataframe.drop(["phone"],axis=1,inplace=True)

user_dataframe.rename(columns={"cleaned_Phone":"phone"},inplace=True)
print(user_dataframe.columns)


user_dataframe=user_dataframe.query("age>20 and age <40")




user_dataframe["email"]=user_dataframe["email"].replace({"example.com":"email.com"},regex=True)
print()
print(user_dataframe["email"].unique())
print()
print(user_dataframe["registered_date"])

user_dataframe['registered_date'] = pd.to_datetime(user_dataframe['registered_date']).dt.tz_convert('UTC')

# Convert to Indian Standard Time (IST)
user_dataframe['registered_date'] = user_dataframe['registered_date'].dt.tz_convert('Asia/Kolkata')

print(user_dataframe)
user_dataframe.reset_index(drop=True, inplace=True)

user_dataframe.to_csv("transform.csv",index=False)

