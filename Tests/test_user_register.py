import requests
import self

from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import pytest


class TestUserRegister(BaseCase):
    @pytest.mark.parametrize('data', [
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
                             )
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        return self.email

    # def gen_email(self):
    #     base_part = "learnqa"
    #     domain = "example.com"
    #     random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    #     return f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        print(response.content)
        Assertions.assert_json_has_key(response, "id")

    def test_case_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

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
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)

    def test_create_user_with_short_username(self):
        data = {
            'password': '123',
            'username': 'a',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short"

    def test_create_user_with_long_username(self):
        data = {
            'password': '123',
            'username': ('a' * 251),
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long"

    def test_create_user_without_param(self):

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400
