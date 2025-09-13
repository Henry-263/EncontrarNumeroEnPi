import tkinter as tk
from tkinter import ttk
import sys

ventana = tk.Tk()
ventana.title("Número dentro de pi")
ventana.geometry("800x600")

num = None
pos = None
posicion_busqueda = [0, 1]

try:
    with open("pi.txt", "r") as f:
        pi_str = f.read().strip()
except FileNotFoundError:
    print("No existe el archivo pi.txt")
    sys.exit()

def siguiente_numero():
    global posicion_busqueda
    global num, pos

    if num is not None and pos is not None:
        # empezamos a buscar desde la última posición encontrada +1
        posicion_busqueda[0] = pos + 1
        posicion_busqueda[1] += 1
        obtener_numero()

def validate_entry(text):
    return text.isdecimal()

def obtener_numero(event=None):
    global num, pos, posicion_busqueda
    if num != texto.get():
        posicion_busqueda[0] = 0
        posicion_busqueda[1] = 1
    num = texto.get()

    pi_decimals = pi_str[2:] if pi_str.startswith("3.") else pi_str

    pos = pi_decimals.find(num, posicion_busqueda[0])
    print(f"Buscando desde posición {posicion_busqueda}")

    if not num:
        resultado.config(text="El número ingresado no es válido")
    elif pos == -1:
        resultado.config(text="No existe el número en los primeros 100000 decimales de pi")
    else:
        inicio = pos + 1
        fin = pos + len(num)
        resultado.config(
            text=f"La vez {posicion_busqueda[1]} que aparece el número {num} está en la posición de pi: ({inicio}-{fin})"
        )

siguiente = tk.Button(ventana, text="->", command=siguiente_numero)
siguiente.place(x=350, y=100)

texto = tk.Entry(
    validate="key",
    validatecommand=(ventana.register(validate_entry), "%S")
)
texto.place(x=300, y=50)

resultado = tk.Label(text="")
resultado.place(x=250, y=80)

titulo = ttk.Label(
    text="Encuentra en qué posición de pi se encuentra un número:"
)
titulo.place(x=230, y=20)

texto.bind("<Return>", obtener_numero)

ventana.mainloop()


