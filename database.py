import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta
import os


# Load the environment variables
DETA_KEY = "c0z11a89_vEzHeMyetF1sjuNYX8HVLfhDPJn8QeXS"


# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("User_Login_details")
db2 = deta.Base("Admission_form_details")


def insert_login_details(name, username, password):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"Name": name, "Username": username, "Password": password})

def insert_student_details(f_name,m_name,l_name,email_id,phone_no,caste,math_marks,percentage,result_id,
                           address):
    return db2.put({"First Name":f_name, "Middle Name":m_name, "Last Name":l_name, "Email ID":email_id,
                  "Phone":phone_no, "Caste":caste, "Maths Marks":math_marks,
                  "Percentage":percentage, "Result ID":result_id, "Address":address})


def fetch_all_details():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_details(period):
    """If not found, the function will return None"""
    return db.get(period)

