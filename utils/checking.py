from requests import Response
import json

from src.enums.global_enums import GlobalErrorMessages


class Checking:
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert response.status_code == status_code, (GlobalErrorMessages.WRONG_STATUS_CODE.value +
                                                     f' Received status code: {response.status_code}.' +
                                                     f' Expected status code: {status_code}')

    @staticmethod
    def check_status_code_is_not(response: Response, status_code):
        assert response.status_code != status_code, (GlobalErrorMessages.WRONG_STATUS_CODE.value +
                                                     f' Received status code: {response.status_code}.' +
                                                     f' Expected status code is not: {status_code}')

    @staticmethod
    def check_existence_key(response: Response, expected_key):
        response = response.json()
        assert expected_key in list(response), GlobalErrorMessages.WRONG_STATUS_KEY.value

    @staticmethod
    def check_existence_key_value(response: Response, field_name, expected_value):
        response = response.json()
        check_value = response.get(field_name)
        assert check_value == expected_value, GlobalErrorMessages.WRONG_STATUS_VALUE.value

    @staticmethod
    def check_json_scheme(response: Response, scheme):
        response = response.json()
        scheme.model_validate(response)

    @staticmethod
    def check_response_text(response: Response, text):
        response = response.text
        assert response == text, (GlobalErrorMessages.WRONG_RESPONSE_TEXT.value +
                                  f' Received response text: "{response}" . '
                                  f'Expected response text: "{text}"')

    @staticmethod
    def check_diff_response_requests_body(response: Response, expected_response_body):
        # response = response.json()
        # expected_response_body = json.loads(expected_response_body)
        # expected_response_body = expected_response_body.json()
        print(f'expected_response_body: {expected_response_body}')
        print(f'response: {response.json()}')
        # assert sorted(response) == sorted(
        #     expected_response_body), GlobalErrorMessages.WRONG_RESPONSE_BODY

        assert sorted(response.json()) == sorted(expected_response_body), GlobalErrorMessages.WRONG_RESPONSE_BODY

