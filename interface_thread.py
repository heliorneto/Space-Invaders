from common import menu, sair
import threading, time, msvcrt
sem = threading.Semaphore()

def interface_thread():
    while True:
        for i in range(100):
            sem.acquire()
            menu[i] = msvcrt.getch().decode("utf-8")
            if menu[i] == 'E':
                sair[0] = True
            sem.release()
