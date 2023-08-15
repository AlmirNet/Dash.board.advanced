# Em components/dashboard existe esta importação 'from globals import *' importando esta pasta globals
import pandas as pd
import os 

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):