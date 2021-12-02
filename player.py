from common import comando, posicaoPlayer, shoot
import threading, time, msvcrt
sem = threading.Semaphore()

def player():
    x0 = 1
    
    while True:
        for i in range(100):
            sem.acquire()
            jogador = x0*' '+'---\n'
            posicaoPlayer[0] = jogador
            comando[i] = msvcrt.getch().decode("utf-8")
            print(comando[i])
            if comando[i] == '1':
                x0 -= 1
            elif comando[i] == '2':
                x0 += 1
            elif comando[i] == '3':
                shoot[0] = x0*' '+' |'
            else:
                break
            sem.release()
            time.sleep(0.5)
