import allure

from utils.api import MemeApi
from utils.checking import Checking

from src.pydantic_schemas.get_memes import GetMemes


class TestGetMemes:
    @allure.title('TestGetMemes')
    def test_get_memes(self, auth):
        body = {'Authorization': f'{auth}'}
        response = MemeApi.get_memes(body)
        Checking.check_status_code(response, 200)
        Checking.check_json_scheme(response, GetMemes)

    @allure.title('TestGetMemesWithoutToken')
    def test_get_memes_without_token(self):
        response = MemeApi.get_memes(None)
        Checking.check_status_code(response, 401)

    @allure.title('TestGetMemesWithInvalidD')
    def test_get_memes_with_invalid_token(self):
        body = {'Authorization': 'random'}
        response = MemeApi.get_memes(body)
        Checking.check_status_code(response, 401)
