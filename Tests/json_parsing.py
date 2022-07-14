import requests

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "user"})
parsed_response_text = response.json()
print(parsed_response_text["answer"])


