def validar_int(caracter):
    for c in caracter:
        if c < '0' or c > '9':
            return False
    return True
#---------------------------------------------------------------------------------------------------------------------------------
def validar_par(numero: int) -> bool:
    
    retorno = False 
    
    if numero % 2 == 0 :
        retorno = True
        
    return retorno 
#---------------------------------------------------------------------------------------------------------------------------------
def validar_char(caracter):
    retorno = True
    for c in caracter:
        c_aux = ord(c)
        if not ((65 <= c_aux <= 90) or (97 <= c_aux <= 122)):
            retorno = False
    return retorno    
#---------------------------------------------------------------------------------------------------------------------------------
def convertir_a_mayuscula(caracter):
    retorno = caracter
    if ord(caracter) >= 97 and ord(caracter) <= 122:
        valor = ord(caracter) - 32
        retorno = chr(valor)
    
    return retorno
    
 
 #---------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------
def convertir_a_minuscula (caracter):
    retorno = caracter
    if ord(caracter) >= 65 and ord(caracter) <= 90:
        valor = ord(caracter) + 32
        retorno = chr(valor)
        
    return retorno
#---------------------------------------------------------------------------------------------------------------------------------
def validar_genero(caracter):
    retorno = True
    caracter = convertir_a_mayuscula(caracter)
    if caracter != 'F' and caracter != 'M' and caracter != 'X':
        retorno = False
    
    return retorno
#---------------------------------------------------------------------------------------------------------------------------------
def es_float(valor):
    retorno = False
    contador = 0
    contador_puntos = 0
    for caracteres in valor:
        retorno = False
        caracter = ord(caracteres)
        # Controlo que sea el primer caracter 
        if (contador == 0):
            # Controlo que no sea un numero
            if (caracter < 48 or caracter > 57):
                retorno = False
                break
            # Controlo que sea un numero
            else:
                retorno = True
        # Controlo a partir del segundo caracter en adelante
        if (contador > 0) and ((caracter >= 48 and caracter <= 57) or (caracter == 46)):
            retorno = True
        # Controlo la cantidad de puntos
        if caracter == 46:
            contador_puntos += 1
        # Controlo si hay mas de 1 punto
        if contador_puntos > 1:
            retorno = False
            break

        contador += 1
    return retorno
#---------------------------------------------------------------------------------------------------------------------------------

'''
    Retorna la cantidad de caracteres dentro de una cadena
    
    parametro : cadena a analizar 

'''
#---------------------------------------------------------------------------------------------------------------------------------
def contar_cadena(str) :
    contador = 0
    for c in str : 
        contador = contador + 1 
        
    return contador 

def validar_documento(dni) : 
    
    longitud_cadena = contar_cadena (dni)
    retorno = False
    
    if longitud_cadena >= 6 and longitud_cadena <= 8 :
        retorno = True
        
    return retorno 

def primera_a_mayuscula(palabra):
    return palabra.capitalize()