import json
import json.decoder
from requests import Response

class BaseCase:
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Не могу найти cookie с именем {cookie_name} в последнем ответе"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, header_name):
        assert header_name in response.headers, f"Не могу найти header с именем {header_name} в последнем ответе"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON does't have key '{name}'"

        return response_as_dict[name]
