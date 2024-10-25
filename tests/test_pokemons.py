import requests
import pytest

#________________________________________________________________

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = ''
TRAINER_ID = '11740'
HEADERS = {
  'Content-Type': 'application/json',
  'trainer_token': TOKEN
}
#________________________________________________________________

@pytest.fixture
def get_trainer():
    response = requests.request('GET', url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADERS)
    return response

def test_status_code(get_trainer):
    assert get_trainer.status_code == 200

def test_trainer_name(get_trainer):
    data = get_trainer.json()
    assert data['data'][0]["trainer_name"] == 'Абубибоба'
