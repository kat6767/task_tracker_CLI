import json
import os

run = True

#creamos una variable para guardar la ruta (nombre) de nuestro archivo 
ruta_tareas = 'archivo_Tareas.json'

#funcion para guardar las tareas que se agreguen.
def guardar_Modificacion(datos): #datos espera un conjunto para añadir al json. 
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

#el contenidoTarea debe ser string. 
''' MODIFICAR LA CONDICIONAL PARA EVALUAR '''
def agregar_Tarea(contenidoTarea):
    if not contenidoTarea or contenidoTarea == None: 
        print('El contenido de la tarea no puede estar vacío.')
    
    archivo_Tareas = cargarArchivo()
    nuevaTarea = {'Contenido': contenidoTarea, 'Estado':'N/C'}
    archivo_Tareas['Tareas'].append(nuevaTarea)
    guardar_Modificacion(archivo_Tareas)
    print('La tarea se ha agregado exitosamente.')

#muestra las tareas 
'''HACER UN FILTRO PARA TAREAS COMPLETADAS, NO COMPLETADAS Y EN PROCESO '''
def ver_Tareas(estadoBuscado): 
    archivo_Tareas = cargarArchivo()

    #Comprueba si la lista de tareas está vacía
    if not archivo_Tareas['Tareas']: 
        print("-"*20 + " La lista de tareas está vacía. " + "-"*20)

    for i, t in enumerate(archivo_Tareas['Tareas'], 1): 
        print("Las tareas son: ")
        print(f"{i}. [{t['Estado']}] -----  {t['Contenido']}")
        print('-'*20)

    if estadoBuscado == "NC": 
        print("-"*20 + " TO-DO TASKS " + "-"*20)
        for i, t in enumerate(archivo_Tareas['Tareas']): 
            #HAY QUE CREAR FUNCIÓN PARA AVERIGUAR SI NO HAY TAREAS PENDIENTES
            ''' 
            if not t['Estado']: 
                print('No hay tareas pendientes. ¡Yay!')
            '''
            if t['Estado'] == 'N/C':
                print(f"{i}. [{t['Estado']}] -----  {t['Contenido']}")


    
'''
#testing
while run: 
    print('Bienvenido. Que desea hacer?')
    chose = input(' 1. Agregar una tarea \n 2. Ver las tareas \n 3. Salir \n')

    if chose == '1': 
        inputOfDoom = input('Ingrese la tarea: ')
        agregar_Tarea(inputOfDoom)

    if chose == '2': 
        ver_Tareas()

    if chose == '3': 
        print('Hasta luego...')
        run = False
'''