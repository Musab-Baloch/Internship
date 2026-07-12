import sqlite3


connect = sqlite3.connect("UserData.db")
curr = connect.cursor()

# Column structure in the USERS table:
# FIRST_NAME, LAST_NAME, EMAIL, PASSWORD


def create_user(first_name: str, last_name: str, email: str, password: str):
    
    curr.execute(
        "INSERT INTO Users(FIRST_NAME, LAST_NAME, EMAIL, PASSWORD) VALUES(?, ?, ?, ?)", 
        (first_name, last_name, email, password)
    )
    connect.commit() 
    return {"Status": "Action Successful"}


def get_user_info(first_name: str, last_name: str, password: str):

    curr.execute(
        "SELECT * FROM Users WHERE FIRST_NAME = ? AND LAST_NAME = ? AND PASSWORD = ?", 
        (first_name, last_name, password)
    )
    return curr.fetchall()


def edit_user_email(email_old: str, email_new: str):

    curr.execute(
        "UPDATE Users SET EMAIL = ? WHERE EMAIL = ?", 
        (email_new, email_old)
    )
    connect.commit() 
    return {"Status": "Action Successful"}


def edit_user_first_name(password: str, first_name_new: str):

    curr.execute(
        "UPDATE Users SET FIRST_NAME = ? WHERE PASSWORD = ?", 
        (first_name_new, password)
    )
    connect.commit()
    return {"Status": "Action Successful"}


def edit_user_last_name(password: str, last_name_new: str):

    curr.execute(
        "UPDATE Users SET LAST_NAME = ? WHERE PASSWORD = ?", 
        (last_name_new, password)
    )
    connect.commit()
    return {"Status": "Action Successful"}


def edit_user_password(password_old: str, password_new: str):

    curr.execute(
        "UPDATE Users SET PASSWORD = ? WHERE PASSWORD = ?", 
        (password_new, password_old)
    )
    connect.commit()
    return {"Status": "Action Successful"}


def delete_user(first_name: str, last_name: str, password: str):

    curr.execute(
        "DELETE FROM Users WHERE FIRST_NAME = ? AND LAST_NAME = ? AND PASSWORD = ?", 
        (first_name, last_name, password)
    )
    connect.commit() 
    return {"Status": "Action Successful"}