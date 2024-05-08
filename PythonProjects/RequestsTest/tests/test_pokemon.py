import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'db3871d7895e6aca37783e685449f099'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = '2559'

def test_status_code():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainers():
    response_trainers=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_trainers.json()["data"][0]["trainer_name"] == 'Феня'

