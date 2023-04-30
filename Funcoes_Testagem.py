
#São funções usadas para testar o projeto

from Analisador import automato, determina_proximo;
from Avaliador import posfixar, gerar_arvore, obter_expressoes;

#Testa o automato responsável por determinar se a expressão é válida ou não
def testa_automato():
    #Código para testar o Automato
    for each in automato.keys():
        teste_values = ['A', 'a', '(', ')', '∧', '∨', '¬', '→', '↔'];

        print("----------------------------");
        print("Movimentos do Nó " + each + " :  ");
        for valor_teste in teste_values:
            proximo_no = determina_proximo(each, valor_teste);
            if proximo_no != -1:
                print(valor_teste + ' -----> ', proximo_no);
        print("----------------------------");
        print("   ");

#Gera uma série de dados sobre o processo de construção da tabela verdade
def debugger_analise(expressao):
    
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
    print(arvore_expressao.subformulas);

    print("TODAS AS PROPOSICOES: ");
    print(arvore_expressao.obter_letras());

    print("INTERPRETAÇÕES: ");
    for each in arvore_expressao.avaliar():
        print(each);
