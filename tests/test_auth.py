import pytest
import allure

from utils.api import MemeApi
from utils.checking import Checking
from src.pydantic_schemas.post_authorize import PostAuthorize
from src.data.test_data_auth import data_auth_positive_name, data_auth_negative_name


class TestAuth:
    @allure.title('TestAuth positive')
    @pytest.mark.parametrize("body", data_auth_positive_name)
    def test_auth_positive(self, body):
        response = MemeApi.authorize(body)
        Checking.check_status_code(response, 200)
        Checking.check_json_scheme(response, PostAuthorize)
        Checking.check_existence_key_value(response, 'user', f'{body["name"]}')

    @allure.title('TestAuth positive')
    @pytest.mark.parametrize("body", data_auth_negative_name)
    def test_auth_negative(self, body):
        response = MemeApi.authorize(body)
        Checking.check_status_code(response, 400)