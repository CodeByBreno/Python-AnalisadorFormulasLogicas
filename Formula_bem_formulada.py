# Formula_bem_formulada
# Atividade para Disciplina de Lógica Para Computação - 2022.2
# Feito por: Breno Gabriel de Souza Coelho | Turma 2019.2

#Simbolos Conectivos = ["∧", "∨", "¬", "→", "↔", "(", ")"]

from tkinter import *;
from tkinter import ttk;

paleta_cor = "Modo Escuro";
valido = False;

from Funcoes_Basicas import textualizar;
from Modulos_Auxiliares import eliminar_espacos, remove_repetidos, limpa_lista;
from Funcoes_Testagem import debugger_analise;
from Avaliador import *;
from Analisador import analisa_formula;

#Construtores de Elementos visuais
def botao_conectivo(caractere):

    return Button(conections, 
                  text = caractere, 
                  command=lambda: mudar_texto_input(caractere, False), 
                  bg="#fec51a", 
                  height=conection_button_height, 
                  width=conection_button_width, 
                  fg="#000000",
                  relief="flat",
                  font=font_conectivos);

def botao_teclado(caractere):

    return Button(teclado_principal, 
                  text=caractere, 
                  command=lambda: mudar_texto_input(caractere, False), 
                  bg="#ffe75f", 
                  height=teclado_button_height, 
                  width=teclado_button_width, 
                  fg="#000000",
                  relief="flat",
                  font=font_teclado)

def mudar_cor(elementos_da_tela):
    global paleta_cor;
    print(paleta_cor);
    if paleta_cor == "Modo Escuro":

        color_switcher["text"] = "Modo   Claro";
        paleta_cor = "Modo Claro";

        background_color = "#dddddd";  

        texto_input_background = "#222222";
        texto_input_color = "#dddddd";

        letter_button_color = "#66c0d6"; #30bec0
        letter_text_color = "#222222";
        conection_button_color = "#0197bc";
        conection_text_color = "#222222";

        botao_remove_color = "#0197bc";
        botao_clear_color = "#0197bc";
        botao_espaco_color = "#0197bc";

        cabecalho_fonte_cor = "#222222";

        analisar_cor = "#30bec0";
        tabela_verdade_cor = "#30bec0";
        texto_resposta_background = "#222222";
        texto_resposta_color = "#dddddd";
    
    else:

        color_switcher["text"] = "Modo Escuro";
        paleta_cor = "Modo Escuro";
    
        texto_input_background = "#dddddd";
        texto_input_color = "#222222";
        background_color = "#222222";   

        letter_button_color = "#ffe75f";
        letter_text_color = "#000000";

        conection_button_color = "#fec51a";
        conection_text_color = "#000000";

        botao_remove_color = "#fec51a";
        botao_clear_color = "#fec51a";
        botao_espaco_color = "#fec51a";

        cabecalho_fonte_cor = "#ffffff";

        analisar_cor = "#ffd700";
        tabela_verdade_cor = "#ffd700";
        texto_resposta_background = "#dddddd";
        texto_resposta_color = "#222222";
    
    elementos_da_tela["janela"].config(bg=background_color)
    elementos_da_tela["cabecalho"].config(bg=background_color)
    elementos_da_tela["titulo_text"].config(bg=background_color, fg=cabecalho_fonte_cor)
    elementos_da_tela["cabecalho_body"].config(bg=background_color, fg=cabecalho_fonte_cor)

    elementos_da_tela["texto_input"].config(bg=texto_input_background, fg=texto_input_color)
    elementos_da_tela["conections"].config(bg=background_color)

    for each in elementos_da_tela["tecla"]:
        each.config(bg=conection_button_color, fg=conection_text_color);

    elementos_da_tela["teclado"].config(bg=background_color)
    elementos_da_tela["teclado_principal"].config(bg=background_color)

    for each in elementos_da_tela["botao"]:
        each.config(bg=letter_button_color, fg=letter_text_color);

    elementos_da_tela["controle"].config(bg=background_color)
    elementos_da_tela["botao_remove"].config(bg=botao_remove_color)
    elementos_da_tela["botao_clear"].config(bg=botao_clear_color)
    elementos_da_tela["botao_espaco"].config(bg=botao_espaco_color)
    elementos_da_tela["manipuladores_da_entrada"].config(bg=background_color);
    elementos_da_tela["botao_analisar"].config(bg=analisar_cor)
    elementos_da_tela["botao_gerar_tabela_verdade"].config(bg=tabela_verdade_cor);
    elementos_da_tela["texto_resposta"].config(bg=texto_resposta_background, fg=texto_resposta_color);

