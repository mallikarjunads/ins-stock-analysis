from modules import *


if __name__ == "__main__":
    num_users = 500  # Change this to the desired number of users
    user_dataframe = create_spark_dataframe(num_users)

user_dataframe.show()



user_dataframe.show()