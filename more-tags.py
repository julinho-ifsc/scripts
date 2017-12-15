import requests
import json

def main():
    credentials = {
        'email': 'admin@example.com',
        'password': 'adminpassword123'
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(
        'https://marvietech.com.br/app/api/auth',
        data=json.dumps(credentials),
        headers=headers
    )

    token = response.json()['token']

    tags = [
        'A5024741',
        '05092941',
        'F5A75941',
        'F53F4741',
        'A52FB541',
        '75224441',
        '556E7641',
        'C5064E41',
        'D50F4741',
        '259F4D41'
    ]

    headers['Authorization'] = 'Bearer ' + token

    for index, tag in enumerate(tags):
        message = {
            'rfid': tag.lower(),
            'name': 'tag ' + str(index + 25)
        }

        print(message['name'])

        r = requests.post(
            'https://marvietech.com.br/app/api/points',
            data=json.dumps(message),
            headers=headers
        )

        print(r.status_code)

main()
