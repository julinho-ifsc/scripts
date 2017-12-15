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

    headers['Authorization'] = 'Bearer ' + token

    route = {
        'name': 'rota 3',
        'points': [
            {
                'point': 24,
                'action': 'b'
            },
            {
                'point': 25,
                'action': 'f'
            },
            {
                'point': 26,
                'action': 'p'
            }
        ]
    }

    r = requests.post(
        'https://marvietech.com.br/app/api/routes',
        data=json.dumps(route),
        headers=headers
    )

    print(r.status_code)

main()
