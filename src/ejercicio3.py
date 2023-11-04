'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.'''

def comprobarNota(nota:int) ->list:
    '''condición de las notas ingresadas en una lista'''
    if nota <=10 and nota >=0 :
        return True
    else:
        return False

if __name__=="__main__":
    #entrada
    asignaturas = ["Matemáticas", "Física", "Química", "Historia" ,"Lengua"]
    
    #proceso
    notas=[]
    for asignatura in asignaturas:
        nota = int(input(str(asignatura) + " escribe la nota que has sacado: "))
        if comprobarNota(nota) is True:
            notas.append(nota)
        else:
            #salida
            print("Vuelve a ingresa una nota de 0 a 10")  

    for n in range(0,len(asignaturas)):
        print("En la asignatura " + str(asignaturas[n]) + " has sacado un: " + str(notas[n]))