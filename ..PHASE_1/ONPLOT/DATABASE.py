import sqlite3

connect = sqlite3.connect("UserData.db")

curr = connect.cursor()

# Column structure in the USERS table;
# FIRST_NAME, LAST_NAME, EMAIL, PASSWORD


def create_user(first_name: str, last_name: str, email: str, password: str ):
    curr.execute("INSERT INTO Users(FIRST_NAME, LAST_NAME, EMAIL, PASSWORD) VALUES(first_name, last_name, email, password)")

    return {"Status" : "Action Successful"}

def get_user_info(first_name: str, last_name: str):

    pass

def edit_user_info(first_name: str, lastname: str, password: str):

    pass

def delete_user(first_name: str, last_name: str):
    pass
