from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://tracker.gg/lol/leaderboards/stats/all/LeaguePoints?region=NA&queueType=RANKED_SOLO_5x5")

driver.implicitly_wait(3)

na_leaderboard = driver.find_elements(By.TAG_NAME, 'tr')

overall_position = []
player_name = []
rank = []
league_points = []
win_rate = []
matches_played = []

for player in na_leaderboard:

    new_list = player.text.split()

    if len(new_list) == 6:

        overall_position.append(new_list[0])
        player_name.append(new_list[1])
        rank.append(new_list[2])
        league_points.append(new_list[3])
        win_rate.append(new_list[4])
        matches_played.append(new_list[5])

    elif len(new_list) == 7:

        two_name_player = new_list[1] + new_list[2]

        overall_position.append(new_list[0])
        player_name.append(two_name_player)
        rank.append(new_list[3])
        league_points.append(new_list[4])
        win_rate.append(new_list[5])
        matches_played.append(new_list[6])

    elif len(new_list) == 8:

        three_name_player = new_list[1] + new_list[2] + new_list[3]

        overall_position.append(new_list[0])
        player_name.append(three_name_player)
        rank.append(new_list[4])
        league_points.append(new_list[5])
        win_rate.append(new_list[6])
        matches_played.append(new_list[7])

print(overall_position)
print(player_name)
print(rank)
print(league_points)
print(win_rate)
print(matches_played)

assert (overall_position != []), 'list is empty'
assert (player_name != []), 'list is empty'
assert (rank != []), 'list is empty'
assert (league_points != []), 'list is empty'
assert (win_rate != []), 'list is empty'
assert (matches_played != []), 'list is empty'

driver.quit()

import pandas as pd

df = pd.DataFrame({
    "overall_position": overall_position,
    "player_name": player_name,
    "rank": rank,
    "league_points": league_points,
    "win_rate": win_rate,
    "matches_played": matches_played
})

print(df)

df.to_csv("na_leaderboard.csv", index=False)