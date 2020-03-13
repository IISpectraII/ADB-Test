"""
Ejecución de comandos ADB para realizar tareas de depuración
Geovanny Andrés González - 201719528
Construcción de aplicaciones móviles
Universidad de los Andes - Colombia
"""
""" //======== ========\\"""

import subprocess
import os
import time

""" //======== Variables y funciones a utilizar ========\\"""
# Ruta de la herramienta ADB. Por favor asegurese de utilizar la ruta absoluta donde se encuentran las herramientas
rutaADB = r'C:\Users\Geovanny\AppData\Local\Android\Sdk\platform-tools\\'
adb = r'.\adb.exe'
rutaAPK = r'C:\Users\Geovanny\Desktop\Univesidad de los Andes\Septimo Semestre - 2020-1\Construccion de Aplicaciones Moviles\Parcial ADB\ADB-Test\walpha.apk'
walphaPackage = "com.wolfram.android.alpha"
valorN = -1
eventosAlBack = (201719528 % 4) + 8
rutaRepositorio = r"C:\Users\Geovanny\Desktop\Univesidad de los Andes\Septimo Semestre - 2020-1\Construccion de Aplicaciones Moviles\Parcial ADB\ADB-Test"
indiceScreen = 0
indiceContacto = 0
espera = 1

#Funciones a utilizar

#Mostrar los datos del estudiante y obtener el numero de acciones a ejecutar
def introduccion(): 
    global valorN
    print('Ejecución de comandos ADB para realizar tareas de depuración')
    print('Geovanny Andrés González - 201719528')
    print('Construcción de aplicaciones móviles')
    print('Universidad de los Andes - Colombia \n')
    print('Valor de X para hacer back %d' % eventosAlBack)
    valorN = int(input("Por favor ingrese el número de acciones a ejecutar (N) \n"))

#Ejecutar un comando en la consola de Windows.
#Retorna la salida del proceso en ejecución como una cadena de texto
def ejecutar(comando):    
    resultado = str(subprocess.check_output(comando, shell=True), 'utf-8')
    print(resultado)
    return resultado

#Cambiar el directorio de trabajo de la ejecución del script
def cambiarDirectorio(nuevoDirectorio):
    if os.path.exists(nuevoDirectorio):
        os.chdir(nuevoDirectorio)
    else:
        print('Lo sentimos el directorio %s no existe' % nuevoDirectorio)

#Ejecutar una aplicación con ADB dado su nombre de paquete
def ejecutarAplicacion(nombrePaquete):
    ejecutar('%s shell monkey -p %s -c android.intent.category.LAUNCHER 1' % (adb, nombrePaquete))

def screenShot():
    global indiceScreen
    nombreCaptura = 'pantallazo%d' % indiceScreen
    indiceScreen += 1
    fotos = rutaRepositorio + "/capturas"
    ejecutar('%s shell screencap -p /sdcard/%s.png' % (adb, nombreCaptura)) #Toma la captura de pantalla
    ejecutar('%s pull /sdcard/%s.png "%s"' % (adb, nombreCaptura, fotos))

def desintalarAplicacion(nombrePaquete):
    ejecutar('%s uninstall %s' % (adb, nombrePaquete))

def menuNotificaciones():
    ejecutar('%s shell cmd statusbar expand-notifications' % adb)

def hacerBack():
    ejecutar('%s shell input keyevent KEYCODE_BACK' % adb)

""" //======== Eventos a realizar ========\\"""
# Ir a la ventana de inicio del sistema y ejecutar la primera aplicación disponible en el launcher
def actividad1():
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb) #Cambiar a la ventana de inicio del dispositivo
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb) #Ir a la primera pantalla de inicio
    
    screenShot()
    
    # Debido a las diferentes versiones de Android la ventana de incio del menú no siempre está disponible 
    # un ejemplo de ello son los dispositivos Huawei con interfaz EMUI
    # Por ello utilizaremos las opciones de bajo nivel para realizar un tap en la primera aplicación de mi móvil
    # al inicio de la pantalla (reloj)
    # Saludos. Geovanny.

    ejecutar('%s shell input tap 110 200' % adb) #Abre la aplicación de reloj
    time.sleep(espera)
    screenShot()

#Utilizar long-tap con 3 aplicaciones en la pantalla de inicio 
def actividad2():
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb) #Ir a la primera pantalla de inicio
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb)
    ejecutar('%s shell input swipe 900 1000 100 1000' % adb) #Cambiar de ventana
    ejecutar('%s shell input draganddrop 140 250 140 250 350' % adb)
    time.sleep(espera)
    screenShot()
    ejecutar('%s shell input keyevent KEYCODE_BACK' % adb)
    ejecutar('%s shell input draganddrop 140 530 140 530 350' % adb)
    time.sleep(espera)
    screenShot()
    ejecutar('%s shell input keyevent KEYCODE_BACK' % adb)
    ejecutar('%s shell input draganddrop 140 800 140 800 350' % adb)
    time.sleep(espera)
    screenShot()

