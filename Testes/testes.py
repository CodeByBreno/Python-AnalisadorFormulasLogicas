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
    
    return [resultado,index_repeticao];

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

lista = [1,1,2,1,3,4,3,2,5,1,2,3,5];

print(remove_repetidos(lista)[0]);
print(remove_repetidos(lista)[1]);

print(limpa_lista(lista, remove_repetidos(lista)[1]))

