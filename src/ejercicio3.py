'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.'''

def guardarNota(nota:int) ->list:
    '''almacena las asignaturas ingresadas en una lista'''
    for n in asignatura:
        calificaciones = []
        calificaciones.append(nota)
        nota = input("Indica la nota que sacaste en cada asignatura: ")
    return calificaciones

if __name__=="__main__":
    #entrada
    asignatura = ["Matemáticas", "Física", "Química", "Historia" ,"Lengua"]
    
    #proceso
    nota = input("Indica la nota que sacaste en cada asignatura: ")
    almacen = guardarNota(nota)

    #salida
    for n in asignatura:
        print("En " + str(asignatura) + " has sacado un " + str(nota))