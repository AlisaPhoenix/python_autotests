import requests 

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'db3871d7895e6aca37783e685449f099'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
BODY_POKENON = {
    "name": "Рикитикитави",
    "photo": "https://dolnikov.ru/pokemons/albums/019.png"
}
CHANGE_NAME = {
    "pokemon_id": "26297",
    "name": "Pink",
    "photo": "https://dolnikov.ru/pokemons/albums/039.png"
}
ADD_POKEBALL = {
    "pokemon_id": "26297"
}

 
response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER,  json = BODY_POKENON)
print(response_create.text)

response_change_name = requests.put(url = f'{URL}/pokemons' , headers=HEADER, json=CHANGE_NAME)
print(response_change_name.text)

response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER , json =ADD_POKEBALL)
print(response_add_pokeball.text)