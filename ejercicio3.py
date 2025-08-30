# Ejercicio 3: Estudiante aprobado
# Un estudiante aprueba si su nota >= 7 O si pasó la recuperación

nota = float(input("Ingrese la nota del estudiante: "))

if nota < 7:
    print("Lo sentimos, el estudiante no ha aprobado. Se recomienda asistir a la recuperación.")
    recuperacion_input = input("¿Ingrese nota de recuperación? ")
    recuperacion = float(recuperacion_input)

    if recuperacion >= 7:
        print("¡Felicidades! El estudiante ha aprobado gracias a la recuperación.")
    else:
        print("Lo sentimos, el estudiante no ha aprobado ni siquiera con la recuperación.")
else:
    print("¡Felicidades! El estudiante ha aprobado con una nota de", nota)