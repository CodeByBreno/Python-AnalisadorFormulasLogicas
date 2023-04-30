# ----------------------------------------
# ----------------------------------------
# AVALIADOR DAS FORMULAS 
# ----------------------------------------
# ----------------------------------------

#Simbolos Conectivos = ["∧", "∨", "¬", "→", "↔", "(", ")"]

from Funcoes_Basicas import *;
from Modulos_Auxiliares import *;

class Pilha():

    tamanho : int;
    topo : any;
    conteudo : list[any];
    
    def __init__(self):
        self.tamanho = 0;
        self.topo = "";
        self.conteudo = [];

    def push(self, valor):
        self.topo = valor;
        self.conteudo.append(valor);
        self.tamanho += 1;
        return self.tamanho;

    def pop(self):

        if self.tamanho == 0:
            self.topo = "";
            return -1;
    
        if self.tamanho == 1:
            self.topo = "";
            self.tamanho -= 1;
            return self.conteudo.pop();
    
        if self.tamanho > 1:
            valor_retorno = self.conteudo.pop();
            self.tamanho -= 1;
            self.topo = self.conteudo[self.tamanho-1];
            return valor_retorno;

class No:
    valor: any;
    esquerda: any;
    direita: any;
    depth: int;
    tipo: str;

    def __init__(self, valor, esquerda = None, direita = None):
        self.valor = valor;
        self.esquerda = esquerda;
        self.direita = direita; 
        self.depth = None;

        if len(valor) == 2:
            simbol = valor[1];
        else:
            simbol = valor;
        
        if (eh_conectivo(simbol)):
            self.tipo = "conectivo";
        else:
            self.tipo = "letra";

    def __str__(self):
        return self.valor;

class ArvoreBinaria():
    raiz: No;
    marcadores: Pilha;
    folhas: list;
    altura: int;
    interpretacao: list;
    subformulas: list;

    def __init__(self, no):
        self.raiz = no;
        self.raiz.depth = 0;
        self.marcadores = Pilha();
        self.marcadores.push(no);
        self.folhas = [no];
        self.altura = 0;
        self.interpretacao = [];
        self.subformulas = [];

    #Adição feita em Pré-Ordem
    def adicionar(self, novo_no):  

        self.folhas.append(novo_no);
        novo_no.depth = self.marcadores.topo.depth + 1;

        if novo_no.depth > self.altura:
            self.altura = novo_no.depth;

        if self.marcadores.topo.esquerda == None:
            self.marcadores.topo.esquerda = novo_no;
        else:
            if self.marcadores.topo.direita == None:
                self.marcadores.topo.direita = novo_no;
                self.marcadores.pop();
        
        if (novo_no.tipo == "conectivo"):
            self.marcadores.push(novo_no);

    def exibir_ordem_adicao(self):
        resultado = [];
        for each in self.folhas:
            resultado.append(each);
        
        return resultado;

    def exibir_ordem_profundidade(self):
        resultado = [];

        for c in range(self.altura+1):
            for folha in self.folhas:
                if folha.depth == c:
                    resultado.append(folha);

        return resultado;

    def exibir_conexões(self):
        for folha in self.exibir_ordem_profundidade():
            print(str(folha.depth) + " : " + str(folha.esquerda) + " <--- " + str(folha) + " ---> " + str(folha.direita));

    def obter_letras(self):
        proposicoes = [];

        for folha in self.folhas:

            if folha.tipo == "letra":
                if len(folha.valor) == 2:
                    if not contem(proposicoes, folha.valor[1]):
                        proposicoes.append(folha.valor[1]);
                else:
                    if not contem(proposicoes, folha.valor):
                        proposicoes.append(folha.valor);
        
        return proposicoes;

    def avaliar(self):
        interpretacoes = [];
        proposicoes = self.obter_letras();
        N = pow(2, len(proposicoes));

        for c in range(N):
            self.interpretacao = [];
            self.interpretacao.append(avaliar_corpo(self, self.raiz, c, proposicoes));
            interpretacoes.append(self.interpretacao);
    
        return interpretacoes;

