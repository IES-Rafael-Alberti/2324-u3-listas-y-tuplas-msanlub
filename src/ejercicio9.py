'''Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.'''

def vecesVocal(palabra:str,vocales:str) -> int:
    '''cuenta el numero de veces que sale cada vocal'''
    conteo = 0
    for vocal in palabra:
        if vocal in vocales:
            conteo += 1
    return conteo

if __name__=="__main__":
    #entrada
    palabra = input("Escribe una palabra: ")

    #proceso
    vocales = ["a","e","i","o","u"]
    

