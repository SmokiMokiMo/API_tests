from lib.assertion import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import lib.logger
import json


class TestUserPetStore(BaseCase):
    def test_user_registration(self):
        """New user registration"""
        # We are preparing the data for using
        registration_data = self.prepare_registration_data()
        registration_data_dict = json.dumps(registration_data)

        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        # We are preparing the data for asserting
        expected_username = registration_data["username"]
        user_id = registration_data["id"]
        expected_keys = ["code", "type", "message"]
        expected_values = [200, "unknown", str(user_id)]
        expected_dict = {
            "code": 200,
            "type": "unknown",
            "message": str(user_id)
        }

        # Send 'POST' request on '/user' end point
        response = MyRequests.post("/user", data=registration_data_dict, headers=headers)

        # We check the received data
        Assertions.assert_status_code(response, 200)
        Assertions.assert_expected_dict(response, expected_dict)
        Assertions.assert_json_has_key(response, expected_keys)
        Assertions.assert_json_has_values(response, expected_values)

        """Get user by user name"""
        #Send 'POST' request on '/user/{username}' end point
        response = MyRequests.get(f"/user/{expected_username}")

        # We check the received data
        Assertions.assert_status_code(response, 200)
        Assertions.assert_value_by_name(response, expected_username)

        """Put update user"""
        # Updated user data
        registration_data = json.dumps(self.prepare_registration_data())
        update_reg_data_dict = json.loads(registration_data)


        # Send 'PUT' request on '/user/{username}' end point
        response = MyRequests.put(f"/user/{expected_username}", data=update_reg_data_dict, headers=headers)

        # We check the received data
        Assertions.assert_status_code(response, 200)
        #Assertions.assert_value_by_name(response, expected_username)





