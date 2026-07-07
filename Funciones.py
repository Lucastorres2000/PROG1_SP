from Validaciones import *
import json 

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
    Pide un numero al usuario.
    Itera con un maximo de 3 intentos pidiendo un numero 
    valida solo numeros y entre un rango solicitado 
    Si es correcto RETORNA el valor, caso contrario ERROR

 parametro : Mensaje , Mensaje de interfaz al usuario
 parametro : min , Indica el rango minimo solicitado 
 parametro : max , Indica el rango maximo solicitado 

'''
 
def pedir_float_rango(mensaje:str ,num_min:int ,num_max:int ) -> float :
    
    retorno = False
    flag_salida_while = False
    intentos = 0 
    
    while flag_salida_while == False and intentos  <= 3 :
        aux_caracter = input(mensaje)
        aux_flag = validar_flotante(aux_caracter)
        intentos = intentos + 1 
        if aux_flag == True :
                aux_retorno = float(aux_caracter) 
                
                if aux_retorno >= num_min and aux_retorno <= num_max :
                    retorno = float(aux_caracter) 
                    break
                
                
        else : 
            print("!!!!! __  [ ERROR ] ---  Ingrese un nunero valido __ !!!!! 3/ ",intentos)
        
        
        if intentos == 4 :
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
    return retorno

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
a
    Pide un numero al usuario.
    Itera con un maximo de 3 intentos pidiendo un numero 
    valida que sea un numero flotante  
    

 parametro : Mensaje , Mensaje de interfaz al usuario
 retorno   : Si es correcto RETORNA el valor, caso contrario ERROR

'''
def pedir_float( mensaje )-> float :
    
    retorno = False
    flag_salida_while = False
    intentos = 0 
    
    while flag_salida_while == False and intentos  <= 3 :
        aux_caracter = input(mensaje)
        aux_flag = validar_flotante(aux_caracter)
        intentos = intentos + 1 
        if aux_flag == True :
                retorno = float(aux_caracter) 
                break
                
                
        else : 
            print("!!!!! __  [ ERROR ] ---  Ingrese un nunero valido __ !!!!! 3/ ",intentos)
        
        
        if intentos == 4 :
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
    return retorno

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
    Pide un numero al usuario.
    Itera con un maximo de 3 intentos pidiendo un numero 
    valida solo numeros 
    Si es correcto RETORNA el valor, caso contrario ERROR

 parametro : Mensaje , Mensaje de interfaz al usuario

'''
def pedir_int( mensaje ) -> int :
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

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
    Pide un numero al usuario.
    Itera con un maximo de 3 intentos pidiendo un numero 
    valida solo numeros y entre un rango solicitado 
    Si es correcto RETORNA el valor, caso contrario ERROR

 parametro : Mensaje , Mensaje de interfaz al usuario
 parametro : min , Indica el rango minimo solicitado 
 parametro : max , Indica el rango maximo solicitado 

'''

def pedir_int_rango(mensaje, min , max ) -> int:
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

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
    Pide un strg o char al usuario 
    Itera con un maximo de 3 intentos 
    Valida solo letras 
    Si es correcto retorna el str, caso contrario ERROR
    
    parametro : Mensaje , Mensaje de interfaz al usuario
    
'''
def pedir_str(mensaje) -> str:
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

#--------------------------------------------------------------------------------------------------------------------------------------------------

def pedir_genero () :
    retorno = False
    flag = False
    intentos = 0 
    while flag == False and intentos  < 3 :
        aux_sexo = input("Ingrese Genero F/M/X : ")
        validacion_sexo = validar_genero(aux_sexo)
        if validacion_sexo == True  :
                retorno = aux_sexo 
                break 
                       
        else : 
            print("!!!!! __ [ ERROR ] ---  Ingrese una palabra valido (SOLO LETRAS ) __ !!!!! ")
        intentos = intentos + 1 
        
        if intentos == 4 :
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
    
    return retorno 

#--------------------------------------------------------------------------------------------------------------------------------------------------

def titulos() : 
    print(f"{'#-  Legajo ':<13}{" | "}{'Nombre':<15}{" | "}{'Genero':<10}{" | "}{'Parcial 1':<10}{" | "}{'Parcial 2 ':<10}{" | "}{'Promedio':<10}")

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
    Recibe un alumno y lo muestra 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos

'''
def mostrar_un_alumno(alumno : dict ) :
    print(f"#-    {alumno['legajo']:<7}{" | "}{alumno['ape_nom']:<15}{" | "}{alumno['genero']:<10}{" | "}{alumno['pp']:<10}{" | "}{alumno['sp']:<10}{" | "}{alumno['prom']:<10}")

#--------------------------------------------------------------------------------------------------------------------------------------------------
'''
    Recorre una lista de alumnos y llama a mostar_un_alumno() pasandole cada alumno 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos
'''

def mostrar_lista_alumnos(lista_alumnos: list ) :
    titulos()
    print("#-----------------------------------------------------------------------------------------#\t")
    for alumno in lista_alumnos : 
        mostrar_un_alumno(alumno)
        
    print("#-----------------------------------------------------------------------------------------#\t")
    
#-------------------------------------------------------------------------------------------------------------------------------------------------- 
      
