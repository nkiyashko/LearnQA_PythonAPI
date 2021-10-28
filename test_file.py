import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # Register new user
        register_data = self.prepare_registration_date()
        print(register_data)
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        print(response1.text)
        # Assertions.assert_code_status(response1, 200)
        # Assertions.assert_json_has_keys(response1, id)
