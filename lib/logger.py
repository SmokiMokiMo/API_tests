import datetime
import os
from requests import Response

class Logger:
    file_name = f"logs/log." + str(datetime.datetime.now()) + ".log"

    @classmethod
    def _write_jog_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='UTF-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {testname}"
        data_to_add += f"Time {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request headers: {url}\n"
        data_to_add += f"Request cookies: {url}\n"
        data_to_add += f"\n"

        cls._write_jog_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f"Response code: {response.status_code}"
        data_to_add += f"Response text {response.text}"
        data_to_add += f"Response cookies {cookies_as_dict}"
        data_to_add += f"Response headers {headers_as_dict}"
        data_to_add += f"\n-----\n"

        cls._write_jog_to_file(data_to_add)
