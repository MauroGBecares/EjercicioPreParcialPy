import cursos

def menu():
    print("\nBienvenido al registro !!")
    print("\nQue quiere hacer?")
    print("1- Registrar empleado.")
    print("2- Agregar nuevo curso")
    print("3- Mostrar resumen")
    print("4- Salir")
    opcion = int(input("\nElija la ópcion: "))
    return opcion

def registrar_empleado(empleados: list, cant_cargados: int) -> None:
    if cant_cargados < 46:
        print("\n -- Ingreso de nuevo empleado --")
        nombre = input("Ingrese el nombre del empleado: ")
        legajo = input("Ingrese el legajo del empleado: ")
        antiguedad = int(input("Ingrese la antiguedad del empleado (en meses): "))
        if antiguedad < 6:
            print("\nLa antiguedad del empleado es menor a 6 y por lo tanto no se puede registrar.")
            return
        empleados.append({'name' : nombre, 'leg' : legajo, 'ant' : antiguedad, 'cant_cursos' : 0, 'list_cursos' : []})
        cant_cargados = cant_cargados + 1
        print("\nEmpleado cargado exitosamente !")
        return

def agregar_curso(empleados: list) -> None:
    ingreso_legajo = input("\nIngrese el legajo del empleado: ")
    for empleado in empleados:
        if empleado['leg'] == ingreso_legajo:
            print("\nEmpleado encontrado !")
            opcion = 0
            while True:
                print("\nUsted esta en la sección agregar curso. Que desea hacer?.")
                print("1- Agregar curso")
                print("2- Mostrar cursos")
                print("3- Finalizar carga")
                opcion = int(input())
                if opcion == 1:
                    empleado['list_cursos'].append(cursos.seleccionar_curso())
                    empleado['cant_cursos'] = empleado['cant_cursos'] + 1
                elif opcion == 2:
                    print("\nCursos realizados: ")
                    for curso in empleado['list_cursos']:
                       print(f"\n{curso}") 
                elif opcion == 3:
                    return
                else:
                    print("\nOpcion invalida")
    print("\nEmpleado no encontrado")
    return

def mostrar_resumen(empleados: list):
    print(f"\nCantidad de empleados cargados: {len(empleados)}")
    lista_ordenada_empleados = sorted(empleados, key=lambda x: x['cant_cursos'], reverse=True)
    for empleado in lista_ordenada_empleados:
        print(f"\nEmpleado: {empleado['name']} - Legajo: {empleado['leg']} - Antiguedad: {empleado['ant']} meses")
        cursos = " - ".join(empleado['list_cursos'])
        print(f"Cursos: {cursos}")
        print(f"Cantidad de cursos: {empleado['cant_cursos']}")
