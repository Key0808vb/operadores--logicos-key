# Ejercicio 2: Descuento especial
# Un cliente recibe descuento si es mayor de 60 años O si tiene discapacidad

edad = int(input("Ingrese la edad: "))
discapacitado = input("¿Está discapacitado? (si/no): ").strip().lower() == "si"

if discapacitado or edad > 60:
    print("Recibe el descuento especial.")
else:
    print("No recibe descuento.")