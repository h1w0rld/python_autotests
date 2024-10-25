import requests
import json
from body import POST_pokemons, PUT_pokemons, POST_trainers_add_pokebal

#________________________________________________________________

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = ''
TRAINER_ID = '11740'
HEADERS = {
  'Content-Type': 'application/json',
  'trainer_token': TOKEN
}
#________________________________________________________________

# Создание покемона
res_POST_pokemons = requests.request('POST', url = f'{URL}/pokemons', headers = HEADERS, json = POST_pokemons)

print(res_POST_pokemons.text)

# Список моих покемонов
res_GET_pokemons = requests.request('GET', url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID, 'status' : 1}, headers = HEADERS)

myPokemons = res_GET_pokemons.json()
with open('myPokemons.json', 'w', encoding='utf-8') as f:
      json.dump(myPokemons, f, ensure_ascii=False, indent=4)

pokemon_id = res_GET_pokemons.json()['data'][0]['id']
print(pokemon_id)

# Смена имени покемона
res_PUT_pokemons = requests.request('PUT', url = f'{URL}/pokemons', headers = HEADERS, json = PUT_pokemons)

print(res_PUT_pokemons.text)

# Поймать покемона в покебол
res_POST_trainers_add_pokebal = requests.request('POST', url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = POST_trainers_add_pokebal)

print(res_POST_trainers_add_pokebal.text)