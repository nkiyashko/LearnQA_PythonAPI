from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # Register new user
        register_data = self.prepare_registration_date()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Edit
        new_name = "Changed name"

        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name}
                                   )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        Assertions.assert_json_value_by_name(
            response4,
            'firstName',
            new_name,
            "Wrong name of the user after edit"
        )

# - Попытаемся изменить данные пользователя, будучи неавторизованными
    def test_edit_non_authorized_user(self):
        new_name = "Changed name"

        response3 = MyRequests.put(f"/user/2",
                                   headers={"x-csrf-token": ""},
                                   cookies={"auth_sid": "auth_sid"},
                                   data={"firstName": new_name}
                                   )

        Assertions.assert_code_status(response3, 400)

# - Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
    def test_edit_user_via_authorized_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response, "user_id")

        new_name = "Changed name"

        response2 = MyRequests.put(f"/user/{user_id_from_auth_method}1",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name}
                                   )

        Assertions.assert_code_status(response2, 400)

# - Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
    def test_edit_users_email_without_add_simbol(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response, "user_id")

        new_name = "Changed name"
        new_email = "vinkotovexample.com"
        response2 = MyRequests.put(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name,
                                         "email": new_email}
                                   )

        Assertions.assert_code_status(response2, 400)

# - Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое
# значение в один символ
    def test_edit_users_firstname_to_short(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response, "user_id")

        new_name = "C"

        response2 = MyRequests.put(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name}
                                   )

        Assertions.assert_code_status(response2, 400)


