from lib.assertion import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import lib.logger
import json


class TestUserPetStore(BaseCase):
    def test_user_registration(self):
        """New user registration"""
        # Preparing the data input datas using
        registration_data = self.prepare_registration_data()
        registration_data_dict = json.dumps(registration_data)

        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        # Preparing the data for asserting
        expected_username = registration_data["username"]
        expected_user_id = registration_data["id"]
        expected_username_email = registration_data["email"]
        expected_username_passwd = registration_data["password"]
        expected_keys = ["code", "type", "message"]
        expected_values = [200, "unknown", str(expected_user_id)]
        expected_dict = {
            "code": 200,
            "type": "unknown",
            "message": str(expected_user_id)
        }

        # Send 'POST' request on '/user' end point
        response_post = MyRequests.post("/user", data=registration_data_dict, headers=headers)

        # We check the received data
        Assertions.assert_status_code(response_post, 200)
        Assertions.assert_expected_dict(response_post, expected_dict)
        Assertions.assert_json_has_key(response_post, expected_keys)
        Assertions.assert_json_has_values(response_post, expected_values)

        """Get user by user name"""
        #Send 'GET' request on '/user/{username}' end point
        response = MyRequests.get(f"/user/{expected_username}")

        # Preparing the data for asserting
        expected_dict_get = registration_data_dict

        # We check the received data
        Assertions.assert_status_code(response, 200)
        Assertions.assert_value_by_name(response, expected_username)
        Assertions.assert_expected_dict(response, registration_data)


        """Put update user"""
        # Updated user datas
        registration_data_put = self.prepare_registration_data()
        registration_data_json = json.dumps(registration_data_put)


        # Send 'PUT' request on '/user/{username}'end point
        response_put = MyRequests.put(f"/user/{expected_username}", data=registration_data_json, headers=headers)

        # Preparing the data for asserting
        response_put_dict = json.loads(response_put)
        expected_id_put = response_put_dict["id"]
        expected_dict_put = {
            "code": 200,
            "type": "unknown",
            "message": str(expected_id_put)
        }

        # We check the received data
        Assertions.assert_status_code(response, 200)
        Assertions.assert_expected_dict(response_put, expected_dict_put)

        """Logs user into the system '/user/login'"""
        # Preparing  authorization datas
        login_pass = registration_data_put["password"]
        authorization_datas = {
            "username": str(expected_username),
            "password": str(login_pass)
        }
        # Send 'GET' request on '/user/login' end point
        response_login = MyRequests.get("/user/login", data=authorization_datas)

        #

        expected_message = f"logged in user session:{expected_id_put}"
        expected_dict_login = {
            "code": 200,
            "type": "unknown",
            "message": str(expected_message)
        }
        # We check the received data
        Assertions.assert_status_code(response, 200)
        Assertions.assert_expected_dict(response_login, expected_dict_login)

        #"""Logs out current logged in user session on end point '/user/logout'"""





