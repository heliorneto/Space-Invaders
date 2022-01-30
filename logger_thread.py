from common import score, sair, inicio_jogo, score_cloud_process, tempo_fim_jogo
import threading, time, socket
sem = threading.Semaphore()

def logger_thread():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 8080))
    s.listen(5)

    inicial = time.time()
    inicio_jogo[0] = inicial
    while sair[0] == False:
        clientsocket, adress = s.accept()

        try:
            nome_arquivo = 'log.txt'
            arquivo = open(nome_arquivo, 'r+')
        except FileNotFoundError:
            arquivo = open(nome_arquivo, 'w+')
        time.sleep(10)
        final = time.time()
        tempo = final-inicial
        score_cloud_process[0] = score[0]
        texto = []
        texto.append(f'\n Score: {score[0]} Time: {tempo}')
        arquivo.writelines(texto)
        clientsocket.send(bytes('{},{},{}'.format(inicio_jogo[0], score_cloud_process[0], tempo_fim_jogo[0]), 'utf-8'))
    tempo_fim_jogo[0] = time.time()
    arquivo.close()