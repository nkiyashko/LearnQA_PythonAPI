import requests

class TestHeader:
    def test_header_api(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        header = response.json()
        print(header)
        assert header == {'success': '!'}