def interface_visual_tab_verdade(arvore_expressao, interpretacoes, exb_subf = True):
    #Interface Visual da Tabela Verdade

    janela_tabela_verdade = Tk();
    janela_tabela_verdade.title("Tabela Verdade");
    janela_tabela_verdade.config(bg="silver");
    janela_tabela_verdade.geometry("1000x500");
    
    scrollbar_x = Scrollbar(janela_tabela_verdade, orient='horizontal');
    scrollbar_x.pack(side=BOTTOM, fill='x');
    scrollbar_y =  Scrollbar(janela_tabela_verdade, orient='vertical');
    scrollbar_y.pack(side=RIGHT, fill='y');

    obter_expressoes(arvore_expressao, arvore_expressao.raiz);

    retorno_remove_repetidos = remove_repetidos(arvore_expressao.subformulas);
    todas_expressoes = tuple(retorno_remove_repetidos[0]);
    indices_eliminaveis = retorno_remove_repetidos[1];
    qtd_proposicoes = len(arvore_expressao.obter_letras());

    for c in range(len(interpretacoes)):
        interpretacoes[c] = limpa_lista(interpretacoes[c], indices_eliminaveis);

    prop_tab = propriedade_tabela(interpretacoes);
    N = len(prop_tab);
    prop_tab = prop_tab[0:N-1]; #tirando um '\n' ai

    cabecalho_1 = Frame(janela_tabela_verdade);
    cabecalho_1.pack(side=TOP, pady=(20,0));
    cabecalho_1.configure(background="green");

    texto_tipo = Label(cabecalho_1,
                       text=prop_tab,
                       width=50,
                       font="Rubik 15",
                       background="green",
                       fg="white");
    texto_tipo.pack(side=TOP, padx=(10,0));
    
    style = ttk.Style(janela_tabela_verdade);

    style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=40,
                    fieldbackground="silver");
    style.configure("Treeview.Heading",
                    background="silver",
                    foreground="black",
                    rowheight=40,
                    fieldbackground="silver");
    style.map("Treeview", background=[('selected', 'green')]);

    tabela_verdade = ttk.Treeview(janela_tabela_verdade, 
                                  selectmode="browse", 
                                  column=todas_expressoes, 
                                  show="headings",
                                  height=2**qtd_proposicoes,
                                  style=("Treeview"),
                                  xscrollcommand = scrollbar_x.set,
                                  yscrollcommand = scrollbar_y.set,
                                  );
    tabela_verdade.pack(side=TOP, anchor='center', pady=(50,0));
    scrollbar_x.config( command = tabela_verdade.xview);
    scrollbar_y.config( command = tabela_verdade.yview)

    tabela_verdade.tag_configure('odd', background='#E8E8E8');
    tabela_verdade.tag_configure('even', background='#DFDFDF');
    tabela_verdade.tag_configure('general_text', font=('Rubik', '15'));

    tam_tabela = 0;
    for i in range(len(todas_expressoes)):
        aux = tamanho_coluna_tab_verdade(len(todas_expressoes[i]));
        print("Tamanho de " + str(todas_expressoes[i]) + " : " + str(aux));
        tam_tabela += aux;
        tabela_verdade.column(todas_expressoes[i], 
                              width=aux, 
                              stretch=NO,
                              anchor= "center",);
        tabela_verdade.heading("#" + str(i+1), text=todas_expressoes[i]);
    
    for c in range(len(interpretacoes)):
        if c%2 == 0:
            tabela_verdade.insert("", END, values=interpretacoes[c], tags=('odd', 'general_text'));
        else:
            tabela_verdade.insert("", END, values=interpretacoes[c], tags=('even', 'general_text'));
    
    centralize_with_x = (1000 - tam_tabela)//2;
    if centralize_with_x < 0: 
        centralize_with_x = 0;

    janela_tabela_verdade.mainloop();

