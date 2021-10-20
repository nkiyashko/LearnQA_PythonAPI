import requests


response = requests.get("https://playground.learnqa.ru/api/homework_header")
print(response.headers)
header = response.json()
print(header)
