import requests

class TestCookie:
    def test_cookie_api(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        # print(response.cookies.get_dict())
        cookie = response.cookies.get_dict()
        print(cookie)
        assert cookie == {'HomeWork': 'hw_value'}
