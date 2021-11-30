from common import comando, posicaoPlayer

def player():
    x0 = 1
    
    while comando != 3:
        jogador = x0*' '+'---\n'
        posicaoPlayer[0] = jogador
        if comando == 1:
            x0 -= 1
        elif comando == 2:
            x0 += 1
        else:
            break
