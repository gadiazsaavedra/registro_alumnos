"""import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

import sqlite3
import random"""
##### model.py #######
import sqlite3


def create_table():
    conn = sqlite3.connect("data.db")
    table_create_query = """CREATE TABLE IF NOT EXISTS Student_Data 
            (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
            registration_status TEXT, num_courses INT, num_semesters INT)
    """
    conn.execute(table_create_query)
    conn.close()


def insert_data(
    firstname,
    lastname,
    title,
    age,
    nationality,
    registration_status,
    numcourses,
    numsemesters,
):
    conn = sqlite3.connect("data.db")
    data_insert_query = """INSERT INTO Student_Data (firstname, lastname, title, 
    age, nationality, registration_status, num_courses, num_semesters) VALUES 
    (?, ?, ?, ?, ?, ?, ?, ?)"""
    data_insert_tuple = (
        firstname,
        lastname,
        title,
        age,
        nationality,
        registration_status,
        numcourses,
        numsemesters,
    )
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()


def read_data():
    conn = sqlite3.connect("data.db")
    data_read_query = """SELECT * FROM Student_Data"""
    cursor = conn.cursor()
    cursor.execute(data_read_query)
    rows = cursor.fetchall()
    conn.close()
    return rows


#### controller.py ####

import tkinter as tk
from tkinter import ttk, messagebox

# from model import create_table, insert_data, read_data


def enter_data(
    first_name_entry,
    last_name_entry,
    title_combobox,
    age_spinbox,
    nationality_combobox,
    reg_status_var,
    numcourses_spinbox,
    numsemesters_spinbox,
):
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("------------------------------------------")

            # Create Table
            create_table()

            # Insert Data
            insert_data(
                firstname,
                lastname,
                title,
                age,
                nationality,
                registration_status,
                numcourses,
                numsemesters,
            )

        else:
            messagebox.showwarning(
                title="Error", message="First name and last name are required."
            )
    else:
        messagebox.showwarning(
            title="Error", message="You have not accepted the terms"
        )


def read_data():
    # Create Table
    conn = sqlite3.connect("data.db")
    table_create_query = """CREATE TABLE IF NOT EXISTS Student_Data 
            (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
            registration_status TEXT, num_courses INT, num_semesters INT)
    """
    conn.execute(table_create_query)

    # Read Data
    data_read_query = """SELECT * FROM Student_Data"""
    cursor = conn.cursor()
    cursor.execute(data_read_query)
    rows = cursor.fetchall()
    conn.close()

    # Create new window for displaying data
    read_window = tk.Toplevel()
    read_window.title("Student Data")
    read_window.resizable(True, True)

    # Create table for displaying data
    table = ttk.Treeview(read_window)
    table["columns"] = (
        "firstname",
        "lastname",
        "title",
        "age",
        "nationality",
        "registration_status",
        "num_courses",
        "num_semesters",
    )
    table.heading("firstname", text="First Name")
    table.heading("lastname", text="Last Name")
    table.heading("title", text="Title")
    table.heading("age", text="Age")
    table.heading("nationality", text="Nationality")
    table.heading("registration_status", text="Registration Status")
    table.heading("num_courses", text="# Courses")
    table.heading("num_semesters", text="# Semesters")

    for row in rows:
        table.insert("", "end", values=row)

    table.pack(fill="both", expand=True)


##### main.py ######

import tkinter as tk
from tkinter import ttk
from tkinter import *

# from controller import enter_data, read_data
import random

window = Tk()
window.title("Formulario de Ingreso de Datos")
window.resizable(True, True)

frame = tk.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tk.LabelFrame(frame, text="Informacion de Usuario")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tk.Label(user_info_frame, text="Nombre")
first_name_label.grid(row=0, column=0, padx=10, pady=5)

last_name_label = tk.Label(user_info_frame, text="Apellido")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Titulo")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Sr.", "Sra.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Edad")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info_frame, text="Nacionalidad")
nationality_combobox = ttk.Combobox(
    user_info_frame,
    values=[
        "Argentina",
        "Uruguay",
        "Paraguay",
        "Brasil",
        "Chile",
        "Bolivia",
        "Peru",
    ],
)
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tk.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(courses_frame, text="Registracion")

reg_status_var = tk.StringVar(value="No Registrado")
registered_check = tk.Checkbutton(
    courses_frame,
    text="Actualmente Registrado",
    variable=reg_status_var,
    onvalue="Registrado",
    offvalue="No registrado",
)

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(
    terms_frame,
    text="I accept the terms and conditions.",
    variable=accept_var,
    onvalue="Accepted",
    offvalue="Not Accepted",
)
terms_check.grid(row=0, column=0)

# Button
button = tk.Button(
    frame,
    text="Enter data",
    command=lambda: enter_data(
        first_name_entry,
        last_name_entry,
        title_combobox,
        age_spinbox,
        nationality_combobox,
        reg_status_var,
        numcourses_spinbox,
        numsemesters_spinbox,
    ),
)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Read data button
read_button = tk.Button(frame, text="Read data", command=read_data)
read_button.grid(row=3, column=1, sticky="news", padx=20, pady=10)


def change_frame_color():
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]
    frame.configure(bg=random.choice(colors))


frame_color_button = tk.Button(
    frame, text="Change Frame Color", command=change_frame_color
)
frame_color_button.grid(row=4, column=1, sticky="news", padx=20, pady=10)

window.mainloop()


#### Codigo Original #####
