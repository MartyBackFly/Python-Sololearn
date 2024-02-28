#   En este codigo agarre una serie de caracteres que tienen un significado traducido a emoticons 
#   para el perfil en Steam que hice hace un tiempo a mano... palabra por palabra 
#   y le hice un remplazo de las 4 palabras claves :Finish_q: :WhiteBlock: 
#   :linked3:":linked1:": .. por simbolos # , -, _ , $ para formar a Toad 
#   mas abajo en el diccionario de palabras pueden cambiar los simbolos para
#   probar algun nuevo diseñó...


# dejo mi perfil steam para que puedan ver el original 

# https://steamcommunity.com/id/Martybackfly/



def reemplazar_palabras(cadena, diccionario_reemplazos):
    for palabra_original, palabra_nueva in diccionario_reemplazos.items():
        cadena = cadena.replace(palabra_original, palabra_nueva)
    return cadena

# Ejemplo de uso
codigo_original = """
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::linked1::linked1::linked1::linked1::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::linked1::linked3::linked3::linked3::linked3::WhiteBlock::WhiteBlock::linked1::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::WhiteBlock::linked3::linked3::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::WhiteBlock::linked3::linked3::linked3::linked3::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::linked3::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked3::linked3::linked3::linked3::linked3::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::linked3::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked3::linked3::WhiteBlock::WhiteBlock::linked3::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::WhiteBlock::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked3::linked3::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::WhiteBlock::linked3::linked3::linked3::linked3::linked3::linked3::linked3::linked3::linked3::WhiteBlock::WhiteBlock::linked3::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::linked3::linked3::linked1::linked1::linked1::linked1::linked1::linked1::linked1::linked1::linked3::linked3::linked3::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::linked1::linked1::WhiteBlock::WhiteBlock::linked1::WhiteBlock::WhiteBlock::linked1::WhiteBlock::WhiteBlock::linked1::linked1::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::WhiteBlock::WhiteBlock::linked1::WhiteBlock::WhiteBlock::linked1::WhiteBlock::WhiteBlock::WhiteBlock::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::WhiteBlock::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::linked1::linked1::linked1::linked1::linked1::linked1::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
"""

diccionario_reemplazos = {
    ":Finish_q:": "-",
    ":WhiteBlock:": "_",
    ":linked3:": "$",
    ":linked1:": "#",
}

codigo_modificado = reemplazar_palabras(codigo_original, diccionario_reemplazos)
print(codigo_modificado)
