'''Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''

def multiploTres(abc:list) ->bool:
    '''comprueba si es multiplo de tres'''
    lista = []
    for n in range(0,len(abc)):
        if n %3 != 0:
            lista.append(abc[n])
    return lista

if __name__=="__main__":
    #entrada
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    #proceso
    multiplos = multiploTres(abc)

    #salida
    print(multiplos)
