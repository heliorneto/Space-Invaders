import threading
from display import display
from enemies import enemies
from player import player
from interface_thread import interface_thread
from logger_thread import logger_thread

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

td.join()

print('Fim de jogo')
