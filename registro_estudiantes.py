# Registro de estudiantes y notas

estudiantes = {}

print("REGISTRO DE ESTUDIANTES")

# Agregar estudiantes
cantidad = int(input("¿Cuántos estudiantes desea registrar? "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota: "))
    estudiantes[nombre] = nota

# Mostrar los estudiantes
print("\nEstudiantes registrados:")
for nombre, nota in estudiantes.items():
    print(nombre, "-", nota)

# Buscar un estudiante
buscar = input("\nIngrese el nombre del estudiante que desea buscar: ")

if buscar in estudiantes:
    print("La nota de", buscar, "es", estudiantes[buscar])
else:
    print("El estudiante no está registrado")

# Eliminar un estudiante
eliminar = input("\nIngrese el nombre del estudiante que desea eliminar: ")

if eliminar in estudiantes:
    del estudiantes[eliminar]
    print("Estudiante eliminado correctamente")
else:
    print("El estudiante no está registrado")

# Mostrar la lista final
print("\nRegistro final:")
for nombre, nota in estudiantes.items():
    print(nombre, "-", nota)