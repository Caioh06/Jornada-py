#pip install pyautogui -> instalar o pyautogui
#pip install pandas openpyxl -> instalar o pandas e o openpyxl

import pyautogui
import time

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# ---- Passo a passo do programa ------

# -----Passo 1: Entrar no sistema da empresa
    #abrir navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3)

# -----Passo 2: Fazer login
    #clicar no campo email
pyautogui.click(x=732, y=363)
pyautogui.write("seuemail@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha1234")
pyautogui.press("tab")
pyautogui.press("enter")

# fazer uma pausa maior pro site carregar
time.sleep(3)

# -----Passo 3: Abrir base de dados
import pandas
tabela = pandas.read_csv("Python Powerup\produtos.csv")
print(tabela)

for linha in tabela.index:
    # -----Passo 4: Cadastrar os produtos
    pyautogui.click(x=735, y=253) #clicar no primeiro campo do codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") #passar para o proximo campo

    #-----campo da marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
   
    #-----campo do tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    #-----campo da categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    #-----campo do preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    #-----campo do custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    #-----campo da observação
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nam":
        pyautogui.write(obs)
    pyautogui.press("tab") #passar para o botao enviar

    pyautogui.press("enter") #clicar no enviar
    pyautogui.scroll(5000) #voltar para o inicio do site
