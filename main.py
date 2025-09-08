import tkinter as tk
from tkinter import ttk
import sys

ventana = tk.Tk()
ventana.title("Numero dentro de pi")
ventana.geometry("800x600")

try:
    with open("pi.txt", "r") as f:
        pi_str = f.read().strip()
except FileNotFoundError:
    print("No existe el archivo pi.txt")
    sys.exit()

def validate_entry(text):
    return text.isdecimal()
def obtener_numero(event = None):
    num = texto.get()
    texto.delete(0, tk.END)
    pi_decimals = pi_str[2:] if pi_str.startswith("3.") else pi_str

    pos = pi_decimals.find(num)
    if not num:
        print("El numero ingresado no es valido")
        resultado.config(text = "El numero ingresado no es valido")
    elif pos == -1:
        print("No existe el número en los primeros 100000 decimales de pi")
        resultado.config(text = "No existe el número en los primeros 100000 decimales de pi")
    else:
        inicio = pos + 1
        fin = pos + len(num)
        print(f"El número está en la posición: ({inicio}-{fin})")
        resultado.config(text = f"El número {num} está en la posición de pi: ({inicio}-{fin})")



texto = tk.Entry(validate="key",
    validatecommand=(ventana.register(validate_entry), "%S")
)
texto.place(x=300, y=50)

resultado = tk.Label(text="")
resultado.place(x=250, y=80)

titulo = ttk.Label(text="Encuentra en que posicion de pi se encuentra un numero:")
titulo.place(x=230, y=20)

texto.bind("<Return>", obtener_numero)
ventana.mainloop()

