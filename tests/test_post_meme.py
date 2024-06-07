import pytest
import allure

from utils.api import MemeApi
from utils.checking import Checking
from src.data.test_data_body import body

from src.pydantic_schemas.post_meme import PostMeme


class TestPostMeme:
    @allure.title('TestPostMeme')
    @pytest.mark.parametrize('data', body)
    def test_post_meme(self, data, auth):
        headers = {'Authorization': f'{auth}'}
        response = MemeApi.post_meme(data, headers)
        Checking.check_status_code(response, 200)
        Checking.check_json_scheme(response, PostMeme)

    @allure.title('TestPostMemeWithoutBody')
    def test_post_meme_without_body(self, auth):
        headers = {'Authorization': f'{auth}'}
        response = MemeApi.post_meme(None, headers)
        Checking.check_status_code_is_not(response, 200)
