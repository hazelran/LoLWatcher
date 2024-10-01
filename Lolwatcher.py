import pandas as pd
from riotwatcher import LolWatcher, RiotWatcher, ApiError

lol_watcher = LolWatcher('Your-API')
riot_watcher = RiotWatcher('Your-API')

region = 'kr'
account = riot_watcher.account.by_riot_id('ASIA', 'T1 Gumayusi', 'KR1')
me = lol_watcher.summoner.by_puuid(region, account['puuid'])

# Get a list of the latest matches
match = lol_watcher.match.matchlist_by_puuid(region, me['puuid'], count = 1)

kr_region = 'ASIA'
match_list = lol_watcher.match.by_id(kr_region, match[0])

# Match data list
all_match_data = []

for team in match_list['info']['teams']:
    match_info = {
        'teamId': team['teamId'],
        'win': team['win'],
        'firstBlood': team.get('objectives', {}).get('firstBlood', {}).get('first', False),
        'firstTower': team.get('objectives', {}).get('tower', {}).get('first', False),
        'firstInhibitor': team.get('objectives', {}).get('inhibitor', {}).get('first', False),
        'firstBaron': team.get('objectives', {}).get('baron', {}).get('first', False),
        'firstDragon': team.get('objectives', {}).get('dragon', {}).get('first', False),
        'firstRiftHerald': team.get('objectives', {}).get('riftHerald', {}).get('first', False),
        'towerKills': team.get('objectives', {}).get('tower', {}).get('kills', 0),
        'inhibitorKills': team.get('objectives', {}).get('inhibitor', {}).get('kills', 0),
        'baronKills': team.get('objectives', {}).get('baron', {}).get('kills', 0),
        'dragonKills': team.get('objectives', {}).get('dragon', {}).get('kills', 0),
        'riftHeraldKills': team.get('objectives', {}).get('riftHerald', {}).get('kills', 0),
        'region': region
    }
    all_match_data.append(match_info)  # Add data to the list
match_info

# Convert match data into DataFrame
match_df = pd.DataFrame(all_match_data)
