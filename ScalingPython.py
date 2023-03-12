import threading
import multiprocessing
import time
import daemon

# Función que simula una tarea pesada y larga
def tarea():
    for i in range(100):
        print("Tarea en proceso...")
        time.sleep(1)
    print("Tarea completada.")

# Ejecución sin hilos ni demonios
print("Ejecución sin hilos ni demonios:")
tarea()

# Ejecución con hilos
print("\nEjecución con hilos:")
hilos = []
for i in range(3):
    hilo = threading.Thread(target=tarea)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

# Ejecución como demonio
print("\nEjecución como demonio:")
def run():
    tarea()

with daemon.DaemonContext():
    run()
