from common import sair, comando
import threading
sem = threading.Semaphore()

def interface_thread():
    while True:
        for i in range(100):
            sem.acquire()
            if comando[i] == 'E':
                sair[0] = True
            sem.release()
