from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertions


class TestUserGet(BaseCase):
    """"Create method with wrong credentials 'user_name'"""
    def test_get_user_details_not_auth_negative(self):
        user_name = str(123456789123456789)
        expected_list_keys = ["code", "type", "message"]
        response = MyRequests.get(f"/user/{user_name}")

        Assertions.assert_status_code(response, 404)
        Assertions.assert_has_keys(response, expected_list_keys)

    def test_get_user_details(self):
        expected_list_keys = ["code", "type", "message"]
        response = MyRequests.get("/user/user")

        Assertions.assert_status_code(response, 404)
        Assertions.assert_has_keys(response, expected_list_keys)

    """Method for user authentication"""
    def test_get_user_details_auth_as_some_user(self):
        date = {
            "username": "SmokiMokiMo",
            "password": "9999999999999999999999999999999999999999999999999999999999999999999888877",
        }
        headers = {
            "Content-Type": "application/json"
        }
        expected_list_keys = ["code", "type", "message"]


        response = MyRequests.post("/user/login", data=date, headers=headers)

        #Assertions.assert_status_code(response, 404)
        #Assertions.assert_has_keys(response, expected_list_keys)

