import sys, time, threading
from common import posicaoEnemies, comando
sem = threading.Semaphore()


def enemies():
    enemies = 'B'

    while True:
        for i in range(15):
            sem.acquire()
            posicaoEnemies[i] = enemies
            sys.stdout.flush()
            sem.release()
            time.sleep(0.5)
