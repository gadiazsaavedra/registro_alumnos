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
                title="Error", message="Nombre y Apellido son requeridos."
            )
    else:
        messagebox.showwarning(title="Error", message="Ud. NO acepto los Terminos")


#### Read Data from DataBase ####
import sqlite3
import tkinter as tk


def read_data():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT * FROM Student_Data")
    result = c.fetchall()

    conn.close()

    # Create a new label to display the data
    data_label = tk.Label(window, text="")
    data_label.pack()

    # Update the label with the data
    for row in result:
        data_label.config(
            text=data_label.cget("text")
            + "Name: {}, Age: {}\n".format(row[0], row[1], row[2])
        )


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

registered_label = tk.Label(courses_frame, text="Registro de Cursos por Semestre")

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

numcourses_label = tk.Label(courses_frame, text="# Cursos Completados")
numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(courses_frame, text="# Semestres")
numsemesters_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tk.LabelFrame(frame, text="Terminos y Condiciones")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(
    terms_frame,
    text="Acepto Terminos y Condiciones.",
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


### Delete Data ######
import tkinter as tk


def delete_data():
    first_name = first_name_field.get()

    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("DELETE FROM Student_Data WHERE name LIKE ?", (first_name + "%",))
    conn.commit()

    conn.close()

    # Clear the input field
    first_name_field.delete(0, tk.END)


# Create the GUI
# window = tk.Tk()
# window.title("Student Data")

# Create the input fields and buttons
# id_label = tk.Label(window, text="ID:")
# id_label.pack()
# id_field = tk.Entry(window)
# id_field.pack()
delete_button = tk.Button(frame, text="Delete", command=delete_data)
delete_button.grid(row=2, column=1, sticky="news", padx=20, pady=10)
# read_button = tk.Button(window, text="Read Data", command=read_data)
# read_button.pack()


### age average ###
"""
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def calculate_avg_age():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT AVG(age) FROM Student_Data")
    result = c.fetchone()[0]
    print("Average age:", result)

    # Create a bar chart of the age average and save it to a file
    fig, ax = plt.subplots()
    ax.bar(["Average Age"], [result])
    ax.set_title("Age Average")
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    fig.savefig("age_average.png")

    conn.close()


def show_age_average():
    # Create a new window to display the age average chart
    window = tk.Toplevel()
    window.title("Age Average Chart")

    # Load the chart image and display it in a canvas
    chart_image = tk.PhotoImage(file="age_average.png")
    canvas = tk.Canvas(window, width=chart_image.width(), height=chart_image.height())
    canvas.create_image(0, 0, anchor="nw", image=chart_image)
    canvas.pack()

    window.mainloop()


# Create the GUI
window = tk.Tk()
window.title("Age Average Calculator")

# Create the input field and buttons
input_label = tk.Label(window, text="Enter ages separated by commas:")
input_label.pack()
input_field = tk.Entry(window)
input_field.pack()
calculate_button = tk.Button(
    window, text="Calculate Average", command=calculate_avg_age
)
calculate_button.pack()
show_button = tk.Button(window, text="Show Chart", command=show_age_average)
show_button.pack()
"""

window.mainloop()


#### Codigo Original #####
