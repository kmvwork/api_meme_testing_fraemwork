import allure

from utils.api import MemeApi
from utils.checking import Checking

from src.pydantic_schemas.get_meme_by_id import GetMemeById


class TestGetMeme:
    @allure.title('TestGetMemeByID')
    def test_get_meme_by_id(self, auth, create_meme):
        meme_id = create_meme.json()['id']
        body = {'Authorization': f'{auth}'}
        response = MemeApi.get_meme_by_id(meme_id, body)
        Checking.check_status_code(response, 200)
        Checking.check_json_scheme(response, GetMemeById)

    @allure.title('TestGetMemeWithoutID')
    def test_get_meme_without_id(self, auth):
        body = {'Authorization': f'{auth}'}
        response = MemeApi.get_meme_by_id('', body)
        Checking.check_status_code(response, 404)

    @allure.title('TestGetMemeWithIncorrectID')
    def test_get_meme_with_incorrect_id(self, auth, create_meme):
        meme_id = 'tertretretdfgdfgdf'
        body = {'Authorization': f'{auth}'}
        response = MemeApi.get_meme_by_id(meme_id, body)
        Checking.check_status_code(response, 404)
