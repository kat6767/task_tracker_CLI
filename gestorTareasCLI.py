import json
import os

run = True

#creamos una variable para guardar la ruta (nombre) de nuestro archivo 
ruta_tareas = 'archivo_Tareas.json'

#funcion para guardar las tareas que se agreguen.
def guardar_Modificacion(datos): #datos espera un conjunto/diccionario para añadir al json. 
    with open(ruta_tareas, 'w') as file: 
        json.dump(datos, file, indent=4)

#funcion que retorna un archivo preexistente o crea uno de ser necesario.
def cargarArchivo():
    if os.path.exists(ruta_tareas): 
        with open(ruta_tareas, 'r') as file: 
            archivoTareas = json.load(file)
        return archivoTareas
    else: 
        nuevo_archivo = {'Tareas': []}
        guardar_Modificacion(nuevo_archivo)
        return nuevo_archivo

def leerUltimoID(): 
        archivo_Tareas = cargarArchivo()
        if not archivo_Tareas or not archivo_Tareas['Tareas']: 
            return 0 
            
        lista_IDs = [int(t['ID']) for t in archivo_Tareas['Tareas']]
        return max(lista_IDs)

#el contenidoTarea debe ser string. 
def agregar_Tarea(contenidoTarea):
    if not contenidoTarea or not contenidoTarea.strip():
        print('El contenido de la tarea no puede estar vacío.')
        return
    
    archivo_Tareas = cargarArchivo()

    IDtarea = leerUltimoID() + 1
    nuevaTarea = {
        'ID': IDtarea, 
        'Contenido': contenidoTarea, 
        'Estado':'NC'}
    archivo_Tareas['Tareas'].append(nuevaTarea)
    guardar_Modificacion(archivo_Tareas)
    print('La tarea se ha agregado exitosamente. ---- ID: ' + str(IDtarea) )
    return

#Filtro para las tareas, funcion auxiliar de verTareas(estadoRequerido)
def filtrar_Tareas(estado): 
    archivo_Tareas = cargarArchivo()
    estado_buscado = estado.upper()

    #Comprobación de que el estado ingresado por el usuario es válido y existe
    if estado_buscado not in ('C', 'NC', 'EP'): 
        print('-'*20 + ' Ingrese un filtro válido: C, NC, EP ' + '-'*20)
        return

    #Agrupamos las tareas en una nueva lista por estado
    tareas_filtradas = [t for t in archivo_Tareas['Tareas'] if t['Estado'] == estado_buscado]
        
    #Respuesta caso de que la lista quede vacía (no hay tareas)
    if len(tareas_filtradas) == 0:
        print('-'*20 +' No hay tareas que correspondan con ese filtro ' + '-'*20)
        return
    
    #Diccionario para emparejar cada título según el estado correspondiente
    titulos = {
        "C" : " TAREAS COMPLETADAS ",
        "NC": " TAREAS POR COMPLETAR ",
        "EP" : " TAREAS EN PROGRESO "
    }
    titulo = titulos[estado_buscado]
    print("-"*20 + f"{titulo}" + "-"*20)
    for i, t in enumerate(tareas_filtradas, 1): 
        print(f"{i}. [{t['Estado']}] -----  {t['Contenido']}")
    return

#muestra las tareas requeridas 
def ver_Tareas(estadoRequerido=None): 
    archivo_Tareas = cargarArchivo()

    #Comprueba si la lista de tareas está vacía
    if not archivo_Tareas['Tareas']: 
        print("-"*20 + " La lista de tareas está vacía. " + "-"*20)
        return

    if estadoRequerido is None: 
        for i, t in enumerate(archivo_Tareas['Tareas'], 1): 
            print("Las tareas son: ")
            print(f"{i}. [{t['Estado']}] -----  {t['Contenido']}")
        print('-'*20)
        return
    else: 
        filtrar_Tareas(estadoRequerido)

def modificarEstadoTarea():
    
    return
'''
#testing
while run: 
    print('Bienvenido. Que desea hacer?')
    chose = input(' 1. Agregar una tarea \n 2. Ver las tareas \n 3. Salir \n')

    if chose == '1': 
        inputPrueba = input('Ingrese la tarea: ')
        agregar_Tarea(inputPrueba)

    if chose == '2': 
        ver_Tareas()

    if chose == '3': 
        print('Hasta luego...')
        run = False
'''