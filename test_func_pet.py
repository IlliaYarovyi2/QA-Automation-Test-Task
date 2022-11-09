import requests
import pytest


def test_add_new_pet():
    json_data = {
        'id': 77,
        'category': {
            'id': 77,
            'name': 'string',
        },
        'name': 'mars',
        'photoUrls': [
            'string',
        ],
        'tags': [
            {
                'id': 77,
                'name': 'string',
            },
        ],
        'status': 'available',
    }

    result = requests.post("https://petstore.swagger.io/v2/pet", json=json_data)

    assert result.status_code == 200


def test_find_pet_by_status():
    headers = {
        'accept': 'application/json',
    }

    params = {
        "id": 77,
        "category": {
            "id": 77,
            "name": "mars"
        },
        "name": "doggie",
        "photoUrls":
            ["string"],
        "tags": [
            {"id": 77,
             "name": "string"
             }
        ],
        "status": "available"
    }

    result = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params, headers=headers)

    assert result.status_code == 200


def test_UpdatePet():
    json_data = {
        'id': 77,
        'category': {
            'id': 77,
            'name': 'mars',
        },
        'name': 'doggie',
        'photoUrls': [
            'string',
        ],
        'tags': [
            {
                'id': 77,
                'name': 'string',
            },
        ],
        'status': 'sold',
    }

    result = requests.put("https://petstore.swagger.io/v2/pet", json=json_data)

    assert result.status_code == 200


def test_Cleaner_Pet():
    headers = {
        'accept': 'application/json',
        'api_key': '77',
    }

    result = requests.delete('https://petstore.swagger.io/v2/pet/77', headers=headers)
    assert result.status_code == 200


if __name__ == '__main__':
    pytest.main()
