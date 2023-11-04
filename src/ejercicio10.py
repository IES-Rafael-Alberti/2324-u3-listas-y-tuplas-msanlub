'''Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.'''

def numeroMayor(numeros:int) ->int:
    '''encuentra el numero mayor'''
    return max(numeros)
    

def numeroMenor(numeros:int) ->int:
    '''encuentra el numero menor'''
    return min(numeros)

if __name__=="__main__":
    #entrada
    numeros = [50, 75, 46, 22, 80, 65, 8]

    #proceso
    mayor = numeroMayor(numeros)
    menor = numeroMenor(numeros)

    #salida
    print("El número mayor es: " + str(mayor) + " y el menor es: " + str(menor) + ".")