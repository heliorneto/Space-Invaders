from common import sair, comando, resetar
import threading
sem = threading.Semaphore()

def interface_thread():
    while True:
        for i in range(100):
            sem.acquire()
            if comando[i] == 'E':
                sair[0] = True
            if comando[i] == 'R':
                if resetar[0] == False:
                    resetar[0] = True
                else:
                    resetar[0] = False
            sem.release()
