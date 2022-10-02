import requests

url = "https://petstore.swagger.io/v2/pet"


def add_new_pet(url):
    json_data = {
        'id': 0,
        'category': {
            'id': 0,
            'name': 'пес',
        },
        'name': 'doggie',
        'photoUrls': [
            'string',
        ],
        'tags': [
            {
                'id': 0,
                'name': 'string',
            },
        ],
        'status': 'available',
    }

    result = requests.post(url, json=json_data)

    print(result.status_code)
    print(result.text)


def find_pet_by_status():
    headers = {
        'accept': 'application/json',
    }

    params = {
        "id": 9223372036854249242,
        "category": {
            "id": 0,
            "name": "пес"
        },
        "name": "doggie",
        "photoUrls":
            ["string"],
        "tags": [
            {"id": 0,
             "name": "string"
             }
        ],
        "status": "available"
    }

    result = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params, headers=headers)

    print(result.status_code)
    print(result.text)


def update_pet(url):
    json_data = {
        'id': 0,
        'category': {
            'id': 0,
            'name': 'пес',
        },
        'name': 'doggie',
        'photoUrls': [
            'string',
        ],
        'tags': [
            {
                'id': 0,
                'name': 'string',
            },
        ],
        'status': 'sold',
    }

    result = requests.put(url, json=json_data)

    print(result.status_code)
    print(result.text)


add_new_pet(url)
find_pet_by_status()
update_pet(url)
