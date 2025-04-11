import json
import os

if os.path.exists('archivo_Tareas.json'): #asegurandonos que el archivo existe antes de abrir; si existe, lo cargamos
    with open('archivo_Tareas.json', 'r') as file: 
        archivoTareas = json.load(file)

else:
    archivoTareas = {'Tareas': []}


def agregarTarea(texto):
    tarea_Agregada = {'Contenido' : texto,
                      'Estado' : 'N/C'}
    
    #a la lista de tareas en el json le agregamos la que se acaba de ingresar
    archivoTareas['Tareas'].append(tarea_Agregada)
    print(tarea_Agregada)
    with open('archivo_Tareas.json', 'w') as file: 
        json.dump(archivoTareas, file, indent=4)
    return 'La tarea se ha agregado exitosamente.'
    
def verTareas(): 
    #Se hace la variable i para enumerar las tareas. Cada tarea (diccionario) representada por "t"
    for i, t in enumerate(archivoTareas['Tareas'], start=1): 
        print(f"{i} {t['Estado']} {t['Contenido']}")

texto = input('Ingrese una tarea: \n')
agregarTarea(texto)

print("LAS TAREAS SON: ")
verTareas()

#texto = input("Ingrese la tarea que desea agregar: ")
#agregarTarea(texto)
'''
def eliminarTarea():
    return

def modificarTarea(): 
    return

def 
'''