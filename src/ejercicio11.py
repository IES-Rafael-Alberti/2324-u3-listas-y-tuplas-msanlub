'''Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.'''

def calculoProductoEscalar(vectorUno:list,vectorDos:list) ->int:
    '''calcular el producto escalar'''
    resultado = 0
    for posicion in range(len(vectorUno)):
        resultado += (vectorUno[posicion] * vectorDos[posicion])
    return resultado

if __name__=="__main__":
    #entrada
    vectorUno = [1,2,3]
    vectorDos = [-1,0,2]

    #proceso
    productoEscalar = calculoProductoEscalar(vectorUno,vectorDos)

    #salida
    print(productoEscalar)