with open("pi.txt", "r") as f:
    pi_str = f.read().strip()  # Quita espacios al principio o final

num = input("Ingresa un número: ")

# Eliminamos el 3 y el punto inicial si es que están en pi.txt
pi_decimals = pi_str[2:] if pi_str.startswith("3.") else pi_str

pos = pi_decimals.find(num)
if pos == -1:
    print("No existe el número en los primeros 100000 decimales de pi")
else:
    # Posición humana (1 = primer decimal)
    start = pos + 1
    end = pos + len(num)
    print(f"El número está en la posición: ({start}-{end})")
