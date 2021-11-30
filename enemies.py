import sys, time
from common import posicaoEnemies, comando

def enemies():
    enemies = 'B'
    while comando != 3:
        for i in range(15):
            posicaoEnemies[i] = enemies
            sys.stdout.flush()
            time.sleep(0.5)
