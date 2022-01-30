from common import score, sair, inicio_jogo, score_cloud_process, tempo_fim_jogo
import threading, time, socket
sem = threading.Semaphore()

def logger_thread():
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 8080))
    s.listen(5)

    inicial = time.time()
    inicio_jogo[0] = inicial
    while sair[0] == False:
        clientsocket, adress = s.accept()

        msg = '{},{},{}'.format(inicio_jogo[0], score_cloud_process[0], tempo_fim_jogo[0])

        clientsocket.send(bytes(msg, 'utf-8'))
        while sair[0] == False:
            time.sleep(5)
            try:
                nome_arquivo = 'log.txt'
                arquivo = open(nome_arquivo, 'r+')
            except FileNotFoundError:
                arquivo = open(nome_arquivo, 'w+')
            final = time.time()
            tempo = final-inicial
            inicio_jogo[0] = inicial
            score_cloud_process[0] = score[0]
            texto = []
            texto.append(f'\n Score: {score[0]} Time: {tempo}')
            arquivo.writelines(texto)
            score_cloud_process[0] = score[0]
            msg = '{},{},{}'.format(inicio_jogo[0], score_cloud_process[0], tempo_fim_jogo[0])
            clientsocket.send(bytes(msg, 'utf-8'))
    tempo_fim_jogo[0] = time.time()
    msg = '{},{},{}'.format(inicio_jogo[0], score_cloud_process[0], tempo_fim_jogo[0])
    clientsocket.send(bytes(msg, 'utf-8'))
    arquivo.close()