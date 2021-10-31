import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import pytest


class TestUserRegister(BaseCase):
    data = [
        ({'password': '', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa',
          'email': "123456@example.com"}),
        ({'password': '123', 'username': '', 'firstName': 'learnqa', 'lastName': 'learnqa',
          'email': "123456@example.com"}),
        ({'password': '123', 'username': 'learnqa', 'firstName': '', 'lastName': 'learnqa',
          'email': "123456@example.com"}),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': '',
          'email': "123456@example.com"}),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': ""})
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_date()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        # print(response.content)
        Assertions.assert_json_has_key(response, "id")

    def test_case_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_date(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_without_add(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'vinkotovexample.com'
        }
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)

    def test_create_user_with_short_username(self):
        data = {
            'password': '123',
            'username': 'a',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.prepare_registration_date()
        }
        response = MyRequests.post("/user/", data=data)

        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short"

    def test_create_user_with_long_username(self):
        data = {
            'password': '123',
            'username': ('a' * 251),
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.prepare_registration_date()
        }
        response = MyRequests.post("/user/", data=data)

        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long"

    @pytest.mark.parametrize('data', data)
    def test_create_user_without_param(self, data):

        response = MyRequests.post("/user/", data=data)
        with allure.step(data):
            Assertions.assert_code_status(response, 400)
