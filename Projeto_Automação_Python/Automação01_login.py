import pyautogui
from time import sleep

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
sleep(1)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

sleep(3)

pyautogui.press("tab")
#pyautogui.click(x=581, y=750) // parametro clicks = qtdade de cliques q quer dar
pyautogui.write("fmc_nit@globo.com")
pyautogui.press("tab")
pyautogui.write("Senha")
pyautogui.press("enter")

sleep(2)

import pandas

tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    obs = str(tabela.loc[linha, "obs"])

    pyautogui.press("tab")
    pyautogui.write(str(codigo))
    sleep(0.2)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    sleep(0.2)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    sleep(0.2)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    sleep(0.2)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    sleep(0.2)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    sleep(0.2)
    pyautogui.press("tab")
    if obs == "nan":
        pyautogui.write("")
    else:
        pyautogui.write(obs)
    sleep(0.2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    for c in range(0,11):
        pyautogui.press("tab")

