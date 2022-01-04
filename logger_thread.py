from common import score, sair
import threading, time
sem = threading.Semaphore()

def logger_thread():
    inicial = time.time()
    while sair[0] == False:
        try:
            nome_arquivo = 'log.txt'
            arquivo = open(nome_arquivo, 'r+')
        except FileNotFoundError:
            arquivo = open(nome_arquivo, 'w+')
        time.sleep(10)
        final = time.time()
        tempo = final-inicial
        texto = []
        texto.append(f'\n Score: {score[0]} Time: {tempo}')
        arquivo.writelines(texto)
    arquivo.close()