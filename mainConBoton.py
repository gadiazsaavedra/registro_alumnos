import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def ingresar_datos():
    aceptado = accept_var.get()

    if aceptado == "Aceptado":
        # Información del usuario
        nombre = first_name_entry.get()
        apellido = last_name_entry.get()

        if nombre and apellido:
            titulo = title_combobox.get()
            edad = age_spinbox.get()
            nacionalidad = nationality_combobox.get()

            # Información del curso
            estado_registro = reg_status_var.get()
            num_cursos = numcourses_spinbox.get()
            num_semestres = numsemesters_spinbox.get()

            print("Nombre: ", nombre, "Apellido: ", apellido)
            print("Título: ", titulo, "Edad: ", edad, "Nacionalidad: ", nacionalidad)
            print("# Cursos: ", num_cursos, "# Semestres: ", num_semestres)
            print("Estado de registro: ", estado_registro)
            print("------------------------------------------")

            # Crear tabla
            conn = sqlite3.connect("data.db")
            table_create_query = """CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
                    registration_status TEXT, num_courses INT, num_semesters INT)
            """
            conn.execute(table_create_query)

            # Insertar datos
            data_insert_query = """INSERT INTO Student_Data (firstname, lastname, title, 
            age, nationality, registration_status, num_courses, num_semesters) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)"""
            data_insert_tuple = (
                nombre,
                apellido,
                titulo,
                edad,
                nacionalidad,
                estado_registro,
                num_cursos,
                num_semestres,
            )
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

        else:
            tkinter.messagebox.showwarning(
                title="Error", message="Se requieren el nombre y el apellido."
            )
    else:
        tkinter.messagebox.showwarning(
            title="Error", message="No ha aceptado los términos"
        )


window = tkinter.Tk()
window.title("Formulario de entrada de datos")

frame = tkinter.Frame(window)
frame.pack()

# Guardando información del usuario
user_info_frame = tkinter.LabelFrame(frame, text="Información del usuario")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="Nombre")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Apellido")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Título")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Sr.", "Sra.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Edad")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nacionalidad")
nationality_combobox = ttk.Combobox(
    user_info_frame,
    values=[
        "África",
        "Antártida",
        "Asia",
        "Europa",
        "Norteamérica",
        "Oceanía",
        "Sudamérica",
    ],
)
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Guardando información del curso
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Estado de registro")

reg_status_var = tkinter.StringVar(value="No registrado")
registered_check = tkinter.Checkbutton(
    courses_frame,
    text="Actualmente registrado",
    variable=reg_status_var,
    onvalue="Registrado",
    offvalue="No registrado",
)

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Cursos completados")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semestres")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Aceptar términos
terms_frame = tkinter.LabelFrame(frame, text="Términos y condiciones")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="No aceptado")
terms_check = tkinter.Checkbutton(
    terms_frame,
    text="Acepto los términos y condiciones.",
    variable=accept_var,
    onvalue="Aceptado",
    offvalue="No aceptado",
)
terms_check.grid(row=0, column=0)

# Botón
button = tkinter.Button(frame, text="Ingresar datos", command=ingresar_datos)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


# boton para cambiar color de fondo
def cambiar_color_fondo():
    #    color = tkinter.colorchooser.askcolor()[1]
    window.configure(background="lightblue")


color_button = tkinter.Button(
    frame, text="Cambiar color de fondo", command=cambiar_color_fondo
)
color_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
