import sys, time, threading
from common import posicaoEnemies, posicaoPlayer, line1, line2, line3, block2, block3, block4, shootComando, sair
from random import randint
sem = threading.Semaphore()


def enemies():
    enemies = 'B'

    while True:
        for i in range(15):
            # Animação para gerar os inimigos na tela
            sem.acquire()
            posicaoEnemies[i] = enemies
            sys.stdout.flush()
            sem.release()
            time.sleep(0.5)
        shootComando[0] = randint(1, 5)
        shoot()

def shoot():
    # Trajetória do tiro inimigo na coluna 1
    if shootComando[0] == 1:
        line3[0] = ' |'
        time.sleep(0.5)
        line3[0] = ' '
        line2[0] = '|'
        time.sleep(0.5)
        line2[0] = ' '
        line1[0] = ' |'
        time.sleep(0.5)
        line1[0] = ' '
        if posicaoPlayer[0] == '---' or posicaoPlayer[0] == ' ---':
            sair[0] = True
    # Trajetória do tiro inimigo na coluna 6
    elif shootComando[0] == 2:
        line3[0] = '      |'
        time.sleep(0.5)
        line3[0] = ' '
        line2[1] = '| '
        time.sleep(0.5)
        line2[1] = '  '
        line1[0] = '      |'
        time.sleep(0.5)
        line1[0] = ' '
        if posicaoPlayer[0] == '    ---' or posicaoPlayer[0] == '     ---' or posicaoPlayer[0] == '      ---':
            sair[0] = True
    # Trajetória do tiro inimigo na coluna 11
    elif shootComando[0] == 3 and block2[3] == ' ':
        line3[0] = '           |'
        time.sleep(0.5)
        line3[0] = ' '
        block2[3] = '|'
        time.sleep(0.5)
        block2[3] = ' '
        line1[0] = '           |'
        time.sleep(0.5)
        line1[0] = ' '
        if posicaoPlayer[0] == '         ---' or posicaoPlayer[0] == '          ---' or posicaoPlayer[0] == '           ---':
            sair[0] = True
    elif shootComando[0] == 3:
        line3[0] = '           |'
        time.sleep(0.5)
        line3[0] = ' '
    # Trajetória do tiro inimigo na coluna 16
    elif shootComando[0] == 4 and block3[2] == ' ':
        line3[0] = '                |'
        time.sleep(0.5)
        line3[0] = ' '
        block3[2] = '|'
        time.sleep(0.5)
        block3[2] = ' '
        line1[0] = '                |'
        time.sleep(0.5)
        line1[0] = ' '
        if posicaoPlayer[0] == '              ---' or posicaoPlayer[0] == '               ---' or posicaoPlayer[0] == '                ---':
            sair[0] = True
    elif shootComando[0] == 4:
        line3[0] = '                |'
        time.sleep(0.5)
        line3[0] = ' '
    # Trajetória do tiro inimigo na coluna 21
    elif shootComando[0] == 5 and block4[1] == ' ':
        line3[0] = '                     |'
        time.sleep(0.5)
        line3[0] = ' '
        block4[1] = '|'
        time.sleep(0.5)
        block4[1] = ' '
        line1[0] = '                     |'
        time.sleep(0.5)
        line1[0] = ' '
        if posicaoPlayer[0] == '                   ---' or posicaoPlayer[0] == '                    ---' or posicaoPlayer[0] == '                     ---':
            sair[0] = True
    elif shootComando[0] == 5:
        line3[0] = '                     |'
        time.sleep(0.5)
        line3[0] = ' '
