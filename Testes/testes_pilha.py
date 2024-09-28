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
        print(self.tamanho);

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

teste = Pilha();

for i in range(5):
    teste.push(i);

for i in range(teste.tamanho):
    print("VALOR RETIRADO: " + str(teste.pop()));
    print("TOPO: " + str(teste.topo));