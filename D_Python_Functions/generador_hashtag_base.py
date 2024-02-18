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





