import allure

from utils.api import MemeApi
from utils.checking import Checking

body = {
    'text': "mytext",
    'url': "tut.by",
    'tags': ['1', '2', '3'],
    'info': {
        'colors': ['red', 'green', 'blue']
    }
}


class TestDeleteMeme:
    @allure.title('TestDelete positive')
    def test_delete_meme_positive(self, auth):
        header = {'Authorization': f'{auth}'}
        response = MemeApi.post_meme(body, header)
        meme_id = response.json()['id']
        response = MemeApi.delete_meme(meme_id, header)
        Checking.check_status_code(response, 200)

    @allure.title('TestDelete negative')
    def test_delete_meme_negative(self, auth):
        header = {'Authorization': f'{auth}'}
        response = MemeApi.delete_meme(10000000, header)
        Checking.check_status_code(response, 404)
