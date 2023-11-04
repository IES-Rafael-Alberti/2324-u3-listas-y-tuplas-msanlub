'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.'''

def guardaAsignatura(asignatura:str) ->list:
    '''almacena las asignaturas ingresadas en una lista'''
    asignaturas = []
    asignaturas.append(asignatura)
    return asignaturas


if __name__=="__main__":
    #entrada
    asignatura = ["Matemáticas", "Física", "Química", "Historia" ,"Lengua"]

    #proceso
    almacen = guardaAsignatura(asignatura)
    #salida
    print(almacen)