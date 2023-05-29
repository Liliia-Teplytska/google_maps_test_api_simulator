import allure
import requests
from utils.logger import Logger

"""List of HTTP methods"""

class HttpMethod:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    """The GET method"""
    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            Logger.add_response(result)
            return result

    """The POST method"""
    @staticmethod
    def post(url, body):
       with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            Logger.add_response(result)
            return result

    """The PUT method"""
    @staticmethod
    def put(url, body):
       with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            Logger.add_response(result)
            return result

    """The DELETE method"""
    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            Logger.add_response(result)
            return result