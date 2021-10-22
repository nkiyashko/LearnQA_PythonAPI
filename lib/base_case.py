from requests import Response

class BaseCase:
    def get_cookie (self,response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Не могу найти cookie с именем {cookie_name} в последнем ответе"
        return  response.cookies[cookie_name]

    def get_header (self, response: Response, header_name):
        assert  header_name in response.cookies, f"Не могу найти header с именем {header_name} в последнем ответе"
        return  response.headers[header_name]
