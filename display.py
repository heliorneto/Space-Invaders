from common import posicaoEnemies, posicaoPlayer, line1, line2, line3, line4, line5, line6, block1, block2, block3, block4, score, hiScore, sair, pausar
import os, time, threading
sem = threading.Semaphore()

def display():

    while True:
        if sair[0] == True:
            break
        sem.acquire()
        screen = f'SCORE {score[0]} HI-SCORE {hiScore[0]}\n\n {posicaoEnemies[0]}{line6[0]}{posicaoEnemies[1]}{line6[1]}{posicaoEnemies[2]}{line6[2]}{posicaoEnemies[3]}{line6[3]}{posicaoEnemies[4]}{line6[4]}\n {posicaoEnemies[5]}{line5[0]}{posicaoEnemies[6]}{line5[1]}{posicaoEnemies[7]}{line5[2]}{posicaoEnemies[8]}{line5[3]}{posicaoEnemies[9]}{line5[4]}\n {posicaoEnemies[10]}{line4[0]}{posicaoEnemies[11]}{line4[1]}{posicaoEnemies[12]}{line4[2]}{posicaoEnemies[13]}{line4[3]}{posicaoEnemies[14]}{line4[4]}\n{line3[0]}\n {line2[0]}{block1[0]}{block1[1]}{block1[2]}{block1[3]}{line2[1]}{block2[0]}{block2[1]}{block2[2]}{block2[3]}{line2[2]}{block3[0]}{block3[1]}{block3[2]}{block3[3]}{line2[3]}{block4[0]}{block4[1]}{block4[2]}{block4[3]}{line2[4]}\n{line1[0]}\n{posicaoPlayer[0]}\n\n E: Sair    R: Resetar    P: Pausar    p: Retomar'
        print(screen)
        while pausar[0]:
            time.sleep(0.1)
        sem.release()
        time.sleep(0.1)
        while pausar[0]:
            time.sleep(0.1)
        os.system('cls')
