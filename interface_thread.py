from common import sair, pausar, menu, posicaoEnemies, posicaoPlayer, x, block1, block2, block3, block4, score, hiScore
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
                funcResetar()
            if menu[i] == 'P' and cont%2 == 0:
                pausar[0] = True
                cont+=1
            elif menu[i] == 'P' and cont%2 == 1:
                pausar[0] = False
                cont+=1
            sem.release()

def funcResetar():
    for i in range(15):
        posicaoEnemies[i] = ' '

    posicaoPlayer[0] = ' ---'
    x[0] = 1

    block1[0] = 'C'
    block1[1] = 'C'
    block1[2] = 'C'
    block1[3] = 'C'
    block2[0] = 'C'
    block2[1] = 'C'
    block2[2] = 'C'
    block2[3] = 'C'
    block3[0] = 'C'
    block3[1] = 'C'
    block3[2] = 'C'
    block3[3] = 'C'
    block4[0] = 'C'
    block4[1] = 'C'
    block4[2] = 'C'
    block4[3] = 'C'

    score[0] = 0
    hiScore[0] = 0