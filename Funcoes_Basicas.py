#Essas funções fazem coisas bem triviais, que foram necessárias conforme fui construindo o código,
#Como calcular potenciação(sim, eu sei que poderia ter usado **, mas não lembrei na hora KKKKKKKKKK)
#Trocar True (booleano) por V e False (booleano) por F, verificar se um número é par, se um elemento
#está contido numa lista, etc. Os nomes delas são bem autoexplicativos

def pow(valor, expoente):
    multiplicador = valor;
    valor = 1;
    for i in range(expoente):
        valor *= multiplicador;
    return valor;

def textualizar(interpretacoes_logic):
    for each in interpretacoes_logic:
        for c in range(len(each)):
            if each[c]: 
                each[c] = 'V';
            else:
                each[c] = 'F';
    return interpretacoes_logic;

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

def inverter(entrada_lista):
    entrada = "".join(entrada_lista);
    resultado = '';
    for i in range(len(entrada)):
        resultado += entrada[len(entrada) - 1 - i];
    return resultado;

