import pandas as pd
import requests
import openpyxl
# pd.set_option('display.max_columns', None)
url = "https://api.football-data-api.com/league-matches?key=example&league_id=2012"
data = requests.get(url)
# print(data)
resp = data.json()
# print(resp)
resp = data.json()['data']
# print(resp)
dados = pd.DataFrame.from_dict(resp)
# print(dados)
dados.to_excel("league_matches.xlsx", encoding='urf-8', index=False)




