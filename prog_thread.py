# script threads_inc_lock.py
import threading
from threading import Thread
from multiprocessing import Process
import time


ls = []


# função que acrescenta um range através de um valor passado na função.
def contador1(n):
    for i in range(1,n+1):
        print(i)
        ls.append(i)
        time.sleep(0.4)

# função que acrescenta um range através de um valor passado na função.
def contador2(n):
    for i in range(6, n+1):
        print(i)
        ls.append(i)
        time.sleep(0.4)

print('iniciando o programa no contador 1')
#threading é um modulo que faz o processamento em paralelo
#target é onde voce declara a função que será utilizado o thread
#Arg é o argumento passado para a função( obs: a virgula após o valor recebido é porq o Thread espera receber uma tupla.
x = threading.Thread(target=contador1,args=(5,))
#x.start é onde é iniciado o processo de thread
x.start()
print('finalizando o programa no contador 1')
x.join()

print('iniciando o programa no contador 2')
y = threading.Thread(target=contador2,args=(10,))
y.start()
print('finalizando o programa no contador 2')

#Join() é utilizado para que só permita avança o codigo após o Thread finalizar

y.join()

print(ls)