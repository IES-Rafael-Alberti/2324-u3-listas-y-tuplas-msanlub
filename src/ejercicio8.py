'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''

def comprobarPalindromo(palabra:str) ->bool:
    '''comprobamos si la palabra se lee igual de un lado que de otro'''
    if palabra == palabra[::-1]:
        return True
    else:
        return False

if __name__=="__main__":
    #entrada
    palabra = input("Escribe una palabra: ")
    
    #proceso
    esPalindromo = comprobarPalindromo(palabra)

    #salida
    if esPalindromo is True:
        print("Es palíndromo.")
    else:
        print("No es palíndromo.")