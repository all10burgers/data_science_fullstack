import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



df = pd.read_csv('/Users/travisaltenburger/Desktop/archive/Player Shooting.csv')
print(df.head())
names_list = [name for name in df['player']]

player_shooting = {name: df[df['player'] == name].iloc[0].to_dict() for name in names_list}
for name in player_shooting:
    player_shooting[name].pop('player', None)

#print(player_shooting)
aaron_holiday_seasons = df[df['player'] == 'Aaron Holiday']

# Convert each season's stats to a dictionary and store them in a list
aaron_holiday_stats_list = [row.to_dict() for _, row in aaron_holiday_seasons.iterrows()]

# Optionally, remove the 'Player' key from each dictionary
for stats in aaron_holiday_stats_list:
    stats.pop('player', None)

# Display the list of dictionaries
print(aaron_holiday_stats_list)
#print(names_list)
#df.set_index('player', inplace=True)



#player_stats_dict = df.to_dict(orient='index')

#print(player_stats_dict)
# def get_player_shooting(player):
    
#     df = pd.read_csv('/Users/travisaltenburger/Desktop/archive/Player Shooting.csv')
#     df.set_index('Player', inplace=True)

#     player_stats_dict = df.to_dict(orient='index')

#     print(player_stats_dict)