def tamanho_coluna_tab_verdade(tam_entrada):
    if tam_entrada < 5:
        #Pequeno
        return 40;
    if tam_entrada < 10:
        #Medio
        return 90;
    if tam_entrada < 15:
        #Grande
        return 150;
    if tam_entrada < 20:
        return 200;
    return 300;

def mudar_texto_input(entrada, control):

    texto_resposta["text"]= "";
    botao_gerar_tabela_verdade["state"] = "disable";

    if control:
        if entrada == ' ':
            texto_input["text"] = texto_input["text"] + entrada;
        else:
            texto_input["text"] = entrada;
    else:
        texto_input["text"] = texto_input["text"] + entrada;

#Uma ideia interessante, mas desnecessária (dimensionar as colunas da tab_verdade usando uma função não linear)
def dimensiona_tab_verdade(valor):
    return int(-((150)/(valor+8))+20);

#Funções que tiveram que ficar aqui para não criar uma chamada ciclica

def gerar_resposta(entrada, botao_gerar_tabela_verdade):
    resultado_parcial = analisa_formula(eliminar_espacos(entrada));

    if resultado_parcial[0:4] != "ERRO":
        botao_gerar_tabela_verdade["state"] = 'normal';
    
    resultado = resultado_parcial.split("#");
    texto_resposta['text'] = resultado[0];
    print("----------------------------------------------------");
    print("TEXTO INSERIDO: " + entrada);

    if len(resultado) == 2: 
        print(resultado[0] + "  " + resultado[1]);
        return resultado[1];
    else:
        return -1;

def gerar_tabela_verdade(entrada):

    debugger_analise(entrada);

    expressao_posfix = posfixar(entrada);
    arvore_expressao = gerar_arvore(expressao_posfix);
    interpretacoes_logic = arvore_expressao.avaliar();
    interpretacoes = textualizar(interpretacoes_logic);
    
    qtd_subformulas = len(arvore_expressao.subformulas);

    interface_visual_tab_verdade(arvore_expressao, interpretacoes)

#Main Function

#Construindo a Janela principal ------------------------------------------------------------------------------------------------
janela = Tk()
janela.title("Testador de Fórmulas Lógicas");
janela.geometry("1080x700");
#bg = PhotoImage(file = r"H:\Breno Gabriel\Desktop\Projetos Pessoais\Aulas - 8º Periodo\Analisar_formula_logica\imagens\background.jpg");

cabecalho = Frame(janela);
cabecalho.grid(column=0, row=0, pady = (4, 16), padx=(0, 4));

#Personalizações e cores -------------------------------------------------------------------------------------------------------
janela.config(background="#222222");
cabecalho.config(bg="#222222");

font_teclado = "Rubik 13";
font_conectivos = "Rubik 15";
fonte_analisar = "Rubik 15";
fonte_texto_resposta = "Rubik 15";

conection_button_height = 1;
conection_button_width = 7;

teclado_button_height = 2;
teclado_button_width = 5;

space_between_buttons = 5;

#Título e Texto Inicial ------------------------------------------------------------------------------------------------------
titulo = "Análise da Estrutura de uma Fórmula Lógica";
texto_cabecalho = "Clique nas teclas abaixo para inserir a fórmula, e em \"Analisar\" para\n" + "verificar se está adequadamente formulada";

titulo_text = Label (cabecalho, text=titulo, font="Rubik 20", bg = "#222222", fg="#ffffff");
titulo_text.grid (column = 0, row = 0);
cabecalho_body = Label (cabecalho, text=texto_cabecalho, font="Rubik 15", bg = "#222222", fg="#ffffff");
cabecalho_body.grid (column = 0, row = 1);

#input_formula = Entry(janela, width=100);
#input_formula.grid(column = 0, row = 1, padx=(40,20));

#Zona com o Input - Fórmula a ser inserida ------------------------------------------------------------------------------------
texto_input = Label (janela, text="", width=70, font="Rubik 18", height=2);
texto_input.grid(column = 0, row = 1, pady=(8,12), padx=(50,0))

#Teclado   --------------------------------------------------------------------------------------------------------------------

conections = Frame(janela, bg="#222222");
conections.grid(column=0, row=2, pady=(20,0))

