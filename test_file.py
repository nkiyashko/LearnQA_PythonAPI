import pytest
import requests

@pytest.mark.parametrize('data', [
    ({'password': '', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa',
      'email': "123456@example.com"}),
    ({'password': '123', 'username': '', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': "123456@example.com"}),
    ({'password': '123', 'username': 'learnqa', 'firstName': '', 'lastName': 'learnqa', 'email': "123456@example.com"}),
    ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': '', 'email': "123456@example.com"}),
    ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': ""})
]
                         )
def test_create_user_without_param(data):

    response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

    assert response.status_code == 400





