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

#Simbolos Conectivos = ["∧", "∨", "¬", "→", "↔", "(", ")"]

def pow(valor, expoente):
    multiplicador = valor;
    valor = 1;
    for i in range(expoente):
        valor *= multiplicador;
    return valor;

def valor_logico(level, round, size):
    fator = pow(2, size-level);
    fator = round // fator;
    return is_even(fator);

def is_even(numero):
    return numero%2 == 0;

def contem(lista, valor):
    if len(lista) == 0:
        return False;

    for each in lista:
        if (each == valor):
            return True;
    return False;

def eh_conectivo (entrada):
    conectivos = ['∧', '∨', '→', '↔'];

    for simbolo in conectivos:
        if entrada == simbolo:
            return True;

    return False;

def eh_letra_valida (entrada):
    valor_ascii = ord(entrada);
    return valor_ascii >= 65 and valor_ascii <= 90;

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

def eliminar_espacos(entrada):
    lista = entrada.split(" ");
    return ("").join(lista);

def redutor_not(entrada):
    conta_not = 0;
    valor_inicial = 0;
    teve_not_antes = False;
    resultado = '';

    for c in range(len(entrada)):

        if entrada[c] == '¬':
            conta_not += 1;

            if teve_not_antes == False:
                primeiro_not = c;
                teve_not_antes = True;
    
        else:
            if teve_not_antes:
                if conta_not%2 == 0:
                    resultado += entrada[valor_inicial:primeiro_not] + entrada[c];
                else:
                    resultado += entrada[valor_inicial:primeiro_not] + "¬" + entrada[c];
                
                valor_inicial = c+1;
                teve_not_antes = False;
                conta_not = 0;

    resultado += entrada[valor_inicial:len(entrada)]
    return resultado;

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

    def __init__(self, no):
        self.raiz = no;
        self.raiz.depth = 0;
        self.marcadores = Pilha();
        self.marcadores.push(no);
        self.folhas = [no];
        self.altura = 0;
        self.interpretacao = [];

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

def calculadora_logica(P, Q, operador):

    if (operador == "∧"):
        return P and Q;
    if (operador == "∨"):
        return P or Q;
    if (operador == "→"):
        if (P and not Q): return False;
        else: return True;
    if (operador == "↔"):
        if (P == Q): return True;
        else: return False;
    
    if (operador == "¬∧"):
        return not (P and Q);
    if (operador == "¬∨"):
        return not (P or Q);
    if (operador == "¬→"):
        if (P and not Q): return True;
        else: return False;
    if (operador == "¬↔"):
        if (P == Q): return False;
        else: return True;

def inverter(entrada_lista):
    entrada = "".join(entrada_lista);
    resultado = '';
    for i in range(len(entrada)):
        resultado += entrada[len(entrada) - 1 - i];
    return resultado;

def quebra_expressao(entrada):
    N = len(entrada);
    simbolos = [];
    for c in range(N):

        if (eh_letra_valida(entrada[c])):
            if (c + 1 < N) and entrada[c+1] == '¬':
                simbolos.append('¬' + entrada[c]);
            else:
                simbolos.append(entrada[c]);
        
        if (eh_conectivo(entrada[c])):
            if ((c > 0) and entrada[c-1] == '¬') and (not eh_letra_valida(entrada[c-2]) or c-2 < 0):
                simbolos.append('¬' + entrada[c]);
            else:
                simbolos.append(entrada[c]);

    return simbolos;

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

#obter_expressoes(arvore_expressao, arvore_expressao.raiz);
subformulas = [];
def obter_expressoes(arvore, no_atual):
    global subformulas
    
    if (no_atual.esquerda.tipo == "conectivo"):
        esquerda = obter_expressoes(arvore, no_atual.esquerda);
    else:
        esquerda = no_atual.esquerda.valor;
        subformulas.append(esquerda);
        
    if (no_atual.direita.tipo == "conectivo"):
        direita = obter_expressoes(arvore, no_atual.direita);
    else:
        direita = no_atual.direita.valor;
        subformulas.append(direita);

    subformula = '(' + direita + ' ' + no_atual.valor + ' ' + esquerda + ')';
    #É ao contrário mesmo, pq a inversão inverteu os bagui

    subformulas.append(subformula);
    return subformula;

#print("".join(posfixar("¬(R∨T)"))); 
#print("".join(posfixar("¬¬(P∨Q)")));
#print("".join(posfixar("¬(A→¬(B∨Q))")));
#print("".join(posfixar("(((R→¬¬¬B)↔¬¬¬¬((¬R∨T)↔A))∨¬T)")));
#print("".join(posfixar("¬(¬(P→Q)↔A)∧(¬B∨¬C))")));

expressao = "¬(A→¬(B∨Q))";

expressao_posfix = posfixar(expressao);
print("Expressão Posfixada : " + str(expressao_posfix));

arvore_expressao = gerar_arvore(expressao_posfix);

#for each in arvore_expressao.exibir_ordem_profundidade():
#    print(str(each.depth) + " : " + str(each));

print("Arvore 1 ---------------------------------- ");
print("Expressão: " + expressao);
print("Altura da Arvore : " + str(arvore_expressao.altura));
arvore_expressao.exibir_conexões();

print("Ordem de Adição: ");
for folha in arvore_expressao.exibir_ordem_adicao():
    print(str(folha) + ' : ' + str(folha.tipo));

print("Todas as Expressões: ");
obter_expressoes(arvore_expressao, arvore_expressao.raiz);
print(subformulas);

print("TODAS AS PROPOSICOES: ");
print(arvore_expressao.obter_letras());

print("INTERPRETAÇÕES: ");
for each in arvore_expressao.avaliar():
    print(each);