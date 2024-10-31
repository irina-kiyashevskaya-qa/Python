import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e4b9628cd8902d80f5e553029d21140f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "80056",
    "name": "Мышка",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "80056"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name) 
print(response_name.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)