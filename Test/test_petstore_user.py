from lib.assertion import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import lib.logger
import json


class TestUserPetStore(BaseCase):
    def test_user_registration(self):
        registration_data = json.dumps(self.prepare_registration_data())
        headers = {
            "content-type": "application/json"
        }
        expected_keys = ["code", "type", "message"]
        expected_values = [200, "unknown"]
        response = MyRequests.post("/user", data=registration_data, headers=headers)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, expected_keys)
