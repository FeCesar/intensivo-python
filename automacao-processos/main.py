import pandas as pd

databaseName = "./automacao-processos/database/vendas.xlsx"
sellTable = pd.read_excel(databaseName)

revenuesColumns = sellTable[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
revenuesColumns = revenuesColumns.sort_values(by="Valor Final", ascending=False)

amountColumns = sellTable[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
amountColumns = amountColumns.sort_values(by="Quantidade", ascending=False)

ticketMiddleColumns = revenuesColumns["Valor Final"] / amountColumns["Quantidade"]
ticketMiddleColumns = ticketMiddleColumns.to_frame()
ticketMiddleColumns = ticketMiddleColumns.rename(columns={0: "Ticket Médio"})

fullTable = revenuesColumns.join(amountColumns).join(ticketMiddleColumns)

def sendEmail(shoppingName, table):
    import smtplib
    import email.message

    server = smtplib.SMTP('smtp.gmail.com:587')  
    corpo_email = f"""
        <p>Prezados, </p>
        <p>Segue o Relatório de Vendas</p>
        {table.to_html()}
        <p>Qualquer dúvida estou a disposição</p>
    """
    
    msg = email.message.Message()
    msg['Subject'] = f"Relatório de Vendas - {shoppingName}"
    
    msg['From'] = 'ff.cc.ss.rr@gmail.com'
    msg['To'] = 'ff.cc.ss.rr@hotmail.com'
    password = "Felipesteam2101"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

stores = sellTable["ID Loja"].unique()

for store in stores:
    storeTable = sellTable.loc[sellTable["ID Loja"] == store, ["ID Loja", "Quantidade", "Valor Final"]]
    storeTable = storeTable.groupby("ID Loja").sum()
    storeTable["Ticket Médio"] = storeTable["Valor Final"] / storeTable["Quantidade"]
    sendEmail(store, storeTable)

sendEmail("Diretoria", fullTable)

