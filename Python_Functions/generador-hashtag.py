
from Python_Developer import espacio

#isalnum() 


cadena1 = "Python3"
cadena2 = "SoloLearn!"
cadena3 = "12345"

print(cadena1.isalnum())  # Devuelve True, ya que la cadena contiene solo caracteres alfanuméricos.
print(cadena2.isalnum())  # Devuelve False, ya que la cadena contiene un carácter especial (!).
print(cadena3.isalnum())  # Devuelve True, ya que la cadena contiene solo dígitos.



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



