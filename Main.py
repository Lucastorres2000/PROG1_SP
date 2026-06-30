

import json 
from Funciones import * 
lista_alumnos_main = []
salir_menu = False 

while salir_menu == False:
    opcion = 0 
    print("\t\t\t")
    print("#------------------------------------#\t")
    print("#------ 1 ) Leer datos . ")
    print("#------ 2 ) Cargar datos .")
    print("#------ 3 ) Mostrar datos .")
    print("#------ 4 ) Calcular promedio .")
    print("#------ 5 ) Ordenar por promedio .")
    print("#------ 7 ) Salir .")
    print("#------------------------------------#\t\t\t")
    opcion = int(input("# --- OPCION --->  "))
    print("\t\t\t")
    match opcion :
        
        case 1 : 
            with open("data_sp.json","r") as archivo_json :
                datos = json.load(archivo_json)
            lista_alumnos_main = datos["estudiantes"]
            print("#------ CARGADO CORRECTAMENTE ------#  \t\t")

        case 2 :
            cargar_alumnos(lista_alumnos_main)
            print("#------ GUARDADO CORRECTAMENTE ------#  \t\t")
            
            pass
        
        case 3 : 
            mostrar_lista_alumnos(lista_alumnos_main)
            
        case 4 :
            calcular_promedio(lista_alumnos_main)
            print("#------ # CALCULANDO .... # ------#  \t\t")                                                      
            
        case 5 : 
            ordenar_por_promedio(lista_alumnos_main)
            print("#------ # ORDENANDO .... # ------#  \t\t") 
            
        case 6 :
                buscar_alumno(lista_alumnos_main)
            
        case 7 : 
            print("---------- # CERRANDO SISTEMA # ----------")
            salir_menu = True 