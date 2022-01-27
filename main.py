import threading, multiprocessing
from display import display
from enemies import enemies
from player import player
from interface_thread import interface_thread
from logger_thread import logger_thread
from cloud_process import cloud_process

td = threading.Thread(target=display)
tp = threading.Thread(target=player)
te = threading.Thread(target=enemies)
ti = threading.Thread(target=interface_thread)
tl = threading.Thread(target=logger_thread)

td.start()
tp.start()
te.start()
ti.start()
tl.start()

if __name__ == "__main__":
    time_init = multiprocessing.Value('i')
    score = multiprocessing.Value('i')
    time_destroyed = multiprocessing.Value('i')
    time_gameover = multiprocessing.Value('i')

    p1 = multiprocessing.Process(target=cloud_process, args=(time_init, score, time_destroyed, time_gameover))
    p1.start()
    p1.join

td.join()


print('Fim de jogo')
