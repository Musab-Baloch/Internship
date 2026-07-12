from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional

import matplotlib.pyplot as plt

from DATABASE import get_user_info, delete_user, create_user, edit_user_email, edit_user_password, edit_user_first_name, edit_user_last_name

app = FastAPI()

class User(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    password_new: Optional[str] = None
    email: Optional[str] = None
    email_new: Optional[str] = None


@app.get("/")
def root():
    return {"status" : "Successful"}

@app.get("/get-user_info/")
def get_info(user: User):
    info = get_user_info(user.first_name, user.last_name, user.password)
    return info

@app.delete("/delete-user/")
def delete_acct(user: User):
    return delete_user(user.first_name, user.last_name, user.password)


@app.post("/create-account/")
def create_acct(user: User):
    return create_user(user.first_name, user.last_name, user.email, user.password)


@app.put("/update-account/")
def update_acct(user: User):
    
    if user.first_name != None:
        return edit_user_first_name(user.password, user.first_name)

    if user.last_name != None:
        return edit_user_last_name(user.password, user.last_name)

    if user.password != None:
        return edit_user_password(user.password, user.password_new)

    if user.email != None:
        return edit_user_email(user.email, user.email_new)



def create_line_plot(x_axis_data, y_axis_data, x_axis_title, y_axis_title, plot_title, line_title):

    plt.figure(figsize=(8, 5)) 


    plt.plot(
        x_axis_data, 
        y_axis_data, 
        color="#1d6a7e",       
        linestyle="--",       
        linewidth=2.5,       
        marker="o",           
        markersize=8,         
        label= line_title  
    )

    plt.title(plot_title, fontsize=14, fontweight="bold")
    plt.xlabel(x_axis_title, fontsize=11)
    plt.ylabel(y_axis_title, fontsize=11)

    plt.grid(True, linestyle=":", alpha=0.6)  
    plt.legend(loc="upper left")             

    plt.close()
