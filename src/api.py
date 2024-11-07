from modules import *
from api import *

# Function to fetch data from the API
def fetch_user_data(num_users):
    response = requests.get(f"https://randomuser.me/api/?results={num_users}")
    if response.status_code == 200:
        
        return response.json()['results']
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to normalize data into a DataFrame
def create_dataframe(data):
    if data:
        df = pd.json_normalize(data)  # Flatten the JSON data into a DataFrame
        return df
    else:
        return pd.DataFrame()  # Return an empty DataFrame if no data