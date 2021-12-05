# 🛸 Space Invaders

## 🔎 Sobre o Projeto

### **Descrição**

Trata-se de uma versão do jogo Space Invaders que tem como objetivo impedir uma invasão de naves alienígenas, utilizando uma arma de defesa para fazer a maior pontuação possível. Foi implementado de forma a ter uma forte interação com o usuário através do teclado, sendo utilizados conceitos de programação concorrente e tendo as seguintes funcionalidades:

- Controle da movimentação da nave de defesa;
- Controle da trajetória dos tiros;
- Movimento dos invasores inimigos;
- Trajetória dos tiros do inimigo;
- Atualização da interface gráfica em tempo real.

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

## 📲 Como Rodar

Para rodar o jogo basta digitar o comando abaixo no terminal:

    python main.py

Obs: Durante a elaboração do projeto foi utilizada biblioteca msvcrt para pegar o comando utilizado pelo usuário em tempo real. A biblioteca fornece acesso a alguns recursos úteis nas plataformas Windows. Caso tenha problema em rodar em um computador com sistema operacional diferente, tentar com um Windows.

## 🎮 Como Jogar

Após digitar o comando para rodar o jogo no seu terminal, a interface gráfica será gerado com todos os elementos gráficos como as naves inimigas, e a nave de defesa. Para controlar a nave de defesa utilizamos as teclas '1' e '2' do teclado, sendo a tecla '1' utilizada para mover a nave para a esquerda e a tecla '2' para mover a nave para a esquerda. Para efetuar um disparo com a nave de defesa basta se posicionar no local desejado e apertar a tecla '3' no seu teclado. Tal ação efetuará um disparo no local indicado e caso acerte um inimigo aumentará a pontuação atual em 100 pontos, caso acerte um bloco de defesa o mesmo será destruído e caso não acerte nenhum dos alvos o disparo simplemente irá desaparecer no limite superior da tela. 

## 🔧 Ferramentas Utilizadas

- threading -> Biblioteca Python para utilizar os conceitos de programação concorrente.
- time -> Biblioteca Python para indicar as frequências que as Threads serão executadas.
- sys -> Biblioteca Python que fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.
- os -> Biblioteca Python usada no projeto para limpar o terminal e atualizar a interface gráfica da aplicação.
- random -> Biblioteca Python usada para gerar os disparos do inimigo de forma aleatória.
- msvcrt -> Biblioteca Python usada para pegar os comandos digitados pelo usuário no teclado em tempo real.

---

_<p style="text-align:center;">Hélio Neto - 2021</p>_
