lista_cursos = ["PHP", "Python", "C#", "HTML y CSS", "Java", "JS", "Ruby", "Git"]

def seleccionar_curso() -> str:
    print("Ingrese el curso que desea realizar: ")
    for i, curso in enumerate(lista_cursos):
        print(f"{i+1}. {curso}")
    opcion = int(input())
    return lista_cursos[opcion - 1]