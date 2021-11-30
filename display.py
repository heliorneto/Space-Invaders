from common import posicaoEnemies, posicaoPlayer, comando
import os, time

def display():

    while comando != 3:
        score = 589000
        hiScore = 000000
        screen = f'SCORE {score} HI-SCORE {hiScore}\n\n{posicaoEnemies[0]:^4} {posicaoEnemies[1]:^4} {posicaoEnemies[2]:^4} {posicaoEnemies[3]:^4} {posicaoEnemies[4]:^4}\n{posicaoEnemies[5]:^4} {posicaoEnemies[6]:^4} {posicaoEnemies[7]:^4} {posicaoEnemies[8]:^4} {posicaoEnemies[9]:^4}\n{posicaoEnemies[10]:^4} {posicaoEnemies[11]:^4} {posicaoEnemies[12]:^4} {posicaoEnemies[13]:^4} {posicaoEnemies[14]:^4} {posicaoEnemies[15]:^4}\n\n  CCCC  CCCC  CCCC  CCCC\n{posicaoPlayer[0]}'
        print(screen)
        time.sleep(0.5)
        os.system('cls')
