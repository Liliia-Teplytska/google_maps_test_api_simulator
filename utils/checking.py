import json
from requests import Response


class Checking():

    """Method for checking the status codes"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Successfully! Status code = " + str(response.status_code))
        else:
            print("Fail! Status code = " + str(response.status_code))

    """Method for verifying that all required fields in the response are present"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All required fields are present!")

    """Method for validating the correctness of the required field"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("The required field '" + field_name + "' is correct!")

    """Method for checking if the word "failed" is present in the required field 'msg'"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("The word in the required field 'msg' - '" + search_word + "' is present!")
        else:
            print("The word in the required field 'msg' - '" + search_word + "' is absent")
