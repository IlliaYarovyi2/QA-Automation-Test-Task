import requests

def post():
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

    response = requests.post('https://petstore.swagger.io/v2/user/createWithList', json=json_data)

    print(response.status_code)
    print(response.text)

def put():
    json_data = {
        'id': 3,
        'username': 'dynamite',
        'firstName': 'Artem',
        'lastName': 'Petrov',
        'email': 'dynamite@gmail.com',
        'password': 'dynamite322',
        'phone': '0987654321',
        'userStatus': 15,
    }

    response = requests.put("https://petstore.swagger.io/v2/user/bomd", json=json_data)

    print(response.status_code)
    print(response.text)

post()
put()
