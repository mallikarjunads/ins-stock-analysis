from modules import *
from api import *

# Main function to coordinate the fetching and DataFrame creation
def main(num_users):
    user_data = fetch_user_data(num_users)  # Fetch user data
    df = create_dataframe(user_data)  # Create DataFrame from user data
    return df

# Specify the number of users to fetch
num_users = 1500  # Change this to the desired number of users

# Run the main function and print the DataFrame
if __name__ == "__main__":
    user_dataframe = main(num_users)

# Combining the address fields into a single column
user_dataframe['address'] = user_dataframe.apply(
    lambda x: f"{x['location.street.number']} {x['location.street.name']}, {x['location.city']}, {x['location.state']}, {x['location.country']}", axis=1
)

# Selecting the required columns
user_dataframe = user_dataframe[["login.sha256", 'name.first', 'name.last', 'gender', 'address', 
                                 'location.postcode', 'email', 'login.username', 'dob.date', 
                                 'registered.date', 'phone', 'picture.thumbnail']]

# Renaming the columns
user_dataframe.columns = ["id", "first_name", "last_name", "gender", "address", "post_code", 
                          "email", 'username', "dob", "registered_date", "phone", "thumbnail"]

# Display the DataFrame
print(user_dataframe)


user_dataframe.to_csv("users_data.csv")