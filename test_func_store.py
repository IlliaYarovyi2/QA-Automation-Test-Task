import requests
import pytest


def test_createOrderForPet():
    json_data = {
        'id': 12345,
        'petId': 54321,
        'quantity': 0,
        'shipDate': '2022-10-02T10:26:49.867Z',
        'status': 'placed',
        'complete': True,
    }

    result = requests.post('https://petstore.swagger.io/v2/store/order', json=json_data)

    assert result.status_code == 200


def test_findOrderById():
    headers = {
        'accept': 'application/json',
    }

    result = requests.get('https://petstore.swagger.io/v2/store/order/12345', headers=headers)

    assert result.status_code == 200


def test_cleanStore():
    headers = {
        'accept': 'application/json',
    }

    result = requests.delete('https://petstore.swagger.io/v2/store/order/12345', headers=headers)

    assert result.status_code == 200


if __name__ == '__main__':
    pytest.main()
