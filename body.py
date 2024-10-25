import json

def my_pokemon_data():
    with open('myPokemons.json', 'r', encoding='utf-8') as f:
        pokemon_data = json.load(f)
        return pokemon_data['data'][0]


# Функцию для формирования PUT_pokemons
def get_put_pokemons():
    pokemon = my_pokemon_data()
    if pokemon:
        return {
            "pokemon_id": str(pokemon['id']),
            "name": 'Успешный Статус',
            "photo_id": int(pokemon['photo_id'])
        }

# Функция для получения pokemon_id для покебола
def get_pokeball_data():
    pokemon = my_pokemon_data()
    if pokemon:
        return {
            "pokemon_id": str(pokemon['id'])
        }

# Создание покемона
POST_pokemons = {
    "name": "generate",
    "photo_id": -1
}

# Смена имени покемона
PUT_pokemons = get_put_pokemons()

# Поймать покемона в покебол
POST_trainers_add_pokebal = get_pokeball_data()