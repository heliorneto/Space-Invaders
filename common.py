# Lista de posições
posicaoEnemies = [' ']*20
posicaoPlayer = [' ']

# Posição da nave
x = [1]

# Linhas do tabuleiro
line1 = ['']
line2 = [' ', '  ', '  ', '  ', '  ']
line3 = [' ']
line4 = ['    ', '    ', '    ', '    ', '    ']
line5 = ['    ', '    ', '    ', '    ', '    ']
line6 = ['    ', '    ', '    ', '    ', '    ']

# Paredes entre a nave e os inimigos
block1 = ['C', 'C', 'C', 'C']
block2 = ['C', 'C', 'C', 'C']
block3 = ['C', 'C', 'C', 'C']
block4 = ['C', 'C', 'C', 'C']

# Comando de jogo
comando = ['']*100

# Comando de jogo
menu = ['']*100

# Pontuação do jogo e recorde
score = [0]
hiScore = [0]

# Comando para atirar
shootComando = [5]

# Comando para sair do jogo
sair = [False]

# Comando para Pausar
pausar = [False]

# Comando para Resetar
resetar = [False]

# Variáveis para receber no cloud_process
inicio_jogo = [1]
score_cloud_process = [1]
tempo_fim_jogo = [1]