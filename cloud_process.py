import threading
sem = threading.Semaphore()

def cloud_process(time_init, score, time_destroyed, time_gameover):

    sem.acquire()
    time_init.value = 12
    score.value = 25
    time_destroyed.value = 3
    time_gameover.value = 45

    try:
        nome_arquivo = 'cloud_process_log.txt'
        arquivo = open(nome_arquivo, 'r+')
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
    texto = []
    texto.append('\n Tempo de início: {}\n Pontuação: {}\n Tempo que a nave foi destruída: {}\n Tempo que acabou o jogo: {}\n'.format(time_init.value, score.value, time_destroyed.value, time_gameover.value))
    arquivo.writelines(texto)
    line = arquivo.readlines()
    line = line[:-1]
    arquivo.close()
    sem.release()
