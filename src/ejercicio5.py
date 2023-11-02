'''Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.'''

def ordenMayorMenor(lista:list) ->list:
    '''ordena los lista ingresados'''
    numero = len(lista)
    for i in range(numero-1):       # bucle padre
        for j in range(numero-1-i): # bucle hijo
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

if __name__=="__main__":
    #entrada
    lista = [1,2,3,4,5,6,7,8,9,10]
    #salida
    ordenados = ordenMayorMenor(lista)
    print(ordenados)
