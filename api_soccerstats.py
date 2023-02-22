import pandas as pd
import requests

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

url_1 = "https://www.soccerstats.com/matches.asp?matchday=1&listing=1"
url_2 = "https://www.soccerstats.com/matches.asp?matchday=1&listing=2"

r1 = requests.get(url_1, headers=header)
r2 = requests.get(url_2, headers=header)

df1 = pd.read_html(r1.text)
df2 = pd.read_html(r2.text)

len(df1)
df1[6]
len(df2)
df2[6]
print(df1)

jogos_dia1 = df1 [6]
jogos_dia1 = jogos_dia1[['Country','2.5+','1.5+','GA','GF','TG','PPG','Unnamed: 9','Unnamed: 10','Unnamed: 11','PPG.1','TG.1','GF.1','GA.1','1.5+.1','2.5+.1']]
jogos_dia1.columns = ['País','Over25_H','Over15_H','GolsSofridos_H','GolsMarcados_H','MediaGols_H','PPG_H','Home','Hora','Away','PPG_A','MediaGols_A','GolsMarcados_A','GolsSofridos_A','Over15_A','Over25_A']

jogos_dia2 = df2 [6]
jogos_dia2 = jogos_dia2[['BTS','W%','BTS.1','W%.1']]
jogos_dia2.columns = ['BTTS_H','%Vitorias_H','BTTS_A','%Vitorias_A']

jogos_dia = pd.concat([jogos_dia1, jogos_dia2], axis=1)
jogos_dia = jogos_dia[['País','Hora','Home','Away','%Vitorias_H','%Vitorias_A','Over15_H','Over25_H','Over15_A','Over25_A','BTTS_H','BTTS_A','GolsMarcados_H','GolsSofridos_H','GolsMarcados_A','GolsSofridos_A','MediaGols_H','MediaGols_A','PPG_H','PPG_A']]

jogos_dia = jogos_dia.sort_values('Hora')
jogos_dia['Hora'] = pd.to_datetime(jogos_dia['Hora']) - pd.DateOffset(hours=4)
jogos_dia['Hora'] = pd.to_datetime(jogos_dia['Hora'], format= '%H:%M').dt.time
jogos_dia = jogos_dia.dropna()

jogos_dia.reset_index(inplace=True, drop=True)
jogos_dia.index = jogos_dia.index.set_names(['Nº'])
jogos_dia = jogos_dia.rename(index=lambda x: x + 1)

# jogos_dia.to_excel("jogos de hoje.xlsx")

df = jogos_dia


flt = (df.GolsMarcados_H > 1) & (df.GolsSofridos_H > 1) & (df.GolsMarcados_A > 1) & (df.GolsSofridos_A > 1) & (df.MediaGols_H > 1) & (df.MediaGols_A > 1)
df1 = df[flt]
print(df1)
