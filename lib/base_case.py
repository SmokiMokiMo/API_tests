import json.decoder
from datetime import datetime
from requests import Response
import random
import string


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookies with name {cookie_name} in last response"
        return response.cookies[cookie_name]

    def get_headers(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find headers with name {headers_name} in last response"
        return response.headers[headers_name]

    def json_values(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON doesn`t have key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, id_user=None, username=None, email=None, password=None):
        if email is None:
            base_part = "qatest"
            domain = "gmail.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        if username is None:
            letters = string.ascii_lowercase
            username = ''.join(random.choice(letters) for i in range(19))
        if password is None:
            password = random.randint(10 ** 18, (10 ** 19) - 1)
        if id_user is None:
            id_user = random.randint(1, 10 ** 19 - 1)
        return {
            "id": int(id_user),
            "username": str(username),
            "firstName": "ihor",
            "lastName": "zayats",
            "email": str(email),
            "password": str(password),
            "phone": "31451",
            "userStatus": 1
        }


