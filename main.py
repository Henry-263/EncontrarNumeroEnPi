import tkinter as tk
from tkinter import ttk

with open("pi.txt", "r") as f:
    pi_str = f.read().strip()

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
        resultado.config(text = f"El número {num} está en la posición: ({inicio}-{fin})")



ventana = tk.Tk()
ventana.title("Numero dentro de pi")
ventana.geometry("800x600")

texto = tk.Entry(validate="key",
    validatecommand=(ventana.register(validate_entry), "%S")
)
texto.place(x=300, y=50)

resultado = tk.Label(text="")
resultado.place(x=300, y=80)
texto.bind("<Return>", obtener_numero)
ventana.mainloop()

