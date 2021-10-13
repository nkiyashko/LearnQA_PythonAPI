import requests
import json

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

payload1 = {"method": "get"}
payload2 = [{"method": "get"}, {"method": "post"}, {"method": "put"}, {"method": "delete"}]

response1 = requests.Request(url=url, params=payload1)
print(response1)
response2 = requests.head(url=url, data={"method": "head"})
print(response2)
response3 = requests.get(url=url, params=payload1)
print(response3)
response4 = requests.get(url=url, params=payload1)
print(response4.text)



