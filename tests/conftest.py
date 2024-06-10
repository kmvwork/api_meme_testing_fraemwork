import pytest

from utils.api import MemeApi
from src.data.test_data_auth import data_auth_positive_name, data_auth_name_and_token, data_auth_negative_token


@pytest.fixture
def auth(test_name='test'):
    body = {'name': f'{test_name}'}
    response = MemeApi.authorize(body)
    return response.json()['token']


@pytest.fixture
def auth_generate_positive():
    data_auth_name_and_token.clear()
    for item in data_auth_positive_name:
        response = MemeApi.authorize(item)
        data_auth_name_and_token.append({'token': response.json()['token'], 'name': response.json()['user']})
    return data_auth_name_and_token


@pytest.fixture
def auth_generate_negative():
    return data_auth_negative_token


@pytest.fixture
def create_meme(auth):
    body = {
        'text': "mytext",
        'url': "tut.by",
        'tags': ['1', '2', '3'],
        'info': {
            'colors': ['red', 'green', 'blue']
        }
    }
    header = {'Authorization': f'{auth}'}
    response = MemeApi.post_meme(body, header)
    yield response
    MemeApi.delete_meme(response.json()['id'], header)
