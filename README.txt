----------------------------------------------------------------
!!! IMPORTANTE !!!
----------------------------------------------------------------

O programa precisa de uma abertura e fechamento de parênteses para
cada conectivo utilizado. Portanto:

P ∨ Q     -> Ele não vai reconhecer
(P ∨ Q)   -> Agora sim!

(P ∨ Q → A)   -> Ambíguo, use parentêses
(P ∨ (Q → A)) ou ((P ∨ Q) → A)  -> Agora sim!!

¬(P ∨ Q)  -> Isso é okay, negação não precisa de um parênteses a mais por fora
             (ou seja, não precisa colocar (¬(P ∨ Q)). Na verdade isso vai dar erro)

Se você não colocar parênteses suficientes, ele dirá que a fórmula está mal formada.

Além disso, o programa escreve, ao apresentar a tabela verdade, expressões negadas como 
um "operador negado". Ou seja, ¬ (P ∧ Q) é representado como (P ¬∧ Q )

----------------------------------------------------------------
Como executar o projeto?
----------------------------------------------------------------

Basta ter a versão mais atual do Python instalada no sistema (eu usei a 3.10.4)
e instalar o Tkinter (biblioteca usada para desenvolver a interface visual). Para isso,
rode:

pip install tkinter

Depois de concluído, você deve conseguir executar a aplicação normalmente fazendo:

python Formula_bem_formulada.py

Na pasta onde o arquivo supracitado estiver

----------------------------------------------------------------
Como funciona?
----------------------------------------------------------------

Um detalhamento completo tomaria muito espaço, então vou explicar de maneira resumida:

O Analisador determina se a formula está bem formada ou não. Para isso, ele utiliza 
um Automato (vida imagem na raiz dessa pasta). O programa lê a cadeia inserida pelo usuário,
ignorando os espaços, e cada vez que encontra um carcatere, isso muda o estado do automato de 
"qi" para "qj". Se, ao terminar de ler a string de entrada, o estado do automato for um estado
final, então a entrada está correta e o programa informa isso.
Se em algum momento for lido um caractere que não representa nenhuma transição para o estado
atual (por exemplo, q0 não vai pra lugar nenhum se for lido um "conectivo") ou se ao final
da leitura da string de entrada não estivermos num estado final, o automato rejeita a cadeia
e o programa informa que a formula estava mal formulada.

Já o Avaliador é responsável por construir a tabela verdade da expressão inserida. Ele é 
bemmm mais complicadinho, então vou resumir bastante. Existem vários comentários no 
código, e quem quiser saber mais de como implementei cada etapa pode manda mensagem pelo 
insta (@_bgab) ou whatsapp ( 87988129981 )

Ele funciona em 5 etapas principais:

- Limpeza : Pega elementos desnecessários da entrada do usuário (como "não's") em excesso ou
	    espaços em branco e joga isso tudo fora

- Posfixação : Posfixa a expressão de entrada usando duas pilhas. Cada vez que é encontrada
               uma proposição, ela é colocada na cadeia final. Cada vez que encontra um conectivo, 
	       ele é colocado na pilha de conectivos. Quando encontra um abre parênteses ou um '¬',
               coloca isso na pilha de "não's".
	       Daí, se ele encontrar um fechamento de parênteses ')', ele remove o conectivo no topo
	       da pilha e coloca na cadeia final. Além disso, remove também um dos abre parânteses na 
               pilha de não's. Se embaixo dele estiver um '¬', coloca ele na expressão final e o remove
               do topo da pilha. Mostrando é mais fácil de entender. Mas isso basicamente termina com
               uma expressão posfixada.

- Análise Léxica : Analisa a expressão posfixada e identifica quais são os simbolos e as proposições, 
                   daí monta uma lista com cada um deles. Inclusive, para facilitar a construção da árvore,
                   a lista é invertida antes de ser enviada para etapa seguinte.

- Geração da Árvore : Basicamente cria uma árvore binária com os valores lidos da lista de elementos
                      da expressão, gerada na análise léxica. É um algoritmo recursivo, que vai adicionando
		      os componentes da esquerda para direita. Quando encontra um conectivo, adiciona um 
                      novo nó e chama a função para o nó adicionado. Quando encontra uma proposição, coloca
                      ela e "muda de lado". 
                      Tipo, "∧", "→", "R", "P" e "Q" : 
                         - usa o conectivo "∧" para criar a raiz da árvore.
			 - identifica o conectivo "→". Adiciona ele à esquerda e chama a função para esse novo nó (recursividade)
                         - identifica a proposição "R". Adiciona à esquerda de "→" e muda para o lado direito
                         - identifica a proposição "P". Adiciona à direita e volta da recursividade.
                         - Como já foi adicionado algo à esquerda da raiz, ela agora migra para direita e adiciona o "Q"
                         - Fim :) 

	              Termina assim:

                                    ∧
				  /   \								
                                 →     Q
                                / \
                               R   P

                      Além disso, cada nó conta com a informação de se é "conectivo" ou "proposição". Nessa etapa, a negação de uma 
	              expressão é interpretada como o "operador negado" isso foi feito na análise léxica. Ou seja, ¬ (P ∧ Q) é 
                      representado como (P ¬∧ Q )

- Avaliar a Árvore : Isso também é feito recursivamente. Basicamente desce toda à esquerda, até encontrar uma proposição. Atribui um 
                     valor lógico para ela de acordo com um padrão matemático, e passa para o lado direito. Se também for uma
                     proposição, atribui um valor e sobe para o nó pai. Dai calcula o resultado da operação ewntre os dois lado 
                     e envia isso para o nó de cima. Vai repetindo esse procedimento até ter analisado todas as operações e, no final,
                     gera uma lista com as interpretações para aquele caso. Um ciclo externo chama essa função 2^N vezes, obtendo uma 
                     interpretação diferente para cada nova possivel combinação de valores lógicos das proposições. Daí, no final
		     tenho uma lista com todas as interpretações, que são exibidas na tela.

Essa explicação exclui vários detalhes, como a eliminação de proposições reduzidas, o cálculo do valor das proposições, algumas 
conversões no meio do caminho, vários atributos da árvore e dos nodos, e etc. Mas o essencial é isso ai, qualquer dúvida pode mandar
mensagem

--------------------------------------------------------------
Breno Gabriel                                        30/04/23
