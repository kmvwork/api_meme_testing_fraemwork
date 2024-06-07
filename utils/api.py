from configuration import BASE_URL_AUTH, BASE_URL_MEME

import requests


class MemeApi:
    @staticmethod
    def authorize(body=None):
        response = requests.post(BASE_URL_AUTH, json=body)
        return response

    @staticmethod
    def check_authorization(token):
        get_authorize_url = BASE_URL_AUTH + '/' + token
        response = requests.get(get_authorize_url)
        return response

    @staticmethod
    def get_memes(headers):
        response = requests.get(BASE_URL_MEME, headers=headers)
        return response

    @staticmethod
    def get_meme_by_id(id_meme, headers):
        get_url_by_id = BASE_URL_MEME + '/' + str(id_meme)
        response = requests.get(get_url_by_id, headers=headers)
        return response

    @staticmethod
    def post_meme(body, headers):
        result_meme = requests.post(BASE_URL_MEME, json=body, headers=headers)
        return result_meme

    @staticmethod
    def put_meme(id_meme, body, headers):
        put_url_by_id = BASE_URL_MEME + '/' + str(id_meme)
        response = requests.put(put_url_by_id, json=body, headers=headers)
        return response

    @staticmethod
    def delete_meme(id_meme, headers):
        delete_url_by_id = BASE_URL_MEME + '/' + str(id_meme)
        response = requests.delete(delete_url_by_id, headers=headers)
        return response
