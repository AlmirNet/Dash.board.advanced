import pandas as pd
import os



data_structure = {
    'Valor': [],
    'Efetuado': [],
    'Fixo': [],
    'Data': [],
    'Categoria': [],
    'Descricao': [],
}

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
else:
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv", index=False)
    df_receitas.to_csv("df_receitas.csv", index=False)

if ("df_cat_despesas.csv" in os.listdir()) and ("df_cat_receitas.csv" in os.listdir()):
    df_cat_despesas = pd.read_csv("df_cat_despesas.csv", index_col=0)
    df_cat_receitas = pd.read_csv("df_cat_receitas.csv", index_col=0)
    cat_receita = df_cat_receitas.values.tolist()
    cat_despesa = df_cat_despesas.values.tolist()
else:
    cat_receitas = {'Categoria': ["Salario", "Investimento", "Comissao"]}
    cat_despesas = {'Categoria': ["Alimentacao", "Aluguel", "Saude"]}

    df_cat_receitas = pd.DataFrame(cat_receitas, columns=['Categoria'])
    df_cat_despesas = pd.DataFrame(cat_despesas, columns=['Categoria'])
    df_cat_despesas.to_csv("df_cat_despesas.csv", index=False)
    df_cat_receitas.to_csv("df_cat_receitas.csv", index=False)
