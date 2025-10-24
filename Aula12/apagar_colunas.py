import pandas as pd

df_titanic = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')

drop_ticket = df_titanic.drop(columns=['Ticket'])

print(drop_ticket.head())