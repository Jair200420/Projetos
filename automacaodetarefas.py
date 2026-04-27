# Aula 1 - Automação de Tarefas

# Lógica do programa - Passo a passo da realização do projeto:
# 1: Entrar no sistema da impresa: (https://dlp.hashtagtreinamentos.com/python/intensivao/login);
# 2: Fazer login no sistema;
# 3: Importar a abse de dados;
# 4: Cadastrar produtos.

import time
import pyautogui

# Comandos principais da biblioteca pyautogui:
# Clicar >>> pyautogui.click;
# Escrever >>> pyautogui.write;
# Apertar uma tecla >>> pyautogui.press;
# Atalho >>> pyautogui.hotkey;
# Scroll do mouse >>> pyautogui.scroll

# Início do código:

pyautogui.PAUSE = 1 # Tempo de espera entre cada comando da biblioteca do pyautogui
pyautogui.press("win") # Apertar o atalho do windows
pyautogui.write("opera")
pyautogui.press("enter") # Abrir o navegaor Opera

# É possível criar variáveis para facilitar a "chamada" de um valor ou palavra
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Pode-se utilizar a variável "link" ao invés de ter que escrever todo o link, neste caso
# Ex: pyautogui.write(link)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # tempo de segurança para esperar o site abrir

pyautogui.click(x=784, y=389) # Vamos selecionar a barra para inserir o e-mail
pyautogui.write("jgdan@mail.com") # Vamos digitar o nosso endereço de e-mail
pyautogui.press("tab") # Pressionar a tecla "tab" para mudar para o campo de senha
pyautogui.write("jgdan") # Vamos digitar nossa senha
pyautogui.press("tab") # Mudar para o botão de logar
pyautogui.press("enter") # Apertar o botão de logar
time.sleep(3) # Tempo de segurança para o site abrir

# Importação da base de dados:

import pandas

tabela = pandas.read_csv("produtos.csv") # Comando para ler a tabela com a base de dados
print(tabela)

for linha in tabela.index: # Função "for" para pegar todos os itens da nossa base de dados, linha por linha
    pyautogui.click(x=737, y=269)
    # Código do produto
    pyautogui.write(tabela.loc[linha, "codigo"]) # Utiliza-se o comando "tabela.loc" para declarar a linha e nome da coluna para pegar os dados
    pyautogui.press("tab") # Observação: Basta apenas declarar linha no tabela.loc, pois a função "for" muda automaticamente o número de linhas 
    #  Marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # Tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # Faz-se necessário a utilização da função string (str) para transformar os números em uma "palavra"
    pyautogui.press("tab")
    # Preço do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # Custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # Observações
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # Utilizou-se a função condicional "if" para verificar se o espaço é vazio (nan) ou não
        pyautogui.write(tabela.loc[linha, "obs"]) # Se tiver algo para preencher, o código escreverá e no caso contrário, deixará em branco
    # A coluna obs na base de dados apresenta espaços vazios "nan". Logo faz-se necessário tratar com uma condição 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(2000) # Comando para utilizar o scroll do mouse, números negativos rola o scroll par baixo e positivos para cima

# Fim do código