# Verificar el estado del adaptador WiFi
def actividad3():
    wifi = ejecutar('%s shell settings get global wifi_on' % adb)
    wifi = wifi.strip()
    mensaje = 'El adaptador WiFi está encendido' if (wifi != '0') else 'El adaptador WiFi está apagado'
    print(mensaje)
    menuNotificaciones()
    time.sleep(espera)
    screenShot()    
    ejecutar('%s shell input keyevent KEYCODE_BACK' % adb)



#Verificar si el telefono se encuentra en modo avión
def actividad4():
    airplane = ejecutar('%s shell settings get global airplane_mode_on' % adb)
    airplane = airplane.strip()
    mensaje = 'El telefono se encuentra en modo avión' if (airplane == '1') else 'El telefono no se encuentra en modo avión'
    print(mensaje)
    menuNotificaciones()
    time.sleep(espera)
    screenShot()    
    ejecutar('%s shell input keyevent KEYCODE_BACK' % adb)

#Abrir la aplicación de contactos y agregar uno nuevo
def actividad5():
    time.sleep(0.4)
    global indiceContacto
    ejecutarAplicacion('com.android.contacts') #Abrir la aplicación de contactos
    time.sleep(espera)
    screenShot()
    ejecutar('%s shell input tap 539 2200' % adb)
    time.sleep(espera)
    ejecutar('%s shell input tap 930 2100' % adb)
    ejecutar('%s shell input text contacto%s' % (adb, indiceContacto))
    time.sleep(espera)
    ejecutar('%s shell input tap 430 1100' % adb)
    ejecutar('%s shell input text %s' % (adb, str(indiceContacto) + str(indiceScreen)))
    time.sleep(espera)
    screenShot()
    ejecutar('%s shell input tap 996 115' % adb)
    screenShot()    
    indiceContacto += 1

#Disminuir el volumen del telefono móvil
def actividad6():
    ejecutar('%s shell media volume --show --stream 3 --set 1' % adb) #Llevar el volumen al minimo
    screenShot()
    time.sleep(espera)
    ejecutar('%s shell media volume --show --stream 3 --set 6' % adb) #Llevar el volumen a la mitad
    screenShot()
    time.sleep(espera)
    ejecutar('%s shell media volume --show --stream 3 --set 15' % adb) #Llevar el volumen al maximo
    screenShot()

#Encender el adaptador bluetooth
def actividad8():
    ejecutar('%s shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE' % adb)
    time.sleep(espera)
    screenShot()
    ejecutar('%s shell input tap 800 2200' % adb)
    screenShot()

#Escribir el nombre en una aplicación con entrada de texto
def actividad9():
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb) #Ir a la primera pantalla de inicio
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb)
    ejecutar('%s shell input swipe 900 1000 100 1000' % adb) #Cambiar de ventana
    ejecutar('%s shell input tap 140 530' % adb)
    time.sleep(espera)
    screenShot()
    ejecutar('%s shell input tap 930 2100' % adb)
    time.sleep(espera)
    screenShot()
    time.sleep(espera)
    ejecutar('%s shell input roll 10 10' % adb)
    ejecutar('%s shell input text Geovanny-Andres-Gonzalez' % adb)
    screenShot()

actividades = [actividad1, actividad2, actividad3, actividad4, actividad5, actividad6, actividad8, actividad9]

""" Instrucciones """
# Acceder al directorio de ADB
introduccion()
ejecutar('echo {}'.format("======== Ejecutando procesos ========"))
ejecutar('echo {}'.format("======== Accediendo al directorio de ADB ========"))
cambiarDirectorio(rutaADB) # Se accede a la herramienta ADB

#Listar los dispositivos conectados.
ejecutar('echo {}'.format(" ======== Dispositivos conectados ========"))
ejecutar('%s devices' % adb) #Listar todas las aplicaciones del dispositivo

# Instalar aplicación en el sistema, en este caso se escoge WolframAlpha
ejecutar('echo {}'.format(" ======== Instalando Aplicacion ========"))
ejecutar('%s install -d "%s"' % (adb, rutaAPK))

#Ejecutar la aplicación instalada
ejecutarAplicacion(walphaPackage)

for i in range (0, valorN): #Ejecutar cuantas actividades hayan solicitado
    j = i % len(actividades) #Ejecutar la actividad en la lista
    actividades[j]()
    if (i % eventosAlBack == 0): # Si el numero de eventos para hacer la acción back (X) se alcanzan
        hacerBack()

desintalarAplicacion(walphaPackage)
