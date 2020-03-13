"""
Ejecución de comandos ADB para realizar tareas de depuración
Geovanny Andrés González - 201719528
Construcción de aplicaciones móviles
Universidad de los Andes - Colombia
"""

import subprocess
import os

#Funciones a utilizar
#Ejecutar un comando en la consola de Windows.
def ejecutar(comando):
    resultado = subprocess.run(comando, shell=True)
    print("[DEPURACION]" + comando)
    resultado.check_returncode()

def cambiarDirectorio(nuevoDirectorio):
    if os.path.exists(nuevoDirectorio):
        os.chdir(nuevoDirectorio)
    else:
        print('Lo sentimos el directorio %s no existe' % nuevoDirectorio)

""" Variables """
# Ruta de la herramienta ADB. Por favor asegurese de utilizar la ruta absoluta donde se encuentran las herramientas
rutaADB = r'C:\Users\Geovanny\AppData\Local\Android\Sdk\platform-tools\\'
adb = r'.\adb.exe shell cmd'

""" Instrucciones """
# Acceder al directorio de ADB
ejecutar('echo {}'.format("Ejecutando procesos"))
ejecutar('echo {}'.format("Accediendo al directorio de ADB"))
cambiarDirectorio(rutaADB) # Se accede a la herramienta ADB
ejecutar('echo {}'.format("Lista de aplicaciones del dispositivo"))
ejecutar('%s package list packages' % adb) #Listar todas las aplicaciones del dispositivo


