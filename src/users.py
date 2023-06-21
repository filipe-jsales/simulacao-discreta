import pandas as pd
from src.user import User
lista_clientes = []
x = pd.read_excel("users.xlsx", header=None, engine="openpyxl")
qtd_clientes = 50

for index in range(qtd_clientes):
    user_infos = x.iloc[[index]].values
    user_id = user_infos[0][0]
    birth_date = user_infos[0][1]
    sex = user_infos[0][2]
    lista_clientes.append(User(user_id, birth_date, sex)) #user_id, birth_date, sex

def busca_clientes():
    return lista_clientes


