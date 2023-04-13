from lib.assertion import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import lib.logger
import json


class TestUserPetStore(BaseCase):
    def test_user_registration(self):
        """New user registration"""

        # We are preparing the data for using
        registration_data = json.dumps(self.prepare_registration_data())
        registration_data_dict = json.loads(registration_data)
        headers = {
            "content-type": "application/json"
        }

        # We are preparing the data for asserting
        expected_id = str(registration_data_dict["id"])
        expected_keys = ["code", "type", "message"]
        expected_values = [200, "unknown", expected_id]

        # Send 'POST' request on '/user' end point
        response = MyRequests.post("/user", data=registration_data, headers=headers)

        # We check the received data
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, expected_keys)
        Assertions.assert_json_has_values(response, expected_values)
