import pandas as pd

table = pd.read_excel("web-scraping/database/Clientes Pagamento.xlsx")
table = table[["Nome", "Valor Pago", "Valor Total Devido", "Email"]]

devedores = table["Valor Total Devido"] - table["Valor Pago"]

valores = []
for x in devedores:
    valores.append(x)

table["Deve"] = valores
table = table[["Nome", "Deve", "Email"]]
table = table.loc[table["Deve"] != 0]

