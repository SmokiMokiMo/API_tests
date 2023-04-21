import json
import allure
from lib.base_case import BaseCase
from lib.assertion import Assertions
from lib.my_requests import MyRequests


@allure.epic("Performs main API points Register/Login/Login/Edit/GetUser. ")
class TestUserEdit(BaseCase):
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    data_put = None

    @allure.description("This test successfully register new user")
    def test_created_new_user(self):
        # REGISTER
        generate_new_user = self.prepare_registration_data()
        registration_data_str = json.dumps(generate_new_user)

        response_user = MyRequests.post("/user", data=registration_data_str, headers=self.headers)
        expected_user_id = generate_new_user["id"]
        expected_dict = {
            "code": 200,
            "type": "unknown",
            "message": str(expected_user_id)
        }

        Assertions.assert_status_code(response_user, 200)
        Assertions.assert_expected_dict(response_user, expected_dict)

        # Store username and password as class attributes
        self.__class__.username = generate_new_user["username"]
        self.__class__.password = generate_new_user["password"]
        self.__class__.user_id = generate_new_user["id"]

        return self.__class__.username, self.__class__.password, self.__class__.user_id

    @allure.description("This test successfully perform login new user")
    def test_user_login(self):
        # LOGIN
        login_data = {
            "username": self.__class__.username,
            "password": self.__class__.password
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
        response_edit = MyRequests.put(f"/user/{self.username}", data=data_put_str, headers=self.headers)
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