import json

from lib.base_case import BaseCase
from lib.assertion import Assertions
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):

    def test_edit_just_created_user(self):
        # REGISTER
        registration_data = self.prepare_registration_data()
        registration_data_str = json.dumps(registration_data)
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        response_user = MyRequests.post("/user", data=registration_data_str, headers=headers)

        expected_user_id = registration_data["id"]
        expected_dict = {
            "code": 200,
            "type": "unknown",
            "message": str(expected_user_id)
        }

        Assertions.assert_status_code(response_user, 200)
        Assertions.assert_expected_dict(response_user, expected_dict)

        username = registration_data["username"]
        first_name = registration_data["firstName"]
        password = registration_data["password"]
        user_id = registration_data["id"]

        # LOGIN
        login_data = {
            "username": username,
            "password": password
        }
        response_login = MyRequests.get("/user/login", data=login_data)

        Assertions.assert_status_code(response_login, 200)

        #auth_sid = self.get_cookie(response_login, "auth_sid")
        #token = self.get_headers(response_login, "x-csrf-token")

        # LOGOUT
        response_logout = MyRequests.get(f"/user/logout", headers=headers)
        Assertions.assert_status_code(response_logout, 200)


        # EDIT

        data_put = self.prepare_registration_data()
        data_put_str = json.dumps(data_put)

        response_edit = MyRequests.put(f"/user/{user_id}", data=data_put_str, headers=headers)
        Assertions.assert_status_code(response_edit, 200)

        # GET
        data_put_as_dict = data_put
        username = data_put_as_dict["username"]



        response_get = MyRequests.get(f"/user/{username}", headers=headers)

        Assertions.assert_status_code(response_get, 200)
        Assertions.assert_expected_dict(response_get, data_put_as_dict)
