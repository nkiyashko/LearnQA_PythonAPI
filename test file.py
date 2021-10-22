import requests

data = {'email': 'vinkotov@example.com',
        'password': "1234"}
response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
print(response1.json())


