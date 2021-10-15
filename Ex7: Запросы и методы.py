import requests
from json.decoder import JSONDecodeError

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

payload1 = {"method": 'GET'}

response1 = requests.get(url=url)
print("Ответ на первый вопрос")
print(response1.text)
print()

response2 = requests.head(url=url, data={"method": "HEAD"})
print("Ответ на второй вопрос")
print(response2.text)
print()

response3 = requests.get(url=url, params=payload1)
print("Ответ на третий вопрос")
print(response3.text)
print()

print("Ответ на четвертый вопрос")
method = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
for i in method:
    response4 = requests.get(url=url, params=i)
    print(f'GET запрос с параметром {i}')
    print(response4.text)
print()
for i in method:
    response4 = requests.post(url=url, params=i)
    print(f'POST запрос с параметром {i}')
    print(response4.text)
print()
for i in method:
    response4 = requests.put(url=url, params=i)
    print(f'PUT запрос с параметром {i}')
    print(response4.text)
print()
for i in method:
    response4 = requests.delete(url=url, params=i)
    print(f'DELETE запрос с параметром {i}')
    print(response4.text)

