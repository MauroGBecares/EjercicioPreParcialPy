import funciones as func


lista_empleados = []
cant_empleados_cargados = 0

opcionSalir = ""

while opcionSalir != "salir":
    opcion = func.menu()
    if opcion == 1:
        func.registrar_empleado(lista_empleados, cant_empleados_cargados)
    elif opcion == 2:   
        func.agregar_curso(lista_empleados)
    elif opcion == 3:
        func.mostrar_resumen(lista_empleados)
    elif opcion == 4:
        opcionSalir = "salir"
    else:
        print("\nLa opcion ingresada es incorrecta.")

print("\nAdios !!")

