import pytest

from utils.api import MemeApi
from utils.checking import Checking

testdata = [
    {'token': 'Bh5gPLXXkNATnSa', 'name': "max"}
]


class TestCheckToken:
    def test_check_token_positive(self, auth_generate_positive):
        for item in auth_generate_positive:
            text = f'Token is alive. Username is {item["name"]}'
            response = MemeApi.check_authorization(item['token'])
            Checking.check_status_code(response, 200)
            Checking.check_response_text(response, text)

    def test_check_token_negative(self, auth_generate_negative):
        for item in auth_generate_negative:
            response = MemeApi.check_authorization(item['token'])
            Checking.check_status_code(response, 404)
