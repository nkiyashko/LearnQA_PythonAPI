from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserDelete(BaseCase):
    # Первый - на попытку удалить пользователя по ID 2
    def test_delete_undeleteble_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")

        response2 = MyRequests.delete(f"/user/2",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        Assertions.assert_code_status(response2, 400)

        response3 = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response3, "username")

    # Второй - позитивный. Создать пользователя, авторизоваться из-под него, удалить, затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален.
    def test_delete_authorized_user(self):
        register_data = self.prepare_registration_date()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        response3 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        Assertions.assert_code_status(response3, 200)

        response4 = MyRequests.get(f"/user/{user_id}")

        assert response4.content.decode('utf-8') == 'User not found', f"User: {user_id}, was not deleted"

    # Третий - негативный, попробовать удалить пользователя, будучи авторизованными другим пользователем.
    def test_delete_another_user(self):
        register_data = self.prepare_registration_date()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        response3 = MyRequests.delete(f"/user/2",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response3, 200)

        response4 = MyRequests.get(f"/user/2")
        print(response4.content)

