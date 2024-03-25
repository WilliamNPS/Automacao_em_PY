# passo a passo do projeto 
# Passo 1 : Entrar no sistema da empresa 
# biblioteca pra fazer automoção   -> pip install pyautogui
import pyautogui

# biblioteca time  
import time 

# Pausa a cada comando 
pyautogui.PAUSE  = 1

# pyautogui.click -> clicar em algum lugar da tela 
# pyautogui.write -> escrever um  texto 
# pyautogui.press -> pressionar uma tecla do teclado 
# pyautogui.hotkey("ctrl", "v") -> Duas teclas ao mesmo tempo 

# Abrir o navegador 
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3 segundos)
time.sleep(3)
#---------------------------------------------------------------------#

# Passo 2 :  Fazer Login 

pyautogui.click(x=411, y=352)

pyautogui.write("williamDev@suporte.com")
pyautogui.press("tab")
pyautogui.write("williamsuporte")


#clicar no botão de logar 
pyautogui.click(x=701, y=522)
time.sleep(3)

# Passo 3 : Importar a base de dados 
# baixa a biblioca pandas para importação de dados -> pip install pandas numpy openpyxl

import pandas 

tabela =  pandas.read_csv("produtos.csv")


# Passo 4 : Cadastrar o produto

# fazer um loop para cada linha da tabela

for linha in tabela.index:

  #clicar no primeiro campo
  pyautogui.click(x=629, y=238)

  #codigo do produto 
  codigo = tabela.loc[ linha, "codigo"]
  pyautogui.write(codigo)
  pyautogui.press("tab")

  #codigo da marca
 
  marca = tabela.loc[linha,"marca"]
  pyautogui.write(marca)  
  pyautogui.press("tab")

  #codigo do tipo 
 # outra forma pratica de chama os dados
  pyautogui.write(tabela.loc[linha,"tipo"])
  pyautogui.press("tab")

  #codigo da categoria
  pyautogui.write(str(tabela.loc[linha,"categoria"]))
  pyautogui.press("tab")

  #codigo da preço
  pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
  pyautogui.press("tab")

  #codigo da custo
  pyautogui.write(str(tabela.loc[linha,"custo"]))
  pyautogui.press("tab")

  #codigo da observação
  obs = tabela.loc[linha, "obs"]
  if not pandas.isna(obs):
     pyautogui.write(str(obs))  

 
  pyautogui.press("tab")

 
  #cadastrar produto
  pyautogui.press("enter")
  pyautogui.scroll(+5000) 




