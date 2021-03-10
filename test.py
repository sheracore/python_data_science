import pandas as pd
import numpy as np
from nba_api.stats.static import teams


nba_teams = teams.get_teams()
keys = nba_teams[0].keys()
one_dict = {key:[] for key in keys}

for item in nba_teams:
    for key, value in item.items():
        one_dict[key].append(value)

df_teams = pd.DataFrame(one_dict)
#print(df_teams)

df_warriors = df_teams[df_teams['state'] == 'New York']
print(df_warriors)
warriors_id = df_warriors[["id"]].values
warriors_id = warriors_id[0][0]


from nba_api.stats.endpoints import leaguegamefinder

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=warriors_id)
games = gamefinder.get_data_frames()[0]
print(games.head())
games_home = games[games['MATCHUP'] == 'BKN @ HOU']
games_away = games[games['MATCHUP'] =='BKN vs. DAL']
print("__________________________")
print(games_home.head())
print(games_away.head())



df = pd.read_csv("SLA-3G_A3.csv")
print(df.head())
#print(df["RRC_SETUP_SR_ALL"].unique())

list = df["RRC_SETUP_SR_ALL"].unique()
for item in list:
    #print(item)
    pass

list = df["RRC_SETUP_SR_ALL"] >= 0.3582
for item in list:
    #print(item)
    pass

#print(df["VOLTE_CDR"] >= 0.3582)
#print(df[df["VOLTE_CDR"] >= 0.3582])

#print(df[df["SECTOR"] == 'LH1064XC'])

#print(dir(df))
#print(df.iloc[3,8])
#print(df.iloc[0:3,0:8])
#print("********************")
#print(df.loc[1,"PAGING_DELETATION_RATE"])

dict = {"a":[1,2,3,4,5],
        "b":[6,7,8,9,0],
        "c":["a","b","c","d","e"]}

df = pd.DataFrame(dict)


with open("SLA-3G_A3.csv", "r")as file:
    FileContent = file.readline()
    print(FileContent)

#print(df)
#print(df[["b"]])


u = np.array([1,2])
v = np.array([4,5])
z = u*v
print(z)
result = np.dot(u,v)
print(result)





