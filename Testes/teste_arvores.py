
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

def eh_conectivo (entrada):
    conectivos = ['∧', '∨', '→', '↔'];

    for simbolo in conectivos:
        if entrada == simbolo:
            return True;

    return False;

def eh_letra_valida (entrada):
    valor_ascii = ord(entrada);
    return valor_ascii >= 65 and valor_ascii <= 90;

class No:
    valor: any;
    esquerda: any;
    direita: any;
    depth: int;

    def __init__(self, valor, esquerda = None, direita = None):
        self.valor = valor;
        self.esquerda = esquerda;
        self.direita = direita; 
        self.depth = None;

    def __str__(self):
        return self.valor;

class ArvoreBinaria():
    raiz: No;
    marcadores: Pilha;
    folhas: list;
    altura: int;

    def __init__(self, no):
        self.raiz = no;
        self.raiz.depth = 0;
        self.marcadores = Pilha();
        self.marcadores.push(no);
        self.folhas = [no];
        self.altura = 0;

    #Adição feita em Pré-Ordem
    def adicionar(self, novo_no):  
        if len(novo_no.valor) == 2:
            simbol = novo_no.valor[1];
        else:
            simbol = novo_no.valor;

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
        
        if (eh_conectivo(simbol)):
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

def inverter(entrada):
    resultado = '';
    for i in range(len(entrada)):
        resultado += entrada[len(entrada) - 1 - i];
    return resultado;

def quebra_expressao(entrada):
    N = len(entrada);
    simbolos = [];
    for c in range(N):

        if (eh_conectivo(entrada[c])):
            if c > 0 and entrada[c-1] == '¬':
                simbolos.append('¬' + entrada[c]);
            else:
                simbolos.append(entrada[c]);

        if (eh_letra_valida(entrada[c])):
            if c + 2 < N and entrada[c+1] == '¬' and not eh_conectivo(entrada[c+2]):
                simbolos.append('¬' + entrada[c]);
            else:
                simbolos.append(entrada[c]);

    return simbolos;

def pow(valor, expoente):
    multiplicador = valor;
    valor = 1;
    for i in range(expoente):
        valor *= multiplicador;
    return valor;

def valor_logico(level, round, size):
    fator = pow(2,size-level);
    fator = round // fator;
    return is_even(fator);

def is_even(numero):
    return numero%2 == 0;

expressao_posfix = "PQ→¬A↔¬¬B¬C∨∧";

# ∧∨C¬B¬¬↔A¬→QP
# conectivo sem um "não" antes => adiciona conectivo
# letra seguida de um não e outro que não é conectivo => adiciona Não letra
# letra seguida de um não e outro 
#AAAAAAAAAAAAAAA
 
entrada = inverter(expressao_posfix);
expressoes = quebra_expressao(entrada);
arvore_principal = None;

for c in range(len(expressoes)):
    novo_no = No(expressoes[c]);

    if c == 0:
        arvore_principal = ArvoreBinaria(novo_no);
    else:
        arvore_principal.adicionar(novo_no);

for each in arvore_principal.exibir_ordem_profundidade():
    print(str(each.depth) + " : " + str(each));

print("Altura da Arvore : " + str(arvore_principal.altura));
arvore_principal.exibir_conexões();

#Será que deu certo?
#Crie uma função para apresentar a arvore, nivel a nivel

print("TESTANDO O GERADOR DE V E F: ");

for b in range(4):
    linha = [];
    for j in range(16):
        linha.append(valor_logico(b+1, j, 4))
    print(linha);






