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
rutaADB = r'C:\Users\Geovanny\AppData\Local\Android\Sdk\platform-tools\\' #Modificar por el directorio donde se encuentra ADB
adb = r'.\adb.exe'
# Ruta Absoluta del repositorio 
rutaRepositorio = r"C:\Users\Geovanny\Desktop\Univesidad de los Andes\Septimo Semestre - 2020-1\Construccion de Aplicaciones Moviles\Parcial ADB\ADB-Test" 
rutaAPK = rutaRepositorio + '/walpha.apk'
walphaPackage = "com.wolfram.android.alpha"
valorN = -1
eventosAlBack = (201719528 % 4) + 8
indiceScreen = 0
indiceContacto = 0
espera = 1
f = None # Puntero al archivo HTML
nombreCaptura = ""

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

#Generar HTML para documento
def HTMLBase():
    global f
    f = open("InformeHTML.html", "w+")
    f.write('<!DOCTYPE html>')
    f.write('<html lang="es-ES">')
    f.write('  <head>')
    f.write('    <meta charset="utf-8" />')
    f.write('    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
    f.write('    <title>Informe de actividades - Aplicaciones móviles</title>')
    f.write('  </head>')
    f.write('  <body>')
    f.write('    <div class="container-fluid">')

#Cierra el HTML para finalizar su edición
def HTMLCierre():
    f.write('    </div>')
    f.write('    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>')
    f.write('  </body>')
    f.write('</html>')
    f.close()

#Inserta un nuevo elemento de HTML
def HTMLElemento(indice, descripcion, ruta):
    f.write('        <h2>Actividad %d</h2>' % indice)
    f.write('        <h3>%s</h3>' % descripcion)
    f.write('        <img src="./capturas/%s.png" alt="Evidencia Actividad">' % ruta)

def HTMLEvento(indice):
    f.write('        <h1>Evento ejecutado #%d</h1>' % indice)

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
    global nombreCaptura
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
    HTMLElemento(1, "Cambiando a la ventana de inicio", nombreCaptura)
    # Debido a las diferentes versiones de Android la ventana de incio del menú no siempre está disponible 
    # un ejemplo de ello son los dispositivos Huawei con interfaz EMUI
    # Por ello utilizaremos las opciones de bajo nivel para realizar un tap en la primera aplicación de mi móvil
    # al inicio de la pantalla (reloj)
    # Saludos. Geovanny.

    ejecutar('%s shell input tap 110 200' % adb) #Abre la aplicación de reloj
    time.sleep(espera)
    screenShot()
    HTMLElemento(1, "Primera aplicacion disponible en el sistema", nombreCaptura)

#Utilizar long-tap con 3 aplicaciones en la pantalla de inicio 
def actividad2():
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb) #Ir a la primera pantalla de inicio
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb)
    HTMLElemento(2, "Cambiando a la ventana de inicio", nombreCaptura)
    ejecutar('%s shell input swipe 900 1000 100 1000' % adb) #Cambiar de ventana
    ejecutar('%s shell input draganddrop 140 250 140 250 350' % adb)
    time.sleep(espera)
    screenShot()
    HTMLElemento(2, "Long-tap para la primera aplicacion", nombreCaptura)
    ejecutar('%s shell input keyevent KEYCODE_BACK' % adb)
    ejecutar('%s shell input draganddrop 140 530 140 530 350' % adb)
    time.sleep(espera)
    screenShot()
    HTMLElemento(2, "Long-tap para la segunda aplicacion", nombreCaptura)
    ejecutar('%s shell input keyevent KEYCODE_BACK' % adb)
    ejecutar('%s shell input draganddrop 140 800 140 800 350' % adb)
    time.sleep(espera)
    screenShot()
    HTMLElemento(2, "Long-tap para la tercera aplicacion", nombreCaptura)

# Verificar el estado del adaptador WiFi
def actividad3():
    wifi = ejecutar('%s shell settings get global wifi_on' % adb)
    wifi = wifi.strip()
    mensaje = 'El adaptador WiFi esta encendido' if (wifi != '0') else 'El adaptador WiFi esta apagado'
    print(mensaje)
    menuNotificaciones()
    time.sleep(espera)
    screenShot()
    HTMLElemento(3, mensaje, nombreCaptura)    
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
    HTMLElemento(4, mensaje, nombreCaptura)        
    ejecutar('%s shell input keyevent KEYCODE_BACK' % adb)

#Abrir la aplicación de contactos y agregar uno nuevo
def actividad5():
    time.sleep(0.4)
    global indiceContacto
    ejecutarAplicacion('com.android.contacts') #Abrir la aplicación de contactos
    time.sleep(espera)
    screenShot()
    HTMLElemento(5, "Abrir la aplicacion de contactos", nombreCaptura)    
    ejecutar('%s shell input tap 539 2200' % adb)
    time.sleep(espera)
    ejecutar('%s shell input tap 930 2100' % adb)
    ejecutar('%s shell input text contacto%s' % (adb, indiceContacto))
    time.sleep(espera)
    ejecutar('%s shell input tap 430 1100' % adb)
    ejecutar('%s shell input text %s' % (adb, str(indiceContacto) + str(indiceScreen)))
    time.sleep(espera)
    screenShot()
    HTMLElemento(5, "Llenar los datos del contacto", nombreCaptura)    
    ejecutar('%s shell input tap 996 115' % adb)
    screenShot()
    HTMLElemento(5, "Nuevo contacto guardado", nombreCaptura)        
    indiceContacto += 1

#Disminuir el volumen del telefono móvil
def actividad6():
    ejecutar('%s shell media volume --show --stream 3 --set 1' % adb) #Llevar el volumen al minimo
    screenShot()
    HTMLElemento(6, "Volumen minimo", nombreCaptura)        
    time.sleep(espera)
    ejecutar('%s shell media volume --show --stream 3 --set 6' % adb) #Llevar el volumen a la mitad
    screenShot()
    HTMLElemento(6, "Volumen medio", nombreCaptura)        
    time.sleep(espera)
    ejecutar('%s shell media volume --show --stream 3 --set 15' % adb) #Llevar el volumen al maximo
    screenShot()
    HTMLElemento(7, "Volumen alto", nombreCaptura)        

#Encender el adaptador bluetooth
def actividad8():
    ejecutar('%s shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE' % adb)
    time.sleep(espera)
    screenShot()
    HTMLElemento(8, "Solicitar permisos para activar Bluetooth", nombreCaptura)        
    ejecutar('%s shell input tap 800 2200' % adb)
    screenShot()
    HTMLElemento(8, "Bluetooth activado", nombreCaptura)        

#Escribir el nombre en una aplicación con entrada de texto
def actividad9():
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb) #Ir a la primera pantalla de inicio
    ejecutar('%s shell input keyevent KEYCODE_HOME' % adb)
    ejecutar('%s shell input swipe 900 1000 100 1000' % adb) #Cambiar de ventana
    ejecutar('%s shell input tap 140 530' % adb)
    time.sleep(espera)
    screenShot()
    HTMLElemento(9, "Abrir aplicacion de texto", nombreCaptura)
    ejecutar('%s shell input tap 930 2100' % adb)
    time.sleep(espera)
    screenShot()
    HTMLElemento(9, "Crear nota", nombreCaptura)
    time.sleep(espera)
    ejecutar('%s shell input roll 10 10' % adb)
    ejecutar('%s shell input text Geovanny-Andres-Gonzalez' % adb)
    screenShot()
    HTMLElemento(9, "Escribir nombre", nombreCaptura)

actividades = [actividad1, actividad2, actividad3, actividad4, actividad5, actividad6, actividad8, actividad9]

""" Instrucciones """
# Acceder al directorio de ADB
introduccion()
HTMLBase() # Construye el HTML inicial
ejecutar('echo {}'.format("======== Ejecutando procesos ========"))
ejecutar('echo {}'.format("======== Accediendo al directorio de ADB ========"))
cambiarDirectorio(rutaADB) # Se accede a la herramienta ADB

#Listar los dispositivos conectados.
ejecutar('echo {}'.format(" ======== Dispositivos conectados ========"))
dispositivosConectados = ejecutar('%s devices' % adb) #Listar todas las aplicaciones del dispositivo
dispositivosConectados = dispositivosConectados.strip()
if (dispositivosConectados == 'List of devices attached'):
    raise Exception("Por favor conecte un dispositivo fisico y active la depuración para iniciar el proceso")
# Instalar aplicación en el sistema, en este caso se escoge WolframAlpha
ejecutar('echo {}'.format(" ======== Instalando Aplicacion ========"))
ejecutar('%s install -d "%s"' % (adb, rutaAPK))

#Ejecutar la aplicación instalada
ejecutarAplicacion(walphaPackage)
time.sleep(0.5)
screenShot()
HTMLElemento(0, "Ejecutar aplicacion instalada", nombreCaptura)
ejecutar('%s shell input keyevent KEYCODE_BACK' % adb) 
ejecutar('%s shell input keyevent KEYCODE_HOME' % adb)

for i in range (0, valorN): #Ejecutar cuantas actividades hayan solicitado
    j = i % len(actividades) #Ejecutar la actividad en la lista
    HTMLEvento(i + 1) #Imprime el registro del evento en el HTML
    actividades[j]() #Ejecutar
    if (i % eventosAlBack == 0): # Si el numero de eventos para hacer la acción back (X) se alcanzan
        hacerBack()

desintalarAplicacion(walphaPackage)
HTMLCierre() #Suelta el Stream
