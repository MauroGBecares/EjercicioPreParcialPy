import cursos

def menu():
    print("Bienvenido al registro !!")
    print("Que quiere hacer?")
    print("1- Registrar empleado.")
    print("2- Agregar nuevo curso")
    print("3- Mostrar resumen")
    print("4- Salir")
    opcion = int(input("Elija la ópcion: "))
    return opcion

def registrar_empleado(empleados: list, cant_cargados: int) -> None:
    if cant_cargados < 46:
        print("Ingreso de nuevo empleado.")
        nombre = input("Ingrese el nombre del empleado: ")
        legajo = input("Ingrese el legajo del empleado: ")
        antiguedad = int(input("Ingrese la antiguedad del empleado (en meses): "))
        while True:
            if antiguedad < 6:
                antiguedad = int(input("La antiguedad ingresada es menor a 6. Vuelva a cargar una mayor: "))
            else:                
                break
        empleados.append({'name' : nombre, 'leg' : legajo, 'ant' : antiguedad, 'cant_cursos' : 0, 'list_cursos' : []})
        cant_cargados = cant_cargados + 1
        print("Empleado cargado exitosamente !")

def agregar_curso(empleados: list) -> None:
    ingreso_legajo = input("Ingrese el legajo del empleado: ")
    for empleado in empleados:
        if empleado['leg'] == ingreso_legajo:
            print("Empleado encontrado !\n")
            opcion = 0
            while opcion != 2:
                print("Usted esta en la sección agregar curso. Que desea hacer?.")
                print("1- Agregar curso")
                print("2- Mostrar cursos")
                print("3- Finalizar carga")
                opcion = int(input())
                if opcion == 1:
                    empleado['list_cursos'].append(cursos.seleccionar_curso())
                    empleado['cant_cursos'] = empleado['cant_cursos'] + 1
                elif opcion == 2:
                    print("Cursos realizados: ")
                    for curso in empleado['list_cursos']:
                       print(f"{curso}\n") 
                else:
                    return
    print("Empleado no encontrado")
    return

def mostrar_resumen(empleados: list):
    lista_ordenada_empleados = sorted(empleados, key=lambda x: x['cant_cursos'], reverse=True)
    for empleado in lista_ordenada_empleados:
        print(f"Empleado: {empleado['name']} - Legajo: {empleado['leg']} - Antiguedad: {empleado['ant']} meses")
        cursos = " - ".join(empleado['list_cursos'])
        print(f"Cursos: {cursos}")
        print(f"Cantidad de cursos: {empleado['cant_cursos']}")
