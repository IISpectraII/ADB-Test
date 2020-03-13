# Midterm ADB
Datos del estudiante

    * Geovanny Andrés González Rodríguez
    * Código: 201719528

## Hipotesis y prerrequisitos
Para ejecutar correctamente el script es necesario tener instalado python3 en una versión igual o superior a la 3.6 al igual que la herramienta de depuración _ADB_.

El primer cambio a realizar consiste en insertar la ruta absoluta a la herramienta _ADB_. Para ello localice el .exe y ponga la ruta absoluta de su ejecución. En caso de tener instalado AndroidStudio ejecute la siguiente instrucción en _Ejecutar_ para acceder rapidamente a la localización (Esto último tiene éxito si y solo si las rutas por defecto de AndroidStudio no fueron cambiadas en su instalación) %USERPROFILE%\AppData\Local\Android\Sdk\platform-tools\. Copie la ruta absoluta y reemplace el contenido de la variable _rutaADB_ y agregue finalmente otro caracter de escape \

De igual manera debe cambiar la ruta donde se encuentra el repostorio instalado en su PC, por favor agregue la ruta absoluta en la variable _rutaRepositorio_. El script se ha diseñado para ser ejecutado en SO Windows, no se asegura su efectividad en MacOS o Linux. 

Algunos actividades se realizaron ejecutando instrucciones tap y drag and drop controlando la pantalla del dispositivo. Debido a que todos dispositivos Android no son uniformes algunas actividades están propensas a fallar. El dispositivo móvil de referencia para ejecutar el script es un _Huawei Mate 20 Lite_.

Debido a enunciado asignado, algunas actividades se repetían especificamente el regresar a la pantalla de inicio y agregar contacto por ello solo existen 8 diferentes. Para culminar se deja un archivo HTML con la ejecución del script en mi telefono. Finalmente, el script solo funciona con dispositivos conectados fisicamente, no con emuladores. Si se desea probar la opción de encender el Bluetooth por favor apaguelo en su dispositivo para que la aplicación pueda solicitar correctamente los permisos de encendido

Para ejecutarlo despues de haber realizado las modificaciones respectivas y estar en la carpeta del repositorio use ``python ./script.py``

Saludos cordiales 

Geovanny



