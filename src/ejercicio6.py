'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.'''

def comprobarNota(nota:int) ->list:
    '''condición de las notas ingresadas en una lista'''
    if nota <5 and nota >=0 :
        return True
    else:
        return False

if __name__=="__main__":
    #entrada
    asignaturas = ["Matemáticas", "Física", "Química", "Historia" ,"Lengua"]
    
    #proceso
    notas=[]
    suspensos = []
    for asignatura in asignaturas:
        nota = int(input(str(asignatura) + " escribe la nota que has sacado: "))
        notas.append(nota)
        if comprobarNota(nota) is True:
            suspensos.append(asignatura)

    #salida
    print("Las asignaturas que tienes que repetir son: " + str(suspensos))
    