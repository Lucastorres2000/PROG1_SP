from Validaciones import *


def pedir_flotante(mensaje):
 
    retorno = False
    flag_salida_while = False
    intentos = 0 
   
    while flag_salida_while == False and intentos  < 4 :
        aux_caracter = input(mensaje)
        
        try:
            numero = float(aux_caracter)
            return  numero
        
        except ValueError:
            print("!!!!! __  [ ERROR ] ---  Ingrese un nunero valido __ !!!!! ")
            intentos = intentos + 1
            
        if intentos == 4 :
    
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
    
    return retorno 

    
        

'''
    Pide un numero al usuario.
    Itera con un maximo de 3 intentos pidiendo un numero 
    valida solo numeros 
    Si es correcto RETORNA el valor, caso contrario ERROR

 parametro : Mensaje , Mensaje de interfaz al usuario

'''
def pedir_int(mensaje):
    retorno = False
    flag_salida_while = False
    intentos = 0 
    while flag_salida_while == False and intentos  < 4 :
        aux_caracter = input(mensaje)
        aux_flag = validar_int(aux_caracter )
        intentos = intentos + 1 
        if aux_flag == True :
                retorno = int(aux_caracter) 
                return retorno 
                
        else : 
            print("!!!!! __  [ ERROR ] ---  Ingrese un nunero valido __ !!!!! ")
            
        
        
        if intentos == 4 :
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
            
    return retorno

#---------------------------------------------------------------------------------------------------------------------------------

'''
    Pide un numero al usuario.
    Itera con un maximo de 3 intentos pidiendo un numero 
    valida solo numeros y entre un rango solicitado 
    Si es correcto RETORNA el valor, caso contrario ERROR

 parametro : Mensaje , Mensaje de interfaz al usuario
 parametro : min , Indica el rango minimo solicitado 
 parametro : max , Indica el rango maximo solicitado 

'''

def pedir_int_rango(mensaje, min , max ):
    retorno = False
    flag_salida_while = False
    intentos = 0 
    while flag_salida_while == False and intentos  < 4 :
        aux_caracter = input(mensaje)
        aux_flag = validar_int(aux_caracter )
        intentos = intentos + 1 
        if aux_flag == True :
                aux_retorno = int(aux_caracter) 
                if aux_retorno >= min and aux_retorno <= max :
                    retorno = int(aux_caracter) 
                    return retorno 
                else : 
                    print("!!!!! __  [ ERROR ] ---  Ingrese una opcion valida __ !!!!! ")
                
        else : 
            print("!!!!! __  [ ERROR ] ---  Ingrese un numero valido __ !!!!! ")
        
        
        if intentos == 4 :
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
    return retorno

#---------------------------------------------------------------------------------------------------------------------------------

'''
    Pide un strg o char al usuario 
    Itera con un maximo de 3 intentos 
    Valida solo letras 
    Si es correcto retorna el str, caso contrario ERROR
    
    parametro : Mensaje , Mensaje de interfaz al usuario
    
'''
def pedir_str(mensaje):
    retorno = False
    flag = False
    intentos = 0 
    while flag == False and intentos  < 3 :
        aux_caracter = input(mensaje)
        flag = validar_char(aux_caracter)
        
        if flag == True :
                return aux_caracter 
                
                
        else : 
            print("!!!!! __ [ ERROR ] ---  Ingrese una palabra valido (SOLO LETRAS ) __ !!!!! ")
        intentos = intentos + 1 
        
        if intentos == 4 :
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
            
    return retorno

#---------------------------------------------------------------------------------------------------------------------------------

def titulos() : 
    print(f"{'#-  Legajo ':<13}{" | "}{'Nombre':<15}{" | "}{'Genero':<10}{" | "}{'Parcial 1':<10}{" | "}{'Parcial 2 ':<10}{" | "}{'Promedio':<10}")

#---------------------------------------------------------------------------------------------------------------------------------

