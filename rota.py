import requests, json

def main():
    credentials = {
        'email': 'admin@example.com',
        'password': 'adminpassword123'
    }

    headers = {
        'Content-Type': 'application/json'
    }

    r = requests.post(
        'https://marvietech.com.br/app/api/auth',
        data=json.dumps(credentials),
        headers=headers
    )

    token = r.json()['token']

    headers['Authorization'] = 'Bearer ' + token

    route1 = {
        'name': 'rota 1',
        'points': [
            {
                'point': 5,
                'action': 'b'
            },
            {
                'point': 6,
                'action': 'f'
            },
            {
                'point': 7,
                'action': 'p'
            }
        ]
    }

    route2 = {
        'name': 'rota 2',
        'points': [
            {
                'point': 19,
                'action': 'b'
            },
            {
                'point': 20,
                'action': 'f'
            },
            {
                'point': 22,
                'action': 'p'
            }
        ]
    }

    routes = [route1, route2]

    for route in routes:
        r = requests.post(
            'https://marvietech.com.br/app/api/routes',
            data=json.dumps(route),
            headers=headers
        )

        print(r.status_code)

main()