teclado = Frame(janela, bg="#222222");
teclado.grid(column=0, row=3, pady=20);

teclado_principal = Frame(teclado, bg="#222222");
teclado_principal.grid(column=0, row=0, padx=(0,20));
controle = Frame(teclado, bg="#222222");
controle.grid(column=1, row=0);

botao_remove = Button(controle, 
                      text="REMOVE", 
                      command=lambda: mudar_texto_input(texto_input["text"][:len(texto_input["text"]) - 1], True), 
                      bg="#FFD700", 
                      height=3, 
                      width=10,
                      font=font_teclado,
                      relief="flat");
botao_remove.grid(column=0, row=0, pady=(0,20));

botao_clear = Button(controle, 
                      text="CLEAR",
                      command=lambda: mudar_texto_input("", True), 
                      bg="#ffd700", 
                      height=2, 
                      width=10,
                      font=font_teclado,
                      relief="flat");
botao_clear.grid(column=0, row=1, pady=(0,20));

botao_espaco = Button(controle, 
                      text="ESPACO",
                      command=lambda: mudar_texto_input(" ", True), 
                      bg="#ffd700", 
                      height=2, 
                      width=10,
                      font=font_teclado,
                      relief="flat");
botao_espaco.grid(column=0, row=2, pady=(0,20));

#Botões dos Conectivo:
simbolos_conectivos = ["∧", "∨", "¬", "→", "↔", "(", ")"]

tecla = [];
for i in range(len(simbolos_conectivos)):
    tecla.append(botao_conectivo(simbolos_conectivos[i]));
    tecla[i].grid(column=i%7, row=0, padx=space_between_buttons)

#Letras do teclado
letras_QWERTY = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

botao = [];
for i in range(len(letras_QWERTY)):
    botao.append(botao_teclado(letras_QWERTY[i]))
    botao[i].grid(column=i%7, row=i//7+1, padx=space_between_buttons, pady=(0,10))

manipuladores_da_entrada = Frame(janela, bg="#222222");
manipuladores_da_entrada.grid(column=0, row=4, pady=(0,10));

botao_gerar_tabela_verdade = Button(manipuladores_da_entrada,
                                    text="Gerar Tabela Verdade",
                                    command=lambda: gerar_tabela_verdade(texto_input["text"]),
                                    bg="#ffd700",
                                    fg="#000000",
                                    font=fonte_analisar,
                                    width=20,
                                    relief="flat");
botao_gerar_tabela_verdade.grid(column=1, row=0);
botao_gerar_tabela_verdade["state"] = "disable";

botao_analisar = Button(manipuladores_da_entrada, 
               text="Analisar", 
               command=lambda: gerar_resposta(texto_input["text"], botao_gerar_tabela_verdade),
               bg="#ffd700",
               fg="#000000",
               font=fonte_analisar,
               width=20,
               relief="flat");
botao_analisar.grid(column=0, row=0, padx=(0,10));

texto_resposta = Label (janela, 
                        text="", 
                        width=80,
                        height=2,
                        font = fonte_texto_resposta);
texto_resposta.grid(column=0, row=5, pady=10);

elementos_da_tela = {
    "janela": janela, 
    "cabecalho": cabecalho, 
    "titulo_text": titulo_text, 
    "cabecalho_body": cabecalho_body, 
    "texto_input": texto_input,
    "conections": conections,
    "tecla": tecla,
    "teclado": teclado,
    "teclado_principal": teclado_principal,
    "botao": botao, 
    "controle": controle, 
    "botao_remove": botao_remove, 
    "botao_clear": botao_clear, 
    "botao_espaco": botao_espaco,
    "manipuladores_da_entrada": manipuladores_da_entrada,
    "botao_analisar": botao_analisar,
    "botao_gerar_tabela_verdade": botao_gerar_tabela_verdade,
    "texto_resposta": texto_resposta,
}

#Alternador de Modo -----------------------------------------------------------------------------------------------------------
color_switcher = Button (cabecalho, 
                         text="Modo Escuro", 
                         command=lambda: mudar_cor(elementos_da_tela),
                         relief="flat");
color_switcher.grid (column=1, row=1, padx=(30,0));

janela.mainloop();

