from common import comando, posicaoPlayer, posicaoEnemies, line1, line2, line3, line4, line5, line6, block1, block2
import threading, time, msvcrt
sem = threading.Semaphore()

def player():
    # Posição da nave
    x = 1
    
    while True:
        for i in range(100):
            
            # Calcula a posição atual do jogador
            sem.acquire()
            jogador = x*' '+'---\n'
            posicaoPlayer[0] = jogador

            # Pega o comando do teclado e move a nave ou atira
            comando[i] = msvcrt.getch().decode("utf-8")
            if comando[i] == '1':
                x -= 1
            elif comando[i] == '2':
                x += 1
            elif comando[i] == '3':
                line1[0] = x*' '+' |'
                time.sleep(0.5)
                # Trajetória do tiro na coluna 1
                if line1[0] == ' |':
                    line1[0] = ''
                    line2[0] = '|'
                    time.sleep(0.5)
                    line2[0] = ' '
                    line3[0] = ' |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    posicaoEnemies[10] = ' '
                    time.sleep(0.5)
                # Trajetória do tiro na coluna 2
                if line1[0] == '  |' and block1[0] == ' ':
                    line1[0] = ''
                    block1[0] = '|'
                    time.sleep(0.5)
                    block1[0] = ' '
                    line3[0] = '  |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[0] = '|   '
                    time.sleep(0.5)
                    line4[0] = '    '
                    line5[0] = '|   '
                    time.sleep(0.5)
                    line5[0] = '    '
                    line6[0] = '|   '
                    time.sleep(0.5)
                    line6[0] = '    '
                # Trajetória do tiro na coluna 2 ao colidir com o bloco
                if line1[0] == '  |':
                    line1[0] = ''
                    block1[0] = ' '
                # Trajetória do tiro na coluna 3
                if line1[0] == '   |' and block1[1] == ' ':
                    line1[0] = ''
                    block1[1] = '|'
                    time.sleep(0.5)
                    block1[1] = ' '
                    line3[0] = '   |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[0] = ' |  '
                    time.sleep(0.5)
                    line4[0] = '    '
                    line5[0] = ' |  '
                    time.sleep(0.5)
                    line5[0] = '    '
                    line6[0] = ' |  '
                    time.sleep(0.5)
                    line6[0] = '    '
                # Trajetória do tiro na coluna 3 ao colidir com o bloco
                if line1[0] == '   |':
                    line1[0] = ''
                    block1[1] = ' '
                # Trajetória do tiro na coluna 4
                if line1[0] == '    |' and block1[2] == ' ':
                    line1[0] = ''
                    block1[2] = '|'
                    time.sleep(0.5)
                    block1[2] = ' '
                    line3[0] = '    |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[0] = '  | '
                    time.sleep(0.5)
                    line4[0] = '    '
                    line5[0] = '  | '
                    time.sleep(0.5)
                    line5[0] = '    '
                    line6[0] = '  | '
                    time.sleep(0.5)
                    line6[0] = '    '
                # Trajetória do tiro na coluna 4 ao colidir com o bloco
                if line1[0] == '    |':
                    line1[0] = ''
                    block1[2] = ' '
                # Trajetória do tiro na coluna 5
                if line1[0] == '     |' and block1[3] == ' ':
                    line1[0] = ''
                    block1[3] = '|'
                    time.sleep(0.5)
                    block1[3] = ' '
                    line3[0] = '     |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[0] = '   |'
                    time.sleep(0.5)
                    line4[0] = '    '
                    line5[0] = '   |'
                    time.sleep(0.5)
                    line5[0] = '    '
                    line6[0] = '   |'
                    time.sleep(0.5)
                    line6[0] = '    '
                # Trajetória do tiro na coluna 5 ao colidir com o bloco
                if line1[0] == '     |':
                    line1[0] = ''
                    block1[3] = ' '
                # Trajetória do tiro na coluna 6
                if line1[0] == '      |':
                    line1[0] = ''
                    line2[1] = '| '
                    time.sleep(0.5)
                    line2[1] = '  '
                    line3[0] = '      |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    posicaoEnemies[11] = ' '
                    time.sleep(0.5)
            sem.release()
            time.sleep(0.5)
