import requests
import json
from decouple import config

API_KEY = config('API_KEY')
URL = 'https://public-api.tracker.gg/v2/apex/standard/'

# Função que obtêm informações gerais do perfil do player
def get_player_profile(platform, user_id):
    params = {'TRN-Api-Key': API_KEY}
    path = f'profile/{platform}/{user_id}'
    
    req = requests.get(URL + path, params=params)
    return json.loads(req.text)['data']

# Função que obtêm status das lendas do player
def get_stats_legends(platform, user_id):
    params = {'TRN-Api-Key': API_KEY}
    path = f'profile/{platform}/{user_id}/segments/legend'
    
    req = requests.get(URL + path, params=params)
    return json.loads(req.text)
    
# Chamada da função
'''info_player =  get_player_profile('origin', 'tmielnik')
print(json.dumps(info_player, indent = 2))'''

# Chamada da função
info_segment = get_stats_legends('origin', 'tmielnik')
print(json.dumps(info_segment, indent = 2))
