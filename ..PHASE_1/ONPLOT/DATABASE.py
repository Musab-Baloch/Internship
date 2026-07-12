import sqlite3

connect = sqlite3.connect("UserData.db")

curr = connect.cursor()

# Column structure in the USERS table;
# FIRST_NAME, LAST_NAME, EMAIL, PASSWORD


def create_user(first_name: str, last_name: str, email: str, password: str ):
    curr.execute("INSERT INTO Users(FIRST_NAME, LAST_NAME, EMAIL, PASSWORD) VALUES(first_name, last_name, email, password)")

    return {"Status" : "Action Successful"}

def get_user_info(first_name: str, lastname: str, password: str):
    curr.execute("SELECT * FROM Users WHERE FIRST_NAME = first_name AND LAST_NAME = last_name AND PASSWORD = password ")
    return curr.fetchall()


def edit_user_email(email_old : str, email_new : str):

    curr.execute("""
            UPDATE Users SET EMAIL = email_new
            WHERE EMAIL = email_old
             
             """)
    return {"Status" : "Action Successful"}

def edit_user_first_name(password : str, first_name_new : str):

    curr.execute("""
            UPDATE Users SET FIRST_NAME = first_name_new
            WHERE PASSWORD = password
             
             """)
    return {"Status" : "Action Successful"}

def edit_user_last_name(password : str, last_name_new : str):

    curr.execute("""
            UPDATE Users SET LAST_NAME = last_name_new
            WHERE PASSWORD = password
             
             """)
    return {"Status" : "Action Successful"}

def edit_user_password(password_old : str, password_new : str):

    curr.execute("""
            UPDATE Users SET PASSWORD = password_new
            WHERE PASSWORD = password_old
             
             """)
    return {"Status" : "Action Successful"}

def delete_user(first_name: str, lastname: str, password: str):
    curr.execute("DELETE from Users WHERE FIRST_NAME = first_name AND LAST_NAME = last_name AND PASSWORD = password ")
    return {"Status" : "Action Successful"}
