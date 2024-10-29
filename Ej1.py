# Instalar el módulo psutil con: pip install psutil
# psutil es una librería que permite acceder a información sobre los procesos y recursos del sistema.
from tkinter.tix import INTEGER
from xmlrpc.client import boolean

import psutil  # Importamos el módulo psutil, que nos permite interactuar con los procesos del sistema operativo.
bucle = True

while(bucle == True):
    try:
        # Iteramos sobre todos los procesos del sistema utilizando psutil.process_iter(), que devuelve un iterador de procesos.
        notepad = False

        for proc in psutil.process_iter():
            # Obtenemos el nombre del proceso usando proc.name() y su identificador PID con proc.pid.
            processName = proc.name()
            processID = proc.pid

            # Imprimimos el nombre del proceso seguido de su PID.
            print("Nombre:", proc.name())
            print("PID:", proc.pid)
            print("CPU:",proc.cpu_percent())
            print("Memoria:",proc.memory_percent())

            print("--------------------------")
            # Un booleano para ver si el notepad esta en ejecucion
            if (processName == "Notepad.exe"):
                notepad = True

        # Si el notepad esta en ejecucion se muestra un mensaje al final
        if (notepad == True):
            print("\n" + "El proceso Notepad.exe esta en ejecuión" + "\n")
            print("--------------------------")
        # Input para el PID que se desea teminar
        PID_A_Terminar = int(input("Introduzca el PID del proceso que desea terminar"))
        # Bucle que vaya mirando cada PID por el que has introducido
        for proceso in psutil.process_iter():
            try:
                PIDActual = proceso.pid
                # Si el PID del proceso actual coincide con el PID introducido lo intenta terminar
                if (PIDActual) == PID_A_Terminar:
                    proceso.kill()
                    print("Proceso", proceso.name(), "terminado")
            # Si no existe el proceso o no tienes suficiente permiso para terminarlo
            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                print("Error a la hora de eliminar el proceso elegido")
    # Capturamos cualquier excepción que pueda ocurrir durante la iteración de procesos.
    # Por ejemplo, pueden surgir excepciones si un proceso termina mientras se está obteniendo información,
    # si no tenemos permisos suficientes para acceder a la información del proceso, o si el proceso está en estado zombi.
    # except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
    except:
        # Si ocurre cualquier error, imprimimos un mensaje de error.
        print("Error")
    Respuesta = input("Desea seguir el programa (S/N)")
    if Respuesta != "S":
        bucle = False
        print("Programa finalizado")
