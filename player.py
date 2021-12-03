from common import comando, posicaoPlayer, posicaoEnemies, line1, line2, line3, line4, line5, line6, block1, block2, block3, block4, score
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
                    score[0] += 100
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
                    score[0] += 100
                # Trajetória do tiro na coluna 7
                if line1[0] == '       |':
                    line1[0] = ''
                    line2[1] = ' |'
                    time.sleep(0.5)
                    line2[1] = '  '
                    line3[0] = '       |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[1] = '|   '
                    time.sleep(0.5)
                    line4[1] = '    '
                    line5[1] = '|   '
                    time.sleep(0.5)
                    line5[1] = '    '
                    line6[1] = '|   '
                    time.sleep(0.5)
                    line6[1] = '    '
                # Trajetória do tiro na coluna 8
                if line1[0] == '        |' and block2[0] == ' ':
                    line1[0] = ''
                    block2[0] = '|'
                    time.sleep(0.5)
                    block2[0] = ' '
                    line3[0] = '        |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[1] = ' |  '
                    time.sleep(0.5)
                    line4[1] = '    '
                    line5[1] = ' |  '
                    time.sleep(0.5)
                    line5[1] = '    '
                    line6[1] = ' |  '
                    time.sleep(0.5)
                    line6[1] = '    '
                # Trajetória do tiro na coluna 8 ao colidir com o bloco
                if line1[0] == '        |':
                    line1[0] = ''
                    block2[0] = ' '
                # Trajetória do tiro na coluna 9
                if line1[0] == '         |' and block2[1] == ' ':
                    line1[0] = ''
                    block2[1] = '|'
                    time.sleep(0.5)
                    block2[1] = ' '
                    line3[0] = '         |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[1] = '  | '
                    time.sleep(0.5)
                    line4[1] = '    '
                    line5[1] = '  | '
                    time.sleep(0.5)
                    line5[1] = '    '
                    line6[1] = '  | '
                    time.sleep(0.5)
                    line6[1] = '    '
                # Trajetória do tiro na coluna 9 ao colidir com o bloco
                if line1[0] == '         |':
                    line1[0] = ''
                    block2[1] = ' '
                # Trajetória do tiro na coluna 10
                if line1[0] == '          |' and block2[2] == ' ':
                    line1[0] = ''
                    block2[2] = '|'
                    time.sleep(0.5)
                    block2[2] = ' '
                    line3[0] = '          |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[1] = '   |'
                    time.sleep(0.5)
                    line4[1] = '    '
                    line5[1] = '   |'
                    time.sleep(0.5)
                    line5[1] = '    '
                    line6[1] = '   |'
                    time.sleep(0.5)
                    line6[1] = '    '
                # Trajetória do tiro na coluna 10 ao colidir com o bloco
                if line1[0] == '          |':
                    line1[0] = ''
                    block2[2] = ' '
                # Trajetória do tiro na coluna 11
                if line1[0] == '           |' and block2[3] == ' ':
                    line1[0] = ''
                    block2[3] = '|'
                    time.sleep(0.5)
                    block2[3] = ' '
                    line3[0] = '           |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    posicaoEnemies[12] = ' '
                    score[0] += 100
                # Trajetória do tiro na coluna 11 ao colidir com o bloco
                if line1[0] == '           |':
                    line1[0] = ''
                    block2[3] = ' '
                # Trajetória do tiro na coluna 12
                if line1[0] == '            |':
                    line1[0] = ''
                    line2[2] = '| '
                    time.sleep(0.5)
                    line2[2] = '  '
                    line3[0] = '            |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[2] = '|   '
                    time.sleep(0.5)
                    line4[2] = '    '
                    line5[2] = '|   '
                    time.sleep(0.5)
                    line5[2] = '    '
                    line6[2] = '|   '
                    time.sleep(0.5)
                    line6[2] = '    '
                # Trajetória do tiro na coluna 13
                if line1[0] == '             |':
                    line1[0] = ''
                    line2[2] = ' |'
                    time.sleep(0.5)
                    line2[2] = '  '
                    line3[0] = '             |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[2] = ' |  '
                    time.sleep(0.5)
                    line4[2] = '    '
                    line5[2] = ' |  '
                    time.sleep(0.5)
                    line5[2] = '    '
                    line6[2] = ' |  '
                    time.sleep(0.5)
                    line6[2] = '    '
                # Trajetória do tiro na coluna 14
                if line1[0] == '              |' and block3[0] == ' ':
                    line1[0] = ''
                    block3[0] = '|'
                    time.sleep(0.5)
                    block3[0] = ' '
                    line3[0] = '              |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[2] = '  | '
                    time.sleep(0.5)
                    line4[2] = '    '
                    line5[2] = '  | '
                    time.sleep(0.5)
                    line5[2] = '    '
                    line6[2] = '  | '
                    time.sleep(0.5)
                    line6[2] = '    '
                # Trajetória do tiro na coluna 14 ao colidir com o bloco
                if line1[0] == '              |':
                    line1[0] = ''
                    block3[0] = ' '
                # Trajetória do tiro na coluna 15
                if line1[0] == '               |' and block3[1] == ' ':
                    line1[0] = ''
                    block3[1] = '|'
                    time.sleep(0.5)
                    block3[1] = ' '
                    line3[0] = '               |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[2] = '   |'
                    time.sleep(0.5)
                    line4[2] = '    '
                    line5[2] = '   |'
                    time.sleep(0.5)
                    line5[2] = '    '
                    line6[2] = '   |'
                    time.sleep(0.5)
                    line6[2] = '    '
                # Trajetória do tiro na coluna 15 ao colidir com o bloco
                if line1[0] == '               |':
                    line1[0] = ''
                    block3[1] = ' '
                # Trajetória do tiro na coluna 16
                if line1[0] == '                |' and block3[2] == ' ':
                    line1[0] = ''
                    block3[2] = '|'
                    time.sleep(0.5)
                    block3[2] = ' '
                    line3[0] = '                |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    posicaoEnemies[13] = ' '
                    score[0] += 100
                # Trajetória do tiro na coluna 16 ao colidir com o bloco
                if line1[0] == '                |':
                    line1[0] = ''
                    block3[2] = ' '
                # Trajetória do tiro na coluna 17
                if line1[0] == '                 |' and block3[3] == ' ':
                    line1[0] = ''
                    block3[3] = '|'
                    time.sleep(0.5)
                    block3[3] = ' '
                    line3[0] = '                 |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[3] = '|   '
                    time.sleep(0.5)
                    line4[3] = '    '
                    line5[3] = '|   '
                    time.sleep(0.5)
                    line5[3] = '    '
                    line6[3] = '|   '
                    time.sleep(0.5)
                    line6[3] = '    '
                # Trajetória do tiro na coluna 17 ao colidir com o bloco
                if line1[0] == '                 |':
                    line1[0] = ''
                    block3[3] = ' '
                # Trajetória do tiro na coluna 18
                if line1[0] == '                  |':
                    line1[0] = ''
                    line2[3] = '| '
                    time.sleep(0.5)
                    line2[3] = '  '
                    line3[0] = '                  |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[3] = ' |  '
                    time.sleep(0.5)
                    line4[3] = '    '
                    line5[3] = ' |  '
                    time.sleep(0.5)
                    line5[3] = '    '
                    line6[3] = ' |  '
                    time.sleep(0.5)
                    line6[3] = '    '
                # Trajetória do tiro na coluna 19
                if line1[0] == '                   |':
                    line1[0] = ''
                    line2[3] = ' |'
                    time.sleep(0.5)
                    line2[3] = '  '
                    line3[0] = '                   |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[3] = '  | '
                    time.sleep(0.5)
                    line4[3] = '    '
                    line5[3] = '  | '
                    time.sleep(0.5)
                    line5[3] = '    '
                    line6[3] = '  | '
                    time.sleep(0.5)
                    line6[3] = '    '
                # Trajetória do tiro na coluna 20
                if line1[0] == '                    |' and block4[0] == ' ':
                    line1[0] = ''
                    block4[0] = '|'
                    time.sleep(0.5)
                    block4[0] = ' '
                    line3[0] = '                    |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[3] = '   |'
                    time.sleep(0.5)
                    line4[3] = '    '
                    line5[3] = '   |'
                    time.sleep(0.5)
                    line5[3] = '    '
                    line6[3] = '   |'
                    time.sleep(0.5)
                    line6[3] = '    '
                # Trajetória do tiro na coluna 20 ao colidir com o bloco
                if line1[0] == '                    |':
                    line1[0] = ''
                    block4[0] = ' '
                # Trajetória do tiro na coluna 21
                if line1[0] == '                     |' and block4[1] == ' ':
                    line1[0] = ''
                    block4[1] = '|'
                    time.sleep(0.5)
                    block4[1] = ' '
                    line3[0] = '                     |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    posicaoEnemies[14] = ' '
                    score[0] += 100
                # Trajetória do tiro na coluna 21 ao colidir com o bloco
                if line1[0] == '                     |':
                    line1[0] = ''
                    block4[1] = ' '
                # Trajetória do tiro na coluna 22
                if line1[0] == '                      |' and block4[2] == ' ':
                    line1[0] = ''
                    block4[2] = '|'
                    time.sleep(0.5)
                    block4[2] = ' '
                    line3[0] = '                      |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[4] = '|   '
                    time.sleep(0.5)
                    line4[4] = '    '
                    line5[4] = '|   '
                    time.sleep(0.5)
                    line5[4] = '    '
                    line6[4] = '|   '
                    time.sleep(0.5)
                    line6[4] = '    '
                # Trajetória do tiro na coluna 22 ao colidir com o bloco
                if line1[0] == '                      |':
                    line1[0] = ''
                    block4[2] = ' '
                # Trajetória do tiro na coluna 23
                if line1[0] == '                       |' and block4[3] == ' ':
                    line1[0] = ''
                    block4[3] = '|'
                    time.sleep(0.5)
                    block4[3] = ' '
                    line3[0] = '                       |'
                    time.sleep(0.5)
                    line3[0] = ' '
                    line4[4] = ' |  '
                    time.sleep(0.5)
                    line4[4] = '    '
                    line5[4] = ' |  '
                    time.sleep(0.5)
                    line5[4] = '    '
                    line6[4] = ' |  '
                    time.sleep(0.5)
                    line6[4] = '    '
                # Trajetória do tiro na coluna 23 ao colidir com o bloco
                if line1[0] == '                       |':
                    line1[0] = ''
                    block4[3] = ' '
            sem.release()
            time.sleep(0.5)
