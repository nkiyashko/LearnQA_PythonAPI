import pytest
import requests
from lib.base_case import BaseCase

class TestUserAuth(BaseCase):
    exclude_params = [("no_cookie"), ("no_token")]

    def setup(self):
        data = {'email':'vinkotov@example.com',
                'password': "1234"}
        response1 = requests.post("http://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "There is no auth cookie in response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token in the response"
        assert "user_id" in response1.json(), "There is no user id in the response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json()["user_id"]

    def test_auth_user(self):

            response2 = requests.get("http://playground.learnqa.ruapi/user/auth",
                                     headers={"x-csrf-token": self.token},
                                     cookies={"auth_sid": self.auth_sid}
                                     )

            assert "user_id" in response2.json(), "There is no user id in the second response"
            user_id_from_chek_method = response2.json()["user_id"]
            print(user_id_from_chek_method)

            assert self.user_id_from_auth_method == user_id_from_chek_method, "User id from auth method is not equal to user id from chek method"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_chek(self, condition):

        if condition == "no_cookie":
            response2 = requests.get("http://playground.learnqa.ru/api/user/auth",
                                     cookies={"auth_sid": self.auth_sid}
                                     )

            assert "user_id" in response2.json(), "There is no user id in the second response"

            user_id_from_chek_method = response2.json()["user_id"]

            assert user_id_from_chek_method == 0, f"User is authorised with condition {condition}"

