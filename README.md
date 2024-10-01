# LoLWatcher
As Riot has transitioned their system away from Summoner Names to using Riot ID as an authoritative way to reference players in League and TFT. So they deprecated Riot API endpoints with Summoner Names. Here is the detailed method to get access to the data.

## Install RiotWatcher
I will connect to the Riot API using the Python Riot-Watcher package
    pip install riotwatcher

## development API key from Riot
Login or regist for the [Riot Games Developer Portal](https://developer.riotgames.com/).

Step 1. In you 'DASHBOARD' you will have your own `DEVELOPMENT API KEY`.    
Step 2. Initially it will say your API key has expired.    
Step 3. After pushing the button `REGENERATE API KEY`, you will get an API key which is valid for 24 hours.    
Step 4. You also can check which methods you can access through `APPS`

## Convert Riot ID to PUUID and retrieve summoner data by PUUID
```python
# Initialize the LolWatcher and RiotWatcher classes with your Riot API key.
# These classes provide methods for interacting with Riot Games' API for League of Legends data.
from riotwatcher import LolWatcher, RiotWatcher, ApiError

# LolWatcher is used specifically to interact with League of Legends endpoints, 
# such as retrieving summoner information, match history, and game data.
lol_watcher = LolWatcher('your-API-key')    

# RiotWatcher is a broader class that can be used to access various Riot Games APIs, 
# including League of Legends and other games (such as VALORANT).
riot_watcher = RiotWatcher('your-API-key')
```

### In Riot Games API, different region have different execute region
```python
# Depends on the summoner you search
region = 'na1'
exe_region = 'AMERICAS' 
```
### Reference
| execute region | region |
| -- | -- |
|  AMERICAS | NA1 |
|  | BR1 |
|  | LAN |
|  | OC1 |
| EUROPE | EUW1 |
|  | EUNE1 |
| ASIA | KR |
|  | JP1 |

#### `riot_watcher.account.by_riot_id('AMERICAS', 'white space', 'srtty')`
This function fetches account data for the summoner with the given Riot ID (`'white space'` as the name and `'srtty'` as the tag) in the AMERICAS execute region.
```python
# Retrieve account information by Riot ID using the RiotWatcher instance.
# The 'by_riot_id' method requires the region, summoner name ('white space' in this case), and tag ('srtty').
account = riot_watcher.account.by_riot_id('AMERICAS', 'white space', 'srtty')
```

#### `lol_watcher.summoner.by_puuid(my_region, account['puuid'])`
This retrieves summoner information from the League of Legends API based on the player's PUUID (which is fetched from the previous `account` lookup).
```python
# Retrieve summoner information by their PUUID (Player Unique ID) using the LolWatcher instance.
# This uses the 'summoner.by_puuid' method, which requires the region and PUUID (from the previous account lookup).
me = lol_watcher.summoner.by_puuid(my_region, account['puuid'])
```

## Print the retrieved summoner data (this includes summoner name, level, etc.).
#### `print(me)`
This prints out the summoner's data, such as their summoner name, level, etc.
```python
print(me)
```

You can visit [here](https://developer.riotgames.com/docs/lol) for more detail information about Roit ID, PUUID and summonerID. You also can find details about the execute region at `Regional Routing Values`.

## Get a List of latest matches
```python
match = lol_watcher.match.matchlist_by_puuid(region, me['puuid'], count = 1)
```

## Get detailed information on every match
```python
match_list = lol_watcher.match.by_id(exe_region, match[0])

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
```
## Convert match data into DataFrame
```python
match_df = pd.DataFrame(all_match_data)
```
