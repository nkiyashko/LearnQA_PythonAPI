import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

print(len(response.history)) # history возвращает кортеж из ответов сервера
print(response.url)

