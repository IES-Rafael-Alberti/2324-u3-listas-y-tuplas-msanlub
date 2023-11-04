'''Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.'''

def calculoMedia(numeros:list) ->float:
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)

def calculoDesviacionTipica(numeros:list,media:float) ->float:
    resultado = 0
    for numero in numeros:
        resultado += (((numero - media) **2) /len(numeros))
    return resultado **0.5

if __name__=="__main__":
    #entrada
    numerosEntrada = input("Escribe una serie de números separados por comas: ")
    numeros = numerosEntrada.split(',')
    for numero in range(len(numeros)):
        if numeros[numero].isdigit():
            numeros[numero]= int(numeros[numero])

    #proceso
    media = calculoMedia(numeros)
    desviacionTipica = calculoDesviacionTipica(numeros,media)

    #salida
    print("La lista de numeros es: " + str(numeros) + ".La media es: " + str(media) + ",y la desviación típica es: " + str(desviacionTipica))