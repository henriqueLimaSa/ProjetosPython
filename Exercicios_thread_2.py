from threading import Thread
from time import sleep
import math


##Atividade 1
def primeira_thread(tempo,mensagem1):
    print("inicializando thread")
    sleep(tempo)
    print("primeiro parametro passado foi :{}".format(mensagem1))


exec1 = Thread(target=primeira_thread,args=(2,"A"))
exec2 = Thread(target=primeira_thread,args=(3,"B"))
exec1.start()
exec2.start()
exec1.join()
exec2.join()
print("finalizado o processo!!")



##Atividade2
def primeira_thread(tempo,mensagem1,parametro):
    print("inicializando thread")
    print("O parametro passado foi :{}".format(mensagem1))
    sleep(tempo)
    resultado = math.pow(5,parametro)
    print("O resultado da potência foi: {}".format(resultado))



t1 = Thread(target=primeira_thread,args=(4,"C",2))
t2 = Thread(target=primeira_thread,args=(6,"D",3))
t1.start()
t2.start()
t1.join()
t2.join()
print("finalizado o processo!!")