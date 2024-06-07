import allure

from utils.api import MemeApi
from utils.checking import Checking
from src.pydantic_schemas.put_meme import PutMeme

body = {
    'text': "mytext",
    'url': "tut.by",
    'tags': ['1', '2', '3'],
    'info': {
        'colors': ['red', 'green', 'blue']
    }
}


class TestPutMeme:
    @allure.title('TestPutMemePositive')
    def test_put_meme_positive(self, auth):
        header = {'Authorization': f'{auth}'}
        response = MemeApi.post_meme(body, header)
        meme_id = response.json()['id']
        new_body = {
            'id': meme_id,
            'text': "mytext",
            'url': "tut.by",
            'tags': ['1', '2', '3'],
            'info': {
                'colors': ['red', 'green', 'yellow']
            }
        }
        response = MemeApi.put_meme(meme_id, new_body, header)
        Checking.check_status_code(response, 200)
        Checking.check_json_scheme(response, PutMeme)

    @allure.title('TestPutMemePNegative')
    def test_put_meme_negative(self, auth):
        header = {'Authorization': f'{auth}'}
        response = MemeApi.post_meme(body, header)
        meme_id = response.json()['id']
        new_body = {}
        response = MemeApi.put_meme(meme_id, new_body, header)
        Checking.check_status_code_is_not(response, 200)
