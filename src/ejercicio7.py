'''Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''

def eliminaPosicionesMultiploTres(abc:list) ->list:
    '''comprueba si es multiplo de tres'''
    for n in range(len(abc)-1,-1,-1):
        if n %3 == 0:
            abc.pop(n)
    return abc

if __name__=="__main__":
    #entrada
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    #proceso
    multiplos = eliminaPosicionesMultiploTres(abc)

    #salida
    print(multiplos)
