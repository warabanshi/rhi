import argparse
import json
import requests
import subprocess


URL = 'http://localhost:8000/'
HEADERS = {'content-type': 'application/json'}


def run_command(command: str) -> None:
    r = subprocess.call(command)

    if r != 0:
        raise Exception(f'command failed. code={r}')


def call_server(payload=None):
    r = requests.post(URL, data=json.dumps(payload), headers=HEADERS)

    print(f"send payload: {payload}")
    print(f"response = {r.text}")


def register(command: str) -> None:
    try:
        run_command(command)
    except FileNotFoundError as e:
        # raise from r
        print('invalid command')
        return
    except Exception as e2:
        print('command failed')
        return

    payload = {'instruction': 'register', 'body': command}
    call_server(payload=payload)


def get_all() -> None:
    payload = {'instruction': 'get_all'}
    call_server(payload)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--register', help="register a command")

    args = parser.parse_args()

    if args.register:
        register(args.register)
    else:
        get_all()
