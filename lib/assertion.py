from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_value_by_name(response: Response, name: list ):
        try:
            response_data = response.json()
            response_as_dict = response_data.values()
        except json.JSONDecodeError:
            assert False, f"Response in not in JSON format. Response text is '{response.text}'"
        for values in response_as_dict:
            if values == name:
                assert values == name, f"expected username is {name}"\
                                               f"Wrong response username: {response_data.values()}\","


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
            assert value in response_as_dict.values(), f"Response JSON doesn`t have value '{value}'\
             response have this values \n{name} {response_as_dict.values()}" \
                                                       f"{type(name)}, {type(response_as_dict.values())}"

    @staticmethod
    def assert_json_has_id(response: Response, id: int):
        try:
            response_pars = response.json()
            dict_data = json.load(response_pars)
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.content}'"
        assert id == int(dict_data["message"]), f"Response JSON doesn`t have valid id = '{id}'\"" \
                                                f"response data is {dict_data}"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

