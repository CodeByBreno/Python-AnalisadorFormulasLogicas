# 🔢💡 Interpretador de Fórmulas Lógicas

Esse projeto foi desenvolvido para disciplina de Lógica para Computação, no segundo semestre de 2023, ministrada pelo professor Rosalvo Neto. Ele consiste em um software
com interface gráfica para construção e análise de fórmulas lógicas. Ele permite analisar se a fórmula inserida possui o formato correto e, se tiver, gerar a tabela
verdade completa dela.

<h2><strong>IMPORTANTE!</strong></h2>
O programa precisa de uma abertura e fechamento de parênteses <strong>para cada conectivo</strong> utilizado. Portanto:<br><br>

P ∨ Q     -> Ele não vai reconhecer<br>
(P ∨ Q)   -> Agora sim!<br>

(P ∨ Q → A)   -> Ambíguo, use parentêses<br>
(P ∨ (Q → A)) ou ((P ∨ Q) → A)  -> Agora sim!!<br>

¬(P ∨ Q)  -> Isso é okay, negação não precisa de um parênteses a mais por fora<br>
             (ou seja, não precisa colocar (¬(P ∨ Q)). Na verdade isso vai dar erro)<br>

Se você não colocar parênteses suficientes, ele dirá que a fórmula está mal formada.<br>

Além disso, o programa escreve, ao apresentar a tabela verdade, expressões negadas como 
um "operador negado".<br>
Ou seja, ¬ (P ∧ Q) é representado como (P ¬∧ Q )

<h2><strong>Imagem do Projeto: </strong></h2>