'''
    Carga un alumno 
    Pide cada dato validando la carga del mismo 
    una vez cargado los datos correctamente los agrega al diccionario 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos
'''

def cargar_alumnos(lista_alumnos : list ) :
    alumno_aux = {} 
    validar_carga = False 
    alumno_aux['legajo'] = pedir_int("Ingrese legajo :  ") 
    
    if alumno_aux['legajo'] != False :   
        alumno_aux["ape_nom"] = pedir_str("Ingrese apellido y Nombre :  ")
        
        if alumno_aux["ape_nom"] != False :
            alumno_aux["genero"] = pedir_genero ()
            
            if alumno_aux['genero'] != False :
                 alumno_aux["pp"] = pedir_float_rango("Ingrese nota primer parcial : ",1,10)
                 
                 if alumno_aux['pp'] != False : 
                     alumno_aux["sp"] = pedir_float_rango("Ingrese nota segundo parcial : ",1,10)
                     alumno_aux["prom"] = 0
                     
                     if alumno_aux['sp'] != False : 
                         
                         print("\n#---------------------------------------------------------------------------------------#\n")
                         mostrar_un_alumno(alumno_aux)
                         print("\n#---------------------------------------------------------------------------------------#\n")
                         print("")
                         print("#-- CARGAR ALUMNO ? \n\t #-- [1] SI \n\t#-- [2] NO\n")
                         aux_carga = pedir_int ("CARGAR ALUMNO -- > ")
                         if aux_carga == 1 :
                             lista_alumnos.append(alumno_aux)
                             print("\n#-------- # CARGADO CORRECTAMENTE #--------\n")
                         else : 
                             print("\n#-------- # NO SE CARGO EL ALUMNO #--------\n")
                                                
#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
    recibe una lista de alumnos 
    suma los valores del primer parcial y el segundo parcial , 
    luego los divide indicando el promedio y los asigna en la clave 'prom' dentro del alumno 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos
    
'''
def calcular_promedio(lista_alumnos : list ) : 
    
    for alumno in lista_alumnos : 
        aux_suma_notas = alumno['pp'] + alumno['sp']
        total = aux_suma_notas / 2 
        alumno['prom'] = total 


#--------------------------------------------------------------------------------------------------------------------------------------------------
 
'''
    recibe una lista diccionarios alumno , 
    los ordena alfabeticamente por apellido 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos

'''
   
def ordenar_por_nombre(lista_alumnos):

    for i in range(len(lista_alumnos) - 1):
        for j in range(i + 1, len(lista_alumnos)):
            if lista_alumnos[i]["ape_nom"] > lista_alumnos[j]["ape_nom"]:
                aux = lista_alumnos[i]
                lista_alumnos[i] = lista_alumnos[j]
                lista_alumnos[j] = aux

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
    recibe una lista diccionarios alumno , 
    los ordena por promedio 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos

'''

def ordenar_por_promedio(lista_alumnos) : 
    
    for i in range(len(lista_alumnos) - 1):
        for j in range(i + 1, len(lista_alumnos)):
            if lista_alumnos[i]["prom"] < lista_alumnos[j]["prom"]:
                aux = lista_alumnos[i]
                lista_alumnos[i] = lista_alumnos[j]
                lista_alumnos[j] = aux

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
    recibe una lista diccionarios alumno , 
    Busca un legajo indicado y lo muestra 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos

'''
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

#--------------------------------------------------------------------------------------------------------------------------------------------------     

'''
    Descarga la lista de alumnos de un archivo .json
    retorna la lista cargada .
'''
      
def bajar_json() -> list : 
    
    
    with open("data_sp.json","r") as archivo_json :
        
        datos = json.load(archivo_json)
        
    lista_alumnos = datos
    
    return lista_alumnos 

#--------------------------------------------------------------------------------------------------------------------------------------------------

'''

    Sube la lista de alumnos a un archivo .json 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos
    
'''

def subir_json(lista_alumnos : list ) : 
    
    with open("data_sp.json","w") as archivo_json :
                json.dump(lista_alumnos, archivo_json, indent=4 )
                
#--------------------------------------------------------------------------------------------------------------------------------------------------

'''

    Sube la lista de alumnos a un archivo .csv
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos
    
    
'''
def subir_csv (lista_alumnos) : 
    with open("data_alumnos.csv", "w+", encoding="utf-8") as archivo:

    # Escribir encabezados
        claves = list(lista_alumnos[0].keys())
        archivo.write(",".join(claves) + "\n")

    # Escribir datos
        for alumno in lista_alumnos:
            fila = []

            for clave in claves:
             fila.append(str(alumno[clave]))

            archivo.write(",".join(fila) + "\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------
            
'''
    Recorre una lista de alumnos y busca el de mayor promedio y lo retorna 
    
    parametro : lista_alumno lista de alumnos , contiene una lista de diccionarios indicando alumnos

'''
def buscar_mayor(lista_alumnos : list ) -> dict :
    
     
    aux_numero = 0 
    alumno_retornar = {}
    for alumno in lista_alumnos : 
        if alumno['prom'] > aux_numero :
            aux_numero = alumno['prom']
            alumno_retornar = alumno
    
    return alumno_retornar 
