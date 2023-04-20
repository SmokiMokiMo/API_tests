import json
import allure

from lib.base_case import BaseCase
from lib.assertion import Assertions
from lib.my_requests import MyRequests


@allure.epic("Performs main API points Register/Login/Login/Edit/GetUser. ")
class TestUserEdit(BaseCase):
    username = None
    password = None
    user_id = None
    headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
    data_put = None

    @allure.description("This test successfully register new user")
    def test_created_new_user(self):
        # REGISTER
        registration_data = self.prepare_registration_data()
        registration_data_str = json.dumps(registration_data)
        self.username = registration_data["username"]
        self.password = registration_data["password"]
        self.user_id = registration_data["id"]

        response_user = MyRequests.post("/user", data=registration_data_str, headers=self.headers)
        expected_user_id = registration_data["id"]
        expected_dict = {
            "code": 200,
            "type": "unknown",
            "message": str(expected_user_id)
        }

        Assertions.assert_status_code(response_user, 200)
        Assertions.assert_expected_dict(response_user, expected_dict)
        return self.username, self.password

    @allure.description("This test successfully perform login new user")
    def test_user_login(self):
        # LOGIN
        username, password = self.test_created_new_user()
        login_data = {
            "username": username,
            "password": password
        }
        response_login = MyRequests.get("/user/login", data=login_data)
        Assertions.assert_status_code(response_login, 200)

    @allure.description("This test successfully perform logout new user")
    def test_user_logout(self):
        # LOGOUT
        response_logout = MyRequests.get(f"/user/logout", headers=self.headers)
        Assertions.assert_status_code(response_logout, 200)

    @allure.description("This test successfully add some information for new user")
    def test_user_edit(self):
        # EDIT
        self.data_put = self.prepare_registration_data()
        data_put_str = json.dumps(self.data_put)
        response_edit = MyRequests.put(f"/user/{self.user_id}", data=data_put_str, headers=self.headers)
        Assertions.assert_status_code(response_edit, 200)

    @allure.description("This test successfully checks changed information about new user")
    def test_user_get_info(self):
        # GET
        data_put_as_dict = self.data_put
        self.username = data_put_as_dict["username"]
        response_get = MyRequests.get(f"/user/{self.username}", headers=self.headers)

        Assertions.assert_status_code(response_get, 200)
        Assertions.assert_expected_dict(response_get, data_put_as_dict)

    def test_delete_user(self):
        # Delete
        response_delete = MyRequests.post(f"/user/{self.username}", headers=self.headers)

        Assertions.assert_status_code(response_delete, 405)