

import json 
from Funciones import * 
lista_alumnos_main = []
salir_menu = False 
validar_carga = False 

while salir_menu == False:
    opcion = 0 
    print("\n")
    print("#------------------------------------#")
    print("#------  1 ) Leer datos . ")
    print("#------  2 ) Cargar datos .")
    print("#------  3 ) Mostrar datos .")
    print("#------  4 ) Calcular promedio .")
    print("#------  5 ) Ordenar por promedio .")
    print("#------  6 ) Buscar alumno . ")
    print("#------  7 ) Exportar .json  . ")
    print("#------  8 ) Exportar .csv  . ")
    print("#------  9 ) Buscar mayor promedio . ")
    print("#------ 10 ) Salir .")
    print("#------------------------------------#\n")
    opcion = int(input("# --- OPCION --->  "))
    print("\n")
    match opcion :
        
        case 1 : 
            lista_alumnos_main = bajar_json()
            validar_carga = True
            print("\n#------ !!! CARGADO CORRECTAMENTE !!! ------#\n")

        case 2 :
            cargar_alumnos(lista_alumnos_main)
            validar_carga = True
            print("\n#------ !!! GUARDADO CORRECTAMENTE  !!! ------#\n")
            
        case 3 : 
            if validar_carga == True : 
                mostrar_lista_alumnos(lista_alumnos_main)
                
            else : 
                print("\n#-------- !!! PRIMERO DEBE CARGAR UN ALUMNO !!! -------- #\n")
            
        case 4 :
            if validar_carga == True :
                calcular_promedio(lista_alumnos_main)
                print("\n#------ # !!! CALCULANDO !!! # ------#")   
                
            else : 
                print("\n# -------- !!! PRIMERO DEBE CARGAR UN ALUMNO !!! -------- #\n")                                                   
            
        case 5 : 
            if validar_carga == True :
                ordenar_por_promedio(lista_alumnos_main)
                print("\n#------ # ORDENANDO .... # ------# \n") 
            else : 
                print("\n# -------- !!! PRIMERO DEBE CARGAR UN ALUMNO !!! -------- #\n")
            
        case 6 :
            if validar_carga == True :
                buscar_alumno(lista_alumnos_main)
            else : 
                print("\n# -------- !!! PRIMERO DEBE CARGAR UN ALUMNO !!! -------- #\n")
        
        case 7 : 
            if validar_carga == True :
                subir_json(lista_alumnos_main)
                print("\n#------ !!! GUARDADO CORRECTAMENTE  !!! ------#\n")
            else : 
                print("\n# -------- !!! PRIMERO DEBE CARGAR UN ALUMNO !!! -------- #\n")
        
        case 8: 
            if validar_carga == True :
                subir_csv (lista_alumnos_main)
            else : 
                print("\n# -------- !!! PRIMERO DEBE CARGAR UN ALUMNO !!! -------- #\n")
            
        case 9 : 
            if validar_carga == True :
                aux_mejor_promedio = buscar_mayor(lista_alumnos_main)
                mostrar_un_alumno(aux_mejor_promedio)
            else : 
                print("\n# -------- !!! PRIMERO DEBE CARGAR UN ALUMNO !!! -------- #\n")

        case 10 : 
            print("\n!!!!!!!!---------- # CERRANDO SISTEMA # ----------!!!!!!!!\n")
            salir_menu = True 