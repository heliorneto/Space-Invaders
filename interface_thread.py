from common import sair, comando, pausar, resetar, menu
import threading, msvcrt
sem = threading.Semaphore()

def interface_thread():
    while True:
        cont = 0
        for i in range(100):
            sem.acquire()
            menu[i] = msvcrt.getch().decode("utf-8")
            if menu[i] == 'E':
                sair[0] = True
            if menu[i] == 'R':
                resetar[0] = True
            if menu[i] == 'P' and cont%2 == 0:
                pausar[0] = True
                cont+=1
            elif comando[i] == 'P' and cont%2 == 1:
                pausar[0] = False
                cont+=1
            sem.release()
