import socket
import threading
from common import sair
sem = threading.Semaphore()

def cloud_process(time_init, score, time_destroyed, time_gameover):
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 8080))

    while True:
        full_msg = ''
        new_msg = True
        while True:
            msg = s.recv(1024)
            if new_msg:
                msglen = int(msg[:HEADERSIZE])
                new_msg = False
            full_msg += msg.decode('utf-8')
            if len(full_msg)-HEADERSIZE == msglen:
                new_msg = True
                full_msg = ''
            msg_divida = msg.decode('utf-8').split(',')
            if msg_divida[0] != '':
                time_init.value = int(float(msg_divida[0]))
            if len(msg_divida) > 1:
                score.value = int(float(msg_divida[1]))
            if len(msg_divida) > 2:
                time_destroyed.value = int(float(msg_divida[2]))
                time_gameover.value = int(float(msg_divida[2]))

            try:
                nome_arquivo = 'cloud_process_log.txt'
                arquivo = open(nome_arquivo, 'r+')
            except FileNotFoundError:
                arquivo = open(nome_arquivo, 'w+')
            texto = []
            texto.append('\n Tempo de início: {}\n Pontuação: {}\n Tempo que a nave foi destruída: {}\n Tempo que acabou o jogo: {}\n'.format(time_init.value, score.value, time_destroyed.value, time_gameover.value))
            arquivo.writelines(texto)
            arquivo.close()
