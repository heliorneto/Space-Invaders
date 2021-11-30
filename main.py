import threading
from display import display
from enemies import enemies
from player import player

td = threading.Thread(target=display)
tp = threading.Thread(target=player)
te = threading.Thread(target=enemies)

td.start()
tp.start()
te.start()

td.join()
tp.join()
te.join()
