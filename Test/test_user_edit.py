from lib.base_case import BaseCase
from lib.assertion import Assertions
from lib.my_requests import MyRequests

class TestUserEdit(BaseCase):

    def test_edit_just_created_user(self):
        # REGISTER
        registration_data = self.prepare_registration_data()
        response_user = MyRequests.post("user/", data=registration_data)

        Assertions.assert_status_code(response_user, 200)
        Assertions.assert_json_has_key(response_user, "id")

        email = registration_data["email"]
        first_name = registration_data["firstName"]
        password = registration_data["password"]
        user_id = registration_data["id"]

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response_login = MyRequests.post("user/login", login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_headers(response_login, "x-csrf-token")

        # EDIT
        change_first_name = "user_name_test"

        response_edit = MyRequests.put(
            f"user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": change_first_name}
        )
        Assertions.assert_status_code(response_edit, 200)

        # GET
        response_get = MyRequests.get(
            "user/SmokiMokiMo",
            headers= {"x-csrf-token": token},
            cookies= {"auth_sid": auth_sid},
        )

        Assertions.assert_value_by_name(
            response_get,
            "firstName",
            change_first_name,
            "Wrong name of the user first edit"
        )









