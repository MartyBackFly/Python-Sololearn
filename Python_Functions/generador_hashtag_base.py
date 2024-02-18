from aafuncionimprimir import espacio




espacio()





frase = input("put the frase here :P ")



def generar_hashtag(frase):
    palabras = frase.split()
    hashtags = ['#' + palabra for palabra in palabras if palabra.isalnum()]
    return hashtags

# Ejemplo de uso:
#frase_ejemplo = "¡ Aprendiendo Python en SoloLearn ! "

hashtags_generados = generar_hashtag(frase)#(frase_ejemplo)
print((hashtags_generados))








espacio()


#aca obtenemos la frase con hashtag peroo sin coma y sin comillas 


frase = input("Ingrese la frase aquí: ")

def generar_hashtag(frase):
    palabras = frase.split()
    hashtags = ' '.join('#' + palabra for palabra in palabras if palabra.isalnum())
    return hashtags

hashtags_generados = generar_hashtag(frase)
print(hashtags_generados)





espacio()



