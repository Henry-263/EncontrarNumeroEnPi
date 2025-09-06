with open("pi.txt", "r") as f:
    pi_str = f.read()
num = input("Ingresa un numero: ")
pos = pi_str.find(num)

if pos == -1:
    print("No existe el numero")
elif pos < 2:
    print("El numero es o el 3 o el .")
else:
    print("El numero esta en la posicion: (" + str(pos-1) + "-" + str(pos-2+len(num)) +  ")")

