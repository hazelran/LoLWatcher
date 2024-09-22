# LoLWatcher
As Riot has transitioned their system away from Summoner Names to using Riot ID as an authoritative way to reference players in League and TFT. So they deprecated Riot API endpoints with Summoner Names. Here is the detailed method to get access to the data.

## Install RiotWatcher
I will connect to the Riot API using the Python Riot-Watcher package
    pip install riotwatcher

## development API key from Riot
Login or regist for the [Riot Games Developer Portal](https://developer.riotgames.com/).

Step 1. In you 'DASHBOARD' you will have your own 'DEVELOPMENT API KEY'.    
Step 2. Initially it will say your API key has expired.    
Step 3. After pushing the button 'REGENERATE API KEY', you will get an API key which is valid for 24 hours.    
Step 4. You also can check which methods you can access by 'APPS'

## Convert Riot ID to PUUID and retrieve summoner data by PUUID
    ```python
    from riotwatcher import LolWatcher, RiotWatcher, ApiError

    lol_watcher = LolWatcher('your-API-key')

    riot_watcher = RiotWatcher('your-API-key')

    region = 'na1' #depends on the summoner you search    

    """
    by_riot_id('execute region','gameName','tagLine')    
    ~In Riot Games API, different region have different execute region    
    AMERICAS: NA1, BR1, LAN, LAS, OC1    
    EUROPE: EUW1, EUNE1    
    ASIA: KR, JP1    
    """
    account = riot_watcher.account.by_riot_id('AMERICAS', 'white space', 'srtty')

    me = lol_watcher.summoner.by_puuid(my_region, my_account['puuid'])
    
    print(me)
You can visit [here](https://developer.riotgames.com/docs/lol) for more detail information about Roit ID, PUUID and summonerID. You also can find details about the execute region at 'Regional Routing Values'.
