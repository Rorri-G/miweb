# 1. funcion para eliminar los espacios en blanco

def no_space(texto):
    nuevo_texto = ""  # almacena el valor
    nuevo_texto = [char for char in texto if char != ' ']
    return nuevo_texto


def eliminar_espacios(texto):
    return ''.join([c for c in texto if c != ' '])


def no_spaces(texto):
    nuevo_texto = ""  # almacena el valor
    for char in texto:
        if char != " ":  # if is distinc to white space
            nuevo_texto += char
    return nuevo_texto


perrillo = ("La fortuna le sonrie al arriesgado")
# print(no_spaces(perrillo))
# print(eliminar_espacios(perrillo))
# print(no_space(perrillo))


# 2. Contar en un diccionario cuanto se repiten los caracteres de un String

def contar_letras(texto):
    # creamos un diccionario vacío para almacenar los recuentos de palabras
    recuentos = {}
    # convertimos el texto a una lista de palabras
    # palabras = texto.split()
    # iteramos sobre cada palabra en la lista
    for caracter in texto:
        # si la palabra ya está en el diccionario, incrementamos su recuento en 1
        if caracter in recuentos:
            recuentos[caracter] += 1
        # de lo contrario, agregamos la palabra al diccionario con un recuento de 1
        else:
            recuentos[caracter] = 1

    # devolvemos el diccionario completo de recuentos de palabras
    return recuentos


# perri_unido = no_space(perrillo)
# print(contar_letras(perri_unido))

##############################################################

# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista


def ordenar_diccionario_por_valor(diccionario):
    # Usamos la función sorted() para ordenar el diccionario por sus valores
    # Usamos el método items() para obtener una lista de tuplas (clave, valor)
    diccionario_ordenado = sorted(
        diccionario.items(), key=lambda x: x[1], reverse=True)

    # Devolvemos el diccionario ordenado como una lista de tuplas
    return diccionario_ordenado


# dict_ordenado = contar_letras(perri_unido)

# print(ordenar_diccionario_por_valor(dict_ordenado))

#################################################################
# 4. De un listado de tuplas, devolver las llaves que contengan el mayor Valor


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

# 5. crear un mensaje que diga:
# Los caracteres que mas se repiten con 4 repeticiones son :


def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"-{key} con {valor} repeticiones \n"
    return mensaje


##############################################################
# union de todas las funciones
# el objetivo es ver cual caracter se repite mas dentro de una frase
sin_espacios = no_space(perrillo)
contados = contar_letras(sin_espacios)
ordenados = ordenar_diccionario_por_valor(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)
