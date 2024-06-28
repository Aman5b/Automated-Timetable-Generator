# ---- IMPORT LIBRARIES

import streamlit as st
import pandas as pd
import base64
import subprocess

# --------------- BACKGROUND IMAGE

st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Automatic Time Table Generator"}</h1>', unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local('1.jpg')

# ==== Title

typee = st.selectbox('CHOOSE HERE ', ('HOME', 'ADMIN', 'FACULTY', 'STUDENT'))    

if typee == "HOME":
    st.markdown(f'<h1 style="color:#000000;font-size:24px;text-align:center">{" Welcome to our Page !!! "}</h1>', unsafe_allow_html=True)

if typee == "ADMIN":
    st.success("Welcome Admin!!!")
    
    adname = st.text_input("Enter Name", "Name", key="admin_name")
    passs = st.text_input("Enter Password", "Password", type="password", key="admin_password")
    aa = st.button("Submit", key="admin_submit")
    
    if adname == "Admin" and passs == "12345":
        st.success("Admin Login Successfully !!!")    
        subprocess.run(['python', '-m', 'streamlit', 'run', 'Upd3.py'])

if typee == "FACULTY":
    st.success("Welcome Faculty!!!")
    
    fac_name = st.text_input("Enter Faculty Name", "Faculty", key="faculty_name")
    passs1 = st.text_input("Enter Faculty Password", "Faculty Password", type="password", key="faculty_password")
    aa = st.button("Submit", key="faculty_submit")
    
    if fac_name == "faculty" and passs1 == "12345":
        st.success("Faculty Login Successfully !!!")    
        subprocess.run(['python', '-m','streamlit', 'run', 'View.py'])

if typee == "STUDENT":    
    subprocess.run(['python', '-m','streamlit', 'run', 'TimeTable.py'])
    
    # ================================= IMPORT PACKAGES ===============================


    # import streamlit as st

    # import base64

    # import sqlite3

    # # ================ Background image ===

    # st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Automatic Time Table Generator"}</h1>', unsafe_allow_html=True)


    # def add_bg_from_local(image_file):
    #     with open(image_file, "rb") as image_file:
    #         encoded_string = base64.b64encode(image_file.read())
    #     st.markdown(
    #     f"""
    #     <style>
    #     .stApp {{
    #         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
    #         background-size: cover
    #     }}
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    #     )
    # add_bg_from_local('1.jpg')




    # import streamlit as st
    # import sqlite3
    # import re

    # # Function to create a database connection
    # def create_connection(db_file):
    #     conn = None
    #     try:
    #         conn = sqlite3.connect(db_file)
    #     except sqlite3.Error as e:
    #         print(e)
    #     return conn

    # # Function to create a new user
    # def create_user(conn, user):
    #     sql = ''' INSERT INTO users(name, password, email, phone)
    #               VALUES(?,?,?,?) '''
    #     cur = conn.cursor()
    #     cur.execute(sql, user)
    #     conn.commit()
    #     return cur.lastrowid

    # # Function to check if a user already exists
    # def user_exists(conn, email):
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM users WHERE email=?", (email,))
    #     if cur.fetchone():
    #         return True
    #     return False

    # # Function to validate email
    # def validate_email(email):
    #     pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    #     return re.match(pattern, email)

    # # Function to validate phone number
    # def validate_phone(phone):
    #     pattern = r'^[6-9]\d{9}$'
    #     return re.match(pattern, phone)

    # # Main function
    # def main():
    #     # st.title("User Registration")

    #     # Create a database connection
    #     conn = create_connection("dbs.db")

    #     if conn is not None:
    #         # Create users table if it doesn't exist
    #         conn.execute('''CREATE TABLE IF NOT EXISTS users
    #                      (id INTEGER PRIMARY KEY,
    #                      name TEXT NOT NULL,
    #                      password TEXT NOT NULL,
    #                      email TEXT NOT NULL UNIQUE,
    #                      phone TEXT NOT NULL);''')

    #         # User input fields
    #         name = st.text_input("Enter your name")
    #         password = st.text_input("Enter your password", type="password")
    #         confirm_password = st.text_input("Confirm your password", type="password")
    #         email = st.text_input("Enter your email")
    #         phone = st.text_input("Enter your phone number")

    #         col1, col2 = st.columns(2)

    #         with col1:
                    
    #             aa = st.button("REGISTER")
                
    #             if aa:
                    
    #                 if password == confirm_password:
    #                     if not user_exists(conn, email):
    #                         if validate_email(email) and validate_phone(phone):
    #                             user = (name, password, email, phone)
    #                             create_user(conn, user)
    #                             st.success("User registered successfully!")
    #                         else:
    #                             st.error("Invalid email or phone number!")
    #                     else:
    #                         st.error("User with this email already exists!")
    #                 else:
    #                     st.error("Passwords do not match!")
                    
    #                 conn.close()

    #         with col2:
                    
    #             aa = st.button("LOGIN")
                
    #             if aa:
    #                 import subprocess
    #                 subprocess.run(['streamlit','run','login.py'])
    #                 st.success('Successfully Registered !!!')


    # if __name__ == '__main__':
    #     main()



