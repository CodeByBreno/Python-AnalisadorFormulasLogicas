#Conectivos = '∧', '∨', '¬', '→', '↔'
#¬(¬( ¬¬P ∧ Q ) → C )
    
# Analisador

from Funcoes_Basicas import eh_conectivo, eh_letra_valida;

automato = {
    "q0": {"final": False,
           "chaves": 
            { "¬": "q0",
              "(": "q0" ,
              "letra": "q1"}},

    "q1": {"final": True,
           "chaves": 
            {"conectivo": "q2",
             ")": "q6"}},

    "q2": {"final": False,
           "chaves": 
            {"¬": "q2",
             "letra": "q4",
             "(": "q3"}},
            
    "q3": {"final": False,
           "chaves": 
            {"¬": "q3",
             "letra": "q1",
             "(": "q3"}},

    "q4": {"final": True,
           "chaves": 
            {")": "q5"}},
        
    "q5": {"final": True,
           "chaves": 
            {"conectivo": "q2",
             ")": "q5"}},

    "q6": {"final": True,
           "chaves": 
            {"conectivo": "q2"}}
    
}

def determina_proximo(estado, caractere):

    #Caso seja um espaço vindo da entrada, retorna o próprio estado
    if caractere == ' ':
        return estado;
    
    #Se não for um espaço vazio, analiso a transição de estado que deve ser gerada
    for each in automato[estado]["chaves"].keys():     

        #Caso seja um simbolo simples, como '(' ou ')' ou '¬'
        if caractere == each:
            return automato[estado]["chaves"][each];      
          
        #Caso seja uma letra que representa uma proposição
        if each == "letra" and eh_letra_valida(caractere):
            return automato[estado]["chaves"][each];   

        #Caso seja um conectivo - operação lógica - 
        if each == "conectivo" and eh_conectivo(caractere):
            return automato[estado]["chaves"][each];

    return -1;

def analisa_formula (entrada):

    global valido

    estado_atual = "q0";
    cont_abre_par = 0;
    cont_fecha_par = 0;
    count_conectivos = 0;


    for i in range(len(entrada)):
        print(estado_atual, entrada[i]);
        proximo_estado = determina_proximo(estado_atual, entrada[i]);

        if entrada[i] == '(':
            cont_abre_par += 1;
        if entrada[i] == ')':
            cont_fecha_par += 1;
        if eh_conectivo(entrada[i]):
            count_conectivos += 1;

        if proximo_estado == -1:
            return "ERRO: Problema no " + str(i + 1) + "º dígito\n" + "#" + str(i);
    
        estado_atual = proximo_estado;
    
    if cont_fecha_par == cont_abre_par:
        if cont_fecha_par == count_conectivos or cont_fecha_par == count_conectivos - 1:
            if automato[estado_atual]["final"]:
                valido = True;
                return "A fórmula está construida corretamente";
            else:
                return "ERRO: A fórmula possui algum problema";
        else:
            return "ERRO: Todos os conectivos precisam de abertura e fechamento de parênteses";
    else:
        return "ERRO: Parece que faltam alguns parênteses";