def mostrar_un_alumno(alumno : dict ) :
    print(f"#-    {alumno['legajo']:<7}{" | "}{alumno['ape_nom']:<15}{" | "}{alumno['genero']:<10}{" | "}{alumno['pp']:<10}{" | "}{alumno['sp']:<10}{" | "}{alumno['prom']:<10}")

#---------------------------------------------------------------------------------------------------------------------------------

def mostrar_lista_alumnos(lista_alumnos: list ) :
    titulos()
    print("#-----------------------------------------------------------------------------------------#\t")
    for alumno in lista_alumnos : 
        mostrar_un_alumno(alumno)
        
    print("#-----------------------------------------------------------------------------------------#\t")
    
#--------------------------------------------------------------------------------------------------------------------------------- 
      
def cargar_alumnos(lista_alumnos : list ) :
    alumno_aux = {} 
    validar_carga = False 
    alumno_aux['legajo'] = pedir_int("Ingrese legajo ") 
    
    if alumno_aux['legajo'] != False :   
        alumno_aux["ape_nom"] = pedir_str("Ingrese apellido y Nombre ")
        
        if alumno_aux["ape_nom"] != False :
            alumno_aux["genero"] = pedir_str("Ingrese Genero F/M : ")
            
            if alumno_aux['genero'] != False :
                 alumno_aux["pp"] = pedir_flotante("Ingrese nota primer parcial : ")
                 
                 if alumno_aux['pp'] != False : 
                     alumno_aux["sp"] = pedir_flotante("Ingrese nota segundo parcial : ")
                     alumno_aux["prom"] = 0
                     
                     if alumno_aux['sp'] != False : 
                         mostrar_un_alumno(alumno_aux)
                         print("#-- CARGAR ALUMNO ? \t #-- [1] SI \t #-- [2] NO")
                         aux_carga = pedir_int ("CARGAR ALUMNO -- > ")
                         if aux_carga == 1 :
                             lista_alumnos.append(alumno_aux)
                             print("#-------- # CARGADO CORRECTAMENTE #--------")
                         else : 
                             print("#-------- # NO SE CARGO EL ALUMNO #--------")
                         
                         
    
    
    
    
    
    

#---------------------------------------------------------------------------------------------------------------------------------

def calcular_promedio(lista_alumnos : list ) : 
    
    for alumno in lista_alumnos : 
        aux_suma_notas = alumno['pp'] + alumno['sp']
        total = aux_suma_notas / 2 
        alumno['prom'] = total 

#---------------------------------------------------------------------------------------------------------------------------------
    
def ordenar_por_nombre(lista_alumnos):

    for i in range(len(lista_alumnos) - 1):
        for j in range(i + 1, len(lista_alumnos)):
            if lista_alumnos[i]["ape_nom"] > lista_alumnos[j]["ape_nom"]:
                aux = lista_alumnos[i]
                lista_alumnos[i] = lista_alumnos[j]
                lista_alumnos[j] = aux

#---------------------------------------------------------------------------------------------------------------------------------

def ordenar_por_promedio(lista_alumnos) : 
    
    for i in range(len(lista_alumnos) - 1):
        for j in range(i + 1, len(lista_alumnos)):
            if lista_alumnos[i]["prom"] < lista_alumnos[j]["prom"]:
                aux = lista_alumnos[i]
                lista_alumnos[i] = lista_alumnos[j]
                lista_alumnos[j] = aux

#---------------------------------------------------------------------------------------------------------------------------------

def buscar_alumno (lista_alumnos) : 
    
    mostrar_lista_alumnos(lista_alumnos)
    alumno_aux = pedir_int(" #-- Ingrese legajo ---> ")
    se_encontro = False 
    
    for alumno in lista_alumnos : 
        if alumno['legajo'] == alumno_aux :
            titulos()
            print("#-----------------------------------------------------------------------------------------#\t")
            mostrar_un_alumno(alumno)
            se_encontro = True 
        
    if se_encontro == False :
            print("#------ !!!! NO EXISTE EL ALUMNO !!!! ------#")
            
            
    pass