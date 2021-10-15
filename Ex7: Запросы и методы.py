import requests
from json.decoder import JSONDecodeError

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

payload1 = {"method": 'GET'}

response1 = requests.get(url=url)
#print(response1.text)

response2 = requests.head(url=url, data={"method": "HEAD"})
#print(response2)
#print(response2.text)

response3 = requests.get(url=url, params=payload1)
#print(response3.text)

method = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
for i in method:
    response4 = requests.get(url=url, params=i)
    #print(response4.text)
    a = response4.json()
    print(a)
    b = a['success'][0]
    if b == "!":
        print(f'Answer is Succeed in get query with {i} params')
    elif:
        a = response4.raise_for_status(JSONDecodeError)

