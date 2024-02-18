def reemplazar_palabras(cadena, diccionario_reemplazos):
    for palabra_original, palabra_nueva in diccionario_reemplazos.items():
        cadena = cadena.replace(palabra_original, palabra_nueva)
    return cadena

# Ejemplo de uso
codigo_original = """
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::linked1::linked1::linked1::linked1::linked1::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q:
:Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::Finish_q::linked1::linked1::linked3::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$::$:
"""

diccionario_reemplazos = {
    ":Finish_q:": "0",
    ":WhiteBlock:": "#",
    ":linked3:": "$",
    ":linked1:": "/",
}

codigo_modificado = reemplazar_palabras(codigo_original, diccionario_reemplazos)
print(codigo_modificado)
