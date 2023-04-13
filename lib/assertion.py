from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response in not in JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn`t have key '{name}' "
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name: list):
        try:
            response_as_dict = response.json()
            response_keys_list = response_as_dict.keys()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for key in name:
            assert key in response_keys_list, f"Response JSON doesn`t have key '{key}'"

    @staticmethod
    def assert_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
            response_keys_list = response_as_dict.get()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for name in names:
            assert name in response_keys_list, f"Response JSON doesn`t have key '{name}'"

    @staticmethod
    def assert_json_has_values(response: Response, name: list):
        try:
            response_as_dict = response.json()

        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for value in name:
            assert value in response_as_dict.values(), f"Response JSON doesn`t have key '{value}'"

    @staticmethod
    def assert_json_has_id(response: Response, id: int):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.content}'"
        assert 19 == len(response_as_dict[id]), f"Response JSON doesn`t have valid id '{id}'"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

