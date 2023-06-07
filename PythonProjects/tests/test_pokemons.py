import requests
import pytest

host = 'https://pokemonbattle.me:9104'


def test_status_code():

    answer = requests.get(f'{host}/trainers')
    
    assert answer.status_code == 200


def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers', params={'trainer_id': 4656})

    assert answer_body.json()['trainer_name'] == 'Elena'


@pytest.mark.parametrize('key, value', [('trainer_name', 'Elena'),
                                        ('id', '4656'),
                                        ('city', 'Novosibirsk')])

def test_part_of_answer(key, value):
    answer_body = requests.get(f'{host}/trainers', params={'trainer_id': 4656})
    assert answer_body.json()[key] == value