import tkinter as tk
from tkinter import ttk
import sys

ventana = tk.Tk()
ventana.title("Número dentro de pi")
ventana.geometry("800x600")

ventana.grid_columnconfigure(1, weight=1)

tam_fuente = 15
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


texto = tk.Entry(
    font=("Arial", tam_fuente),
    validate="key",
    validatecommand=(ventana.register(validate_entry), "%S")
)
texto.grid(row=1, column=1)

siguiente = tk.Button(ventana, text="->", command=siguiente_numero, font=("Arial", tam_fuente))
siguiente.grid(row=3, column=1)

resultado = tk.Label(text="", font=("Arial", tam_fuente))
resultado.grid(row=2, column=1)

titulo = ttk.Label(
    font=("Arial", tam_fuente),
    text="Encuentra en qué posición de pi se encuentra un número:"
)
titulo.grid(row=0, column=1)

texto.bind("<Return>", obtener_numero)

ventana.mainloop()


