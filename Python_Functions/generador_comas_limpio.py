from aafuncionimprimir import espacio



#en este caso obtenemos la frase con hashtag peroo sin coma y sin comillas 


frase = input("Ingrese la frase aquí: ")

def generar_hashtag(frase):
    palabras = frase.split()
    comas = ' '.join(palabra + ','   for palabra in palabras if palabra.isalnum())
    return comas

hashtags_generados = generar_hashtag(frase)
print(hashtags_generados)





espacio()
