import requests
import pytest


def test_createUser():
    json_data = [
        {
            'id': 98765,
            'username': 'Bomd',
            'firstName': 'Illia',
            'lastName': 'Yarovyi',
            'email': 'bomd@gmail.com',
            'password': '12345',
            'phone': '1234567890',
            'userStatus': 8,
        },
    ]

    result = requests.post('https://petstore.swagger.io/v2/user/createWithList', json=json_data)

    assert result.status_code == 200


def test_updateUser():
    json_data = {
        'id': 98765,
        'username': 'bomb2.0',
        'firstName': 'Illia',
        'lastName': 'Yarovyi',
        'email': 'bomd@gmail.com',
        'password': '123456789',
        'phone': '1234567890',
        'userStatus': 8,
    }

    result = requests.put('https://petstore.swagger.io/v2/user/Bomd', json=json_data)

    assert result.status_code == 200


def test_cleanUser():
    headers = {
        'accept': 'application/json',
    }

    result = requests.delete('https://petstore.swagger.io/v2/user/bomb2.0', headers=headers)

    assert result.status_code == 200


if __name__ == '__main__':
    pytest.main()
