import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

payload1 = {"method": 'GET'}

response1 = requests.get(url=url)
print(response1.text)

response2 = requests.head(url=url, data={"method": "HEAD"})
print(response2)
print(response2.text)

response3 = requests.get(url=url, params=payload1)
print(response3.text)





