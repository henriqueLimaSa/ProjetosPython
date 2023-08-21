import time
from threading import Thread
from time import sleep

def aguarda_tempo(aguardando):
    print("iniciando o thread")
    aguardando = time.sleep(2)
    print("aguardando o threading")

print("Chamando a função thread")
recurso = Thread(target=aguarda_tempo,args=("inicializando",))
recurso.start()

recurso.join()
print("Thread finalizado")