def posfixar(entrada):
    resultado = [];
    pilha_conectivos = Pilha();
    pilha_nots = Pilha();
    componente = '';
    
    #print("Entrada original : " + str(entrada));
    ent_util = redutor_not(eliminar_espacos(entrada));
    #print("Entrada Util: " + str(ent_util));

    for c in range(len(ent_util)):
        
        if ent_util[c] == '(':
            pilha_nots.push('(');
        
        if ent_util[c] == '¬':

            if ent_util[c+1] != '(':
                componente += ent_util[c];
            else:
                pilha_nots.push('¬');
        
        else:
            componente += ent_util[c];

            if eh_letra_valida(ent_util[c]):
                resultado.append(componente);
            
            if eh_conectivo(ent_util[c]):
                pilha_conectivos.push(componente);

            if ent_util[c] == ')':
                resultado.append(pilha_conectivos.pop());
                pilha_nots.pop();

                if (pilha_nots.topo == '¬'):
                    resultado.append(pilha_nots.pop());

            componente = '';

    return resultado;
    
def avaliar_corpo(arvore, no_atual, round, proposicoes):
        
    if (no_atual.esquerda.tipo == "conectivo"):
        esquerda = avaliar_corpo(arvore, no_atual.esquerda, round, proposicoes);
        arvore.interpretacao.append(esquerda);
    else:
        conteudo = no_atual.esquerda.valor;
        if (len(conteudo) == 2):
            esquerda = not valor_logico(proposicoes.index(conteudo[1])+1, round, len(proposicoes));   
        else:
            esquerda = valor_logico(proposicoes.index(conteudo)+1, round, len(proposicoes));   
        arvore.interpretacao.append(esquerda);
    
    if (no_atual.direita.tipo == "conectivo"):
        direita = avaliar_corpo(arvore, no_atual.direita, round, proposicoes);
        arvore.interpretacao.append(direita);
    else:
        conteudo = no_atual.direita.valor;
        if (len(conteudo) == 2):
            direita = not valor_logico(proposicoes.index(conteudo[1])+1, round, len(proposicoes));
        else:
            direita = valor_logico(proposicoes.index(conteudo)+1, round, len(proposicoes));
        arvore.interpretacao.append(direita);
        
    return calculadora_logica(direita, esquerda, no_atual.valor);

def gerar_arvore(entrada):

    entrada_invertida = inverter(entrada);
    print("Entrada Invertida : " + str(entrada_invertida));
    expressoes = quebra_expressao(entrada_invertida);
    print("Expressão Quebrada : ", str(expressoes));
    arvore_principal = None;

    for c in range(len(expressoes)):
        novo_no = No(expressoes[c]);

        if c == 0:
            arvore_principal = ArvoreBinaria(novo_no);
        else:
            arvore_principal.adicionar(novo_no);

    return arvore_principal;

def propriedade_tabela(list):
    N = len(list[0]);
    resultado = '';
    conta_true = 0;
    conta_false = 0;
    print("INTERPRETACAO + " + str(list));
    for interpretacao in list:
        if interpretacao[N-1] == 'V':
            conta_true += 1;
        else:
            conta_false += 1;

    if conta_false == 0:
        resultado += "Tautologia\n";
    if conta_true == 0:
        resultado += "Contraditoria\n";
    if conta_true >= 1:
        resultado += "Satisfativel\n";
    if conta_true >= 1 and conta_false >= 1:
        resultado += "Contingencia\n";
    return resultado;

def obter_expressoes(arvore, no_atual):

    if (no_atual.esquerda.tipo == "conectivo"):
        esquerda = obter_expressoes(arvore, no_atual.esquerda);
    else:
        esquerda = no_atual.esquerda.valor;
        arvore.subformulas.append(esquerda);
        
    if (no_atual.direita.tipo == "conectivo"):
        direita = obter_expressoes(arvore, no_atual.direita);
    else:
        direita = no_atual.direita.valor;
        arvore.subformulas.append(direita);

    subformula = '(' + direita + ' ' + no_atual.valor + ' ' + esquerda + ')';
    #É ao contrário mesmo, pq a inversão inverteu os bagui

    arvore.subformulas.append(subformula);
    return subformula;
