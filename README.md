# 🛸 Space Invaders

## 🔎 Sobre o Projeto

### **Descrição**

Trata-se de uma versão do jogo Space Invaders que tem como objetivo impedir uma invasão de naves alienígenas, utilizando uma arma de defesa para fazer a maior pontuação possível. Foi implementado de forma a ter uma forte interação com o usuário através do teclado, sendo utilizados conceitos de programação concorrente e tendo as seguintes funcionalidades:

- Controle da movimentação da nave de defesa;
- Controle da trajetória dos tiros;
- Movimento dos invasores inimigos;
- Trajetória dos tiros do inimigo;
- Atualização da interface gráfica em tempo real;
- Pausar/Retomar o jogo;
- Sair do jogo;
- Resetar o jogo;
- Gerar um arquivo com a pontuação e tempo de jogo.
- Gerar um arquivo contendo o tempo de início, pontuação, tempo em que a nave foi destruída e tempo de fim de jogo.

### **Ano de implementação**

2021.

### **Responsável**

Hélio Neto.

## 📚 Estrutura de Diretórios

    -> Space-Invaders
        -> common.py
        -> display.py
        -> enemies.py
        -> main.py
        -> player.py
        -> interface_thread.py
        -> logger_thread.py
        -> cloud_process.py

**-> Space-Invaders**

- Pasta onde ficará todo o código do projeto, sendo ele dividido da seguinte forma:

  **-> common.py**

  - Arquivo contendo todas as variáveis globais do projeto.

  **-> display.py**

  - Arquivo contendo a Thread responsável por atualizar a tela gráfico, sendo essa composta por elementos gráficos simples como a letra 'B' representado as naves inimigas, a letra 'C' representando as barreiras entre a nave de defesa e as naves inimigas, o símbolo '---' para representar o jogador e o símbolo '|' para representar os tiros dados pelos inimigos e a nave de defesa. Esse arquivo também contém o código que atualiza a pontuação do jogo. 

  **-> enemies.py**

  - Arquivo contendo a Thread responsável por controlar a movimentação dos inimigos assim como a trajetória dos seus disparos.

  **-> main.py**

  - Processo principal que gerencia o laço principal do jogo. As três Threads são disparadas por esse processo.

  **-> player.py**

  - Arquivo contendo a Thread responsável por controlar a movimentação da nave de defesa assim como a trajetória dos seus disparos. A movimentação da nave e os seus disparos são dados via teclado com a interação do usuário em tempo real. 

  **-> interface_thread.py**

  - Arquivo contendo a Thread responsável por gerenciar o menu de opções do jogo, assim como ler do teclado o comando dado pelo usuário. As ações disponíveis no menu de opções são disparadas via teclado com a interação do usuário em tempo real.

  **-> logger_thread.py**

  - Arquivo contendo a Thread responsável por gerar o arquivo .txt e escrever tanto o score quanto o tempo jogado (que também é calculado nessa thread). O arquivo .txt é atualizado a cada 10 segundos com as novas informações de score e tempo jogado.

  **-> cloud_process.py**

  - Arquivo contendo o processo responsável por gerar o arquivo .txt e escrever o tempo de início, pontuação, tempo em que a nave foi destruída e tempo de fim de jogo (que vem de outro processo). O arquivo .txt é atualizado a cada 5 segundos com as novas informações de score e o processo recebe dados do processo principal via socket.

## 📲 Como Rodar

Para rodar o jogo basta digitar o comando abaixo no terminal:

    python main.py

Obs: Durante a elaboração do projeto foi utilizada biblioteca msvcrt para pegar o comando utilizado pelo usuário em tempo real. A biblioteca fornece acesso a alguns recursos úteis nas plataformas Windows. Caso tenha problema em rodar em um computador com sistema operacional diferente, tentar com um Windows.

## 🎮 Como Jogar

Após digitar o comando para rodar o jogo no seu terminal, a interface gráfica será gerado com todos os elementos gráficos como as naves inimigas, e a nave de defesa. Para controlar a nave de defesa utilizamos as teclas '1' e '2' do teclado, sendo a tecla '1' utilizada para mover a nave para a esquerda e a tecla '2' para mover a nave para a direita. Para efetuar um disparo com a nave de defesa basta se posicionar no local desejado e apertar a tecla '3' no seu teclado. Tal ação efetuará um disparo no local indicado e caso acerte um inimigo aumentará a pontuação atual em 100 pontos, caso acerte um bloco de defesa o mesmo será destruído e caso não acerte nenhum dos alvos o disparo simplemente irá desaparecer no limite superior da tela. Em baixo do ícone do jogador existe um menu de opções sinalizando o que o usuário pode fazer durante a partida. Caso o usuário precione a tecla 'P' após o jogo ter começado, a partida será pausada e para retomar o jogo basta pressionar a tecla 'p'. Caso o usuário pressione a tecla 'R', o jogo será resetado e o score voltará a zerto. Por último, caso o jogador pressione a tecla 'E', o jogo será finalizado.

## 🔧 Ferramentas Utilizadas

- threading -> Biblioteca Python para utilizar os conceitos de programação concorrente.
- time -> Biblioteca Python para indicar as frequências que as Threads serão executadas.
- sys -> Biblioteca Python que fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.
- os -> Biblioteca Python usada no projeto para limpar o terminal e atualizar a interface gráfica da aplicação.
- random -> Biblioteca Python usada para gerar os disparos do inimigo de forma aleatória.
- msvcrt -> Biblioteca Python usada para pegar os comandos digitados pelo usuário no teclado em tempo real.
- socket -> API responsável por tratar a comunicação entre diferentes processos através da criação de um cliente e servidor. Utilizada neste projeto para passar os dados do processo principal para o cloud_process.
- multiprocessing -> Biblioteca semelhante a biblioteca threading que cria um novo processo ao invés de uma threading. Foi usada para criar o cloud_process.

---

_<p style="text-align:center;">Hélio Neto - 2021</p>_