![interface_dark](https://github.com/user-attachments/assets/ef97766c-e1c7-4d0e-a631-17a0137cc0a4)

O projeto conta com uma interface em modo escuro e outra em modo claro também:

<h2><strong>Modo Claro: </strong></h2>

![interface_light](https://github.com/user-attachments/assets/f8ae81fd-22d4-4eb5-b0f9-95af7e0d0871)

Além disso, a tabela verdade gerada é visualizada em outra janela, que também determina se ela é uma <strong>Tautologia, Contradição, Satisfatível ou Continência</strong>

- <strong>Tautologia:</strong> Todas as interpretações são verdadeiras<br><br>
![tautologia](https://github.com/user-attachments/assets/eefb5158-cd9f-45f0-9f67-6cf88b6b65d0)

- <strong>Contradição:</strong> Todas as interpretações são falsas<br><br>
![contradicao](https://github.com/user-attachments/assets/a8723685-b4c5-4ee9-9b59-712eba4178a1)

- <strong>Satisfatível:</strong> Possui ao menos uma interpretação verdadeira<br><br>
![satisfativel2](https://github.com/user-attachments/assets/9f43c215-06c5-4df0-b0ae-382c163b84c8)

- <strong>Continência:</strong> Possui interpretações verdadeiras e falsas<br><br>
![continencia](https://github.com/user-attachments/assets/7f1ae753-31a4-4603-b118-ceb21af5b799)

# ⚙️ Como Executar o Projeto?

Basta ter a versão mais atual do Python instalada no sistema (eu usei a 3.10.4) e instalar o Tkinter (biblioteca usada para desenvolver a interface visual). Para isso, execute o seguinte comando no terminal na pasta do projeto:<br>

<strong>pip install tkinter</strong><br>

Depois de concluído, você deve conseguir executar a aplicação normalmente fazendo:<br>

<strong>python Formula_bem_formulada.p</strong>y<br>

(Novamente, em um terminal na pasta do código)

# 📝 Como o projeto funciona?

Um detalhamento completo tomaria muito espaço, então vou explicar de maneira resumida:<br>

O Analisador determina se a formula está bem formada ou não. Para isso, ele utiliza um Automato (vida imagem na raiz dessa pasta). O programa lê a cadeia inserida pelo usuário,
ignorando os espaços, e cada vez que encontra um carcatere, isso muda o estado do automato de "qi" para "qj". Se, ao terminar de ler a string de entrada, o estado do automato for um estado
final, então a entrada está correta e o programa informa isso.<br>

<h2><strong>Autômato de Reconhecimento da Fórmula (30/04/2023)</strong></h2>

![Automato](https://github.com/user-attachments/assets/54df847d-9bc0-4570-94d1-8f7f55520654)<br>

Se em algum momento for lido um caractere que não representa nenhuma transição para o estado atual (por exemplo, q0 não vai pra lugar nenhum se for lido um "conectivo") ou se ao final
da leitura da string de entrada não estivermos num estado final, o automato rejeita a cadeia e o programa informa que a formula estava mal formulada.<br>

Já o Avaliador é responsável por construir a tabela verdade da expressão inserida. Ele é bemmm mais complicadinho, então vou resumir bastante. Existem vários comentários no 
código, e quem quiser saber mais de como implementei cada etapa pode manda mensagem pelo insta (@_bgab)<br>

Ele funciona em 5 etapas principais:<br>

- <strong>Limpeza</strong> : Pega elementos desnecessários da entrada do usuário (como "não's") em excesso ou
	    espaços em branco e joga isso tudo fora<br>

- <strong>Posfixação</strong> : Posfixa a expressão de entrada usando duas pilhas. Cada vez que é encontrada
         uma proposição, ela é colocada na cadeia final. Cada vez que encontra um conectivo, 
	       ele é colocado na pilha de conectivos. Quando encontra um abre parênteses ou um '¬',
         coloca isso na pilha de "não's".<br>
	       Daí, se ele encontrar um fechamento de parênteses ')', ele remove o conectivo no topo
	       da pilha e coloca na cadeia final. Além disso, remove também um dos abre parânteses na 
         pilha de não's. Se embaixo dele estiver um '¬', coloca ele na expressão final e o remove
         do topo da pilha. Mostrando é mais fácil de entender. Mas isso basicamente termina com
         uma expressão posfixada.

- <strong>Análise Léxica</strong> : Analisa a expressão posfixada e identifica quais são os simbolos e as proposições, 
                   daí monta uma lista com cada um deles. Inclusive, para facilitar a construção da árvore,
                   a lista é invertida antes de ser enviada para etapa seguinte.

- <strong>Geração da Árvore</strong> : Basicamente cria uma árvore binária com os valores lidos da lista de elementos
                      da expressão, gerada na análise léxica. É um algoritmo recursivo, que vai adicionando
		                  os componentes da esquerda para direita. Quando encontra um conectivo, adiciona um 
                      novo nó e chama a função para o nó adicionado. Quando encontra uma proposição, coloca
                      ela e "muda de lado". 
                      Tipo, "∧", "→", "R", "P" e "Q" :<br><br>
                         • usa o conectivo "∧" para criar a raiz da árvore.<br>
			                   • identifica o conectivo "→". Adiciona ele à esquerda e chama a função para esse novo nó (recursividade)<br>
                         • identifica a proposição "R". Adiciona à esquerda de "→" e muda para o lado direito<br>
                         • identifica a proposição "P". Adiciona à direita e volta da recursividade.<br>
                         • Como já foi adicionado algo à esquerda da raiz, ela agora migra para direita e adiciona o "Q"<br>
                         • Fim :) <br><br>
No final, a árvore ficaria assim:

<div align="center">
  <img src="https://github.com/user-attachments/assets/08e6cdb2-17a7-4360-9ca8-03f8c20b138a" width="300">
</div>
  
Além disso, cada nó conta com a informação de se é "conectivo" ou "proposição".<br>
Nessa etapa, a negação de uma expressão é interpretada como o "operador negado" isso foi feito na análise léxica.<br>
Ou seja, ¬ (P ∧ Q) é representado como (P ¬∧ Q )

- <strong>Avaliar a Árvore:</strong> Isso também é feito recursivamente. Basicamente desce toda à esquerda, até encontrar uma proposição. Atribui um 
                     valor lógico para ela de acordo com um padrão matemático, e passa para o lado direito. Se também for uma
                     proposição, atribui um valor e sobe para o nó pai. Dai calcula o resultado da operação ewntre os dois lado 
                     e envia isso para o nó de cima. Vai repetindo esse procedimento até ter analisado todas as operações e, no final,
                     gera uma lista com as interpretações para aquele caso. Um ciclo externo chama essa função 2^N vezes, obtendo uma 
                     interpretação diferente para cada nova possivel combinação de valores lógicos das proposições. Daí, no final
		     tenho uma lista com todas as interpretações, que são exibidas na tela.<br><br>

Essa explicação exclui vários detalhes, como a eliminação de proposições reduzidas, o cálculo do valor das proposições, algumas 
conversões no meio do caminho, vários atributos da árvore e dos nodos, e etc. Mas o essencial é isso ai, qualquer dúvida pode mandar
mensagem



