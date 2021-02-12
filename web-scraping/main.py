import pandas as pd
from selenium import webdriver

table = pd.read_excel("web-scraping/database/Clientes Pagamento.xlsx", dtype={"Cliente": object})
table = table[["Nome", "Valor Pago", "Valor Total Devido", "Email"]]

devedores = table["Valor Total Devido"] - table["Valor Pago"]

valores = []
for x in devedores:
    valores.append(x)

table["Deve"] = valores
table = table[["Nome", "Deve", "Email"]]
table = table.loc[table["Deve"] != 0]
linhas = len(table)
table = table["Nome"]

nomes = []
for name in table:
    nome = name + ","
    nomes.append(nome)

# .loc[Linha, Coluna]

navegador = webdriver.Chrome()
navegador.get("http://www.sorteandoja.com.br/")
navegador.find_element_by_id("fechar-modal-automatico").click()
navegador.find_element_by_id("sj_quantidade3").clear()
navegador.find_element_by_id("sj_quantidade3").send_keys(linhas)
navegador.find_element_by_id("sj_itens").send_keys(nomes)
navegador.find_element_by_id("sj-bt-sortear3").click()


