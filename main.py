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

    # Create a frame for the data grid
    data_frame = tk.Frame(window)
    data_frame.pack()

    # Create labels for column headings
    id_label = tk.Label(data_frame, text="Nombre")
    id_label.grid(row=0, column=0)

    name_label = tk.Label(data_frame, text="Apellido")
    name_label.grid(row=0, column=1)
    # Add more column heading labels
    name_label = tk.Label(data_frame, text="Titulo")
    name_label.grid(row=0, column=2)

    name_label = tk.Label(data_frame, text="Edad")
    name_label.grid(row=0, column=3)

    name_label = tk.Label(data_frame, text="Nacionalidad")
    name_label.grid(row=0, column=4)

    name_label = tk.Label(data_frame, text="Estado")
    name_label.grid(row=0, column=5)

    name_label = tk.Label(data_frame, text="# Cursos")
    name_label.grid(row=0, column=6)

    name_label = tk.Label(data_frame, text="# Semestre")
    name_label.grid(row=0, column=7)

    # Loop through data and add to grid
    for i, row in enumerate(result):
        id_val = tk.Label(data_frame, text=row[0])
        id_val.grid(row=i + 1, column=0)

        name_val = tk.Label(data_frame, text=row[1])
        name_val.grid(row=i + 1, column=1)

        # Add more data labels to the grid
        name_val = tk.Label(data_frame, text=row[2])
        name_val.grid(row=i + 1, column=2)

        name_val = tk.Label(data_frame, text=row[3])
        name_val.grid(row=i + 1, column=3)

        name_val = tk.Label(data_frame, text=row[4])
        name_val.grid(row=i + 1, column=4)

        name_val = tk.Label(data_frame, text=row[5])
        name_val.grid(row=i + 1, column=5)

        name_val = tk.Label(data_frame, text=row[6])
        name_val.grid(row=i + 1, column=6)

        name_val = tk.Label(data_frame, text=row[7])
        name_val.grid(row=i + 1, column=7)

    # Configure column widths
    data_frame.grid_columnconfigure(0, minsize=50)
    data_frame.grid_columnconfigure(1, minsize=100)

    # Add border to window
    window.config(relief="sunken", bd=2)

    # Add border to frames
    data_frame.config(relief="sunken", bd=2)
    # headings_frame is not defined, so comment out this line
    # headings_frame.config(relief="sunken", bd=2)

    # Add borders to labels
    id_label.config(relief="sunken", bd=2)
    name_label.config(relief="sunken", bd=2)
    name_label = tk.Label(data_frame, text="Apellido", relief="sunken")
    name_label.grid(row=0, column=1)

    # Add borders to separators
    for sep in data_frame.grid_slaves():
        if isinstance(sep, ttk.Separator):
            sep.config(relief="sunken", bd=2)





"""
### Delete Data ######
def delete_data():
    id = id_field.get()

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('DELETE FROM Student_Data WHERE id=?', (id,))
    conn.commit()

    conn.close()

    # Clear the input field
    id_field.delete(0, tk.END)

# Create the GUI
#window = tk.Tk()
#window.title("Student Data")

# Create the input fields and buttons
id_label = tk.Label(window, text="ID:")
id_label.pack()
id_field = tk.Entry(window)
id_field.pack()
delete_button = tk.Button(window, text="Delete", command=delete_data)
delete_button.pack()
read_button = tk.Button(window, text="Read Data", command=read_data)
read_button.pack()
"""


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


# function to find a student

import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk

# Create the root window
root = tk.Tk()
# Create a frame for the data grid
data_frame = tk.Frame(window)
data_frame.pack()
# ...


def find_student_by_name(name):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT * FROM Student_Data WHERE firstname LIKE ?", (f"{name}%",))
    result = c.fetchall()

    conn.close()

    return result


def handle_find_button():
    if name := name_entry.get():
        if result := find_student_by_name(name):
            _extracted_from_handle_find_button_5(result)
        else:
            messagebox.showinfo(
                "Student Not Found", f"No student found with name '{name}'"
            )
    else:
        messagebox.showwarning("Invalid Input", "Please enter a name to search for")


# TODO Rename this here and in `handle_find_button`
def _extracted_from_handle_find_button_5(result):
    # Clear previous search results (if any)
    for child in data_frame.winfo_children():
        child.destroy()

    # Highlight the data_frame
    data_frame.configure(bg="yellow")

    # Create table for displaying results
    table = ttk.Treeview(data_frame)
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

    for row in result:
        table.insert("", "end", values=row)

    table.pack(fill="both", expand=True)



# Create a frame inside the root window for the search results
result_frame = tk.Frame(root)
result_frame.pack()

# Create the "Enter Data" button
#enter_data_button = tk.Button(result_frame, text="Enter Data")
#enter_data_button.pack(side=tk.TOP)

# Create the name entry widget
name_entry = tk.Entry(frame)
name_entry.grid(row=5, column=0, sticky="news", padx=30, pady=10)

# Create the "Find" button
find_button = tk.Button(frame, text="Find", command=handle_find_button)
find_button.grid(row=5, column=1, sticky="news", padx=20, pady=10)




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
