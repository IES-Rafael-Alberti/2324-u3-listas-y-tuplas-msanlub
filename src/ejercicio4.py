'''Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.'''

def ordenMenorMayor(numeros:list) ->list:
    '''ordena los numeros ingresados'''
    numero = len(numeros)
    for i in range(numero-1):       # bucle padre
        for j in range(numero-1-i): # bucle hijo
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    return numeros

if __name__=="__main__":
    #entrada y proceso
    numeros = []
    while len(numeros) < 8:
        numero = int(input("Escribe los números ganadores de la primitiva: "))
        numeros.append(numero)
    else:
        print("Error: tamaño de la lista alcanzado (sólo 8 digitos).")

    #salida
    ordenados = ordenMenorMayor(numeros)
    print(ordenados)

