import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


def test_get_user_details_not_auth():
    response = MyRequests.get("/user/2")

    Assertions.assert_json_has_keys(response, "username")
    Assertions.assert_json_has_not_key(response, "email")
    Assertions.assert_json_has_not_key(response, "firstName")
    Assertions.assert_json_has_not_key(response, "lastName")
