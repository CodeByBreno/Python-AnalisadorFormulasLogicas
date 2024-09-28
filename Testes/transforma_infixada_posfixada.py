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
    
    print("Entrada original : " + str(entrada));
    ent_util = redutor_not(eliminar_espacos(entrada));
    print("Entrada Util: " + str(ent_util));

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

#O problema do Não
#print("".join(posfixar("¬(R∨T)"))); #o que fazer?
#print("".join(posfixar("¬¬(P∨Q)")));
#print("".join(posfixar("¬(A→¬(B∨Q))")));
print("".join(posfixar("(((R→¬¬¬B)↔¬¬¬¬¬((¬R∨T)↔A))∨¬T)")));
#print("".join(posfixar("¬(¬(P→Q)↔A)∧(¬B∨¬C))")));

# ¬¬(P∨Q)
# ¬(A→¬(B∨Q))
# ¬(¬(P→Q)↔A)∧(¬B∨¬C)
#print("".join(posfixar("(((R→¬¬¬B)↔¬¬¬¬((¬R∨T)↔A))∨¬T)")));

