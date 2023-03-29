import requests
from lib.base_case import BaseCase
from lib.assertion import Assertions


class TestUserGet(BaseCase):
    """"Create method with wrong credentials 'user_name'"""
    def test_get_user_details_not_auth_negative(self):
        user_name = 123456789123456789
        url = f"https://petstore.swagger.io/v2/user/{user_name}"
        expected_list = ["code", "type", "message"]
        response = requests.get(url)

        Assertions.assert_status_code(response, 404)
        Assertions.assert_has_keys(response, expected_list)

    def test_get_user_details(self):
        url = f"https://petstore.swagger.io/v2/user/{self.id_value}" # NEED ADD ID_VALUE
        expected_list = ["code", "type", "message"]
        response = requests.get(url)

        Assertions.assert_status_code(response, 404)
        Assertions.assert_json_has_key(response, expected_list)

    """Method for user authentication"""
    def test_get_user_details_auth_as_some_user(self):
        date = {
            "username": "user_name_test",
            "password": "password_123",
        }
        headers = {
            "Content-Type": "application/json"
        }
        expected_list = []
        url = "https://petstore.swagger.io/v2/user/login"

        response = requests.post(url, data=data, headers=headers)

