
'''
    Valida que una cadena de caracteres sea un numero flotante 
    
    parametro : caracteres . variable de tipo str , almacena cadena a analizar
    retorna   : Si es solo numeros True , caso contrario False 

'''


def validar_flotante(cadena : str ):
    retorno = True
    cantidad_puntos = 0

    for c in cadena:
        
        if ord(c) >= 48 and ord(c) <= 57:
            pass

        elif c == ".":
            cantidad_puntos += 1

            if cantidad_puntos > 1:
                retorno = False
                return retorno 

        
        else:
            retorno = False

    return retorno

'''
    Valida que una cadena de caracteres sea solo numeros
    
    parametro : caracteres . variable de tipo str , almacena cadena a analizar
    retorna   : Si es solo numeros True , caso contrario False 

'''
def validar_int(caracteres : str ):
    for c in caracteres:
        if c < '0' or c > '9':
            return False
    return True


'''
    Valida que un numero sea par 
    
    parametro : numero . variable de tipo int, contiene el numero a analiazar  
    retorno   :

'''

def validar_par(numero: int) -> bool:
    
    retorno = False 
    
    if numero % 2 == 0 :
        retorno = True
        
    return retorno 
#---------------------------------------------------------------------------------------------------------------------------------
def validar_char(caracteres:str):
    retorno = True
    for c in caracteres:
        c_aux = ord(c)
        if not ((65 <= c_aux <= 90) or (97 <= c_aux <= 122)):
            retorno = False
    return retorno    
#---------------------------------------------------------------------------------------------------------------------------------
def convertir_a_mayuscula(caracteres:str):
    retorno = caracteres
    if ord(caracteres) >= 97 and ord(caracteres) <= 122:
        valor = ord(caracteres) - 32
        retorno = chr(valor)
    
    return retorno
    
 
 #---------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------
def convertir_a_minuscula (caracteres:str):
    retorno = caracteres
    if ord(caracteres) >= 65 and ord(caracteres) <= 90:
        valor = ord(caracteres) + 32
        retorno = chr(valor)
        
    return retorno
#---------------------------------------------------------------------------------------------------------------------------------
def validar_genero(caracteres:str):
    retorno = True
    caracteres = convertir_a_mayuscula(caracteres)
    if caracteres != 'F' and caracteres != 'M' and caracteres != 'X':
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
def contar_cadena(caracteres:str) :
    contador = 0

    for c in caracteres : 
        contador = contador + 1 
        
    return contador 

def validar_documento(dni:str) : 
    
    longitud_cadena = contar_cadena (dni)
    retorno = False
    
    if longitud_cadena >= 6 and longitud_cadena <= 8 :
        retorno = True
        
    return retorno 

def primera_a_mayuscula(palabra):
    return palabra.capitalize()