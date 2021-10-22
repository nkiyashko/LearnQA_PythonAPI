import requests

data = {"login": "super_admin", "password": "welcome"}
response2 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=data)
auth_cookies = dict(response2.cookies)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=auth_cookies)
#print(response3.text)
if response3.text == "You are authorized":
    print(f'You are authorized via Password: [ welcome ] : [ {auth_cookies} ]')
