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

print(redutor_not("(((R→¬¬¬B)↔¬¬¬¬((¬R∨T)↔A))∨¬T)"));
print(redutor_not("A→¬¬¬¬¬R"));
print(redutor_not("A→¬¬¬¬R"));
print(redutor_not("¬¬¬¬R"));
print(redutor_not("¬¬¬¬¬R"));
print(redutor_not("(R→¬¬(((Q∨¬¬W)↔¬(¬R∨¬Q))∨¬(T→¬R)))"));

print(redutor_not("¬¬¬(R∨T)"));       #vagabundo

#(((R→¬¬¬B)↔¬¬¬¬((¬R∨T)↔A))∨¬T)
#A→¬¬¬¬¬R
#(R→¬¬(((Q∨¬¬W)↔¬(¬R∨¬Q))∨¬(T→¬R)))
#"¬(R∨T)"
