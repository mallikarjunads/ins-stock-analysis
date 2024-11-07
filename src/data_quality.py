import pandas as pd
import re
import great_expectations as g
df1=pd.read_csv("transform.csv")
print(df1)

df1["first_name"] = df1["first_name"].apply(lambda name: name.encode('utf-8').decode('unicode_escape'))

# Filter for names that contain only Latin alphabetic characters and spaces
df1 = df1[df1["first_name"].apply(lambda name: bool(re.match(r'^[A-Za-z\s]+$', name)))]

# Display the filtered DataFrame

print()
df1["last_name"] = df1["last_name"].apply(lambda name: name.encode('utf-8').decode('unicode_escape'))

# Filter for names that contain only Latin alphabetic characters and spaces
df1 = df1[df1["last_name"].apply(lambda name: bool(re.match(r'^[A-Za-z\s]+$', name)))]

# Ensure phone column is a string, then filter out rows with phone length between 10 and 15
# Convert phone column to string type to ensure proper length checking
df1["phone"] = df1["phone"].astype(str)


df1 = df1[(df1["phone"].str.len() >= 10) & (df1["phone"].str.len() <= 15)]

print(df1)

df1['dob'] = pd.to_datetime(df1['dob'],format="mixed").dt.strftime('%Y-%m-%d')
print(df1)


df1=df1[df1["post_code"].str.len() >=5]
print(df1)

print()
df1['address'] = df1['address'].apply(lambda x: re.sub(r'[^a-zA-Z,\s]', '', x))


print()
df1=df1[~df1['post_code'].str.contains('[^\d]', regex=True)]

df1['dob'] = pd.to_datetime(df1['dob'])

df1.info()
# Display the filtered DataFrame
print(df1["last_name"])
u=g.from_pandas(df1)

print()


df1.reset_index(drop=True, inplace=True)
df1.to_csv("quality.csv",index=False)