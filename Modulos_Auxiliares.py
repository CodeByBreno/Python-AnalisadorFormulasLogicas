#Essas funções foram usadas para modular os processos de analise da cadeia lógica e o de geração
#da tabela verdade. Elas realizam operações essenciais para o funcionamento dos respectivos códigos

from Funcoes_Basicas import eh_conectivo, eh_letra_valida, is_even;

#Essa função remote todos os espaços da cadeia de entrada (inserida pelo usuário)
def eliminar_espacos(entrada):
    lista = entrada.split(" ");
    return ("").join(lista);

#Essa função remove "não's" redundantes. Uma quantidade par de ¬ em sequência é substituida por nenhum,
#uma quantidade ímpar é substituida por apenas um '¬'
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

#Após posfixar a cadeia de entrada, é necessário identificar todos os simbolos nela presente, com relação
#aos simbolos que são utilizados na lógica proposicional (operadores, proposicoes, etc). É uma Análise
#Léxica. O resultado é uma lista com todos os simbolos separados
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

#Essa função é usada para construir a tabela verdade. Ela atribui para cada proposição um valor verdadeiro
#ou falso, com base num padrão matemático:
#A primeira proposicao encontrada receberá os valores na ordem VVVVVV....VVFFFFF...FFFFFF (alterna apenas uma vez)
#A segunda, VVVVV...VVFFF...FFFFVVVV...VVVFFFF...FFFFF (alterna duas vezes)
#A terceira, VVVV...VVFF..FFVV..FFVV..FFVV..FFFFFF (alterna quator vezes)
#etc. Esse padrão é definido pela ordem em que cada nó é encontrando (o primeiro a ser encontrado vai receber os
# valores segundo o primeiro padrão, o segundo, segundo, o terceiro, terceiro, etc)
def valor_logico(level, round, size):
    fator = pow(2, size-level);
    fator = round // fator;
    return is_even(fator);

#Essencial para construção da tabela verdade, esse código calcula o valor lógico resultante da aplicação
#da operação informada aos valores lógicos P e Q
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

#Da maneira como eu fiz, caso você tenha o mesmo "P" duas vezes em uma fórmula, ele irá aparecer duas vezes 
#na lista de expressões. Isso é incoveniente e gera uma poluição visual desnecessária. O código abaixo remove
#essas repetições redundantes
def remove_repetidos(lista):
    resultado = [];
    index_repeticao = [];
    for c in range(len(lista)):
        flag = True;
        if c == 0:
            resultado.append(lista[c]);
        else:
            for every in resultado:
                if lista[c] == every:
                    flag = False;
                    index_repeticao.append(c);
            if flag:
                resultado.append(lista[c]);
    
    return [resultado, index_repeticao];

#Se eu removo algumas das expressões (as que são repetições), preciso também remover os valores à elas associados
#nas linhas da tabela. Por exemplo, se eu tenho 3 expressões: P P e P^P, ao remover um dos P, precisarei remover
#a segunda coluna de todas as linhas de resultado - que teriam algo como V V V, e agora vão ter V V
def limpa_lista(lista, indices):
    resultado = [];
    for c in range(len(lista)):
        adicionar = True;
        for a in indices:
            if c == a:
                adicionar = False;
        if adicionar:
            resultado.append(lista[c]);
    return resultado;
