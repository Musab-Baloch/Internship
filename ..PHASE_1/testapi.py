# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:11:47 2026

@author: Musab Baloch
"""

from fastapi import FastAPI

app = FastAPI()

# GET
# POST
# PUT
# DELETE

@app.get("/")
def root():
    return {"status" : "Successful Hermano"}

@app.delete("/delete_account")
def delete_acct():
    pass

@app.post("/create-account")
def create_acct():
    return {"name" : "Hermano"}


