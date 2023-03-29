import json.decoder
from datetime import datetime
from requests import Response


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

    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = "qa_test"
            domain = "gmail.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            "id": 0,
            "username": "user_name_test",
            "firstName": "first_name_test",
            "lastName": "last_name_string",
            "email": email,
            "password": "password_123",
            "phone": "0966050097",
            "userStatus": 0
        }


