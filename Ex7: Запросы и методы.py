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

method = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
for i in method:
    response4 = requests.get(url=url, params=i)
    #print(response4.text)
    if response4 is {"success": "!"}:
        print(f'Answer is Sucses in get query with {i} params')
    response5 = requests.post(url=url, data=i)
    print(response5.text)
    if response5 == {"success": "!"}:
        print()
    response6 = requests.put(url=url, data=i)
    print(response6.text)
    if response6 == {"success": "!"}:
        print()
    response7 = requests.delete(url=url, data=i)
    print(response7.text)
    if response7 == {"success": "!"}:
        print()
