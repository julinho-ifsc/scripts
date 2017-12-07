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

    tags = [
        'BC521A14',
        'D2F7E4D4',
        '827277D4',
        None,
        '8275D4D4',
        '727C77D4',
        'C29D77D4',
        '82AD77D4',
        '126174D4',
        'C2FBD4D4',
        'B26777D4',
        'BC6A9A03',
        '22F235D5',
        '527867D4',
        'C2F9C8D4',
        '1CAF5C0D',
        '9C835C0D',
        'FC0F600D',
        'D2CE77D4',
        'F2EFF2D4'
    ]

    headers['Authorization'] = 'Bearer ' + token

    for index, tag in enumerate(tags):
        if tag == None:
            continue

        message = {
            'rfid': tag.lower(),
            'name': 'tag ' + str(index + 1)
        }

        print(message['name'])

        r = requests.post(
            'https://marvietech.com.br/app/api/points',
            data=json.dumps(message),
            headers=headers
        )

        print(r.status_code)

main()
