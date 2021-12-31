from common import sair, comando, pausar
import threading
sem = threading.Semaphore()

def interface_thread():
    while True:
        cont = 0
        for i in range(100):
            sem.acquire()
            if comando[i] == 'E':
                sair[0] = True
            if comando[i] == 'P' and cont%2 == 0:
                pausar[0] = True
                cont+=1
            elif comando[i] == 'P' and cont%2 == 1:
                pausar[0] = False
                cont+=1
            sem.release()
