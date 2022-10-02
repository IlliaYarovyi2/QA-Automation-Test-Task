import requests

url = "https://petstore.swagger.io/v2/store"

def create_order_for_a_pet(url):

    json_data = {
        'id': 12345,
        'petId': 54321,
        'quantity': 0,
        'shipDate': '2022-10-02T10:26:49.867Z',
        'status': 'placed',
        'complete': True,
    }

    result = requests.post('https://petstore.swagger.io/v2/store/order', json=json_data)

    print(result.status_code)
    #print(result.text)

def find_order_by_id():

    headers = {
        'accept': 'application/json',
    }

    result = requests.get('https://petstore.swagger.io/v2/store/order/12345', headers=headers)

    print(result.status_code)
    #print(result.text)

create_order_for_a_pet(url)
find_order_by_id()