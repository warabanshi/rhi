import argparse
import json
import requests
import subprocess


URL = 'http://localhost:8000/'
HEADERS = {'content-type': 'application/json'}


def call_server(payload=None):
    r = requests.post(URL, data=json.dumps(payload), headers=HEADERS)

    print(f"send payload: {payload}")
    print(f"response = {r.text}")

    return r


def run_command(command: str) -> None:
    args = command.split(' ')
    r = subprocess.run(args)

    if r.returncode != 0:
        raise Exception(f'command failed. code={r}')


def register(command: str) -> None:
    try:
        print(command)
        run_command(command)
    except FileNotFoundError as e1:
        # raise from r
        print(f'invalid command: {e1}')
        return
    except Exception as e2:
        print(f'command failed: {e2}')
        return

    payload = {'instruction': 'register', 'body': command}
    call_server(payload=payload)


def flush() -> None:
    payload = {'instruction': 'flush'}
    call_server(payload)


def get_all() -> None:
    payload = {'instruction': 'get_all'}
    r = call_server(payload)

    results = json.loads(r.text)
    for i in range(len(results)):
        print(f"{i+1}: {results[i]}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--register', help="register a command")
    parser.add_argument('-f', '--flush', help="flush registered data", action='store_true')

    args = parser.parse_args()

    if args.register:
        register(args.register)
    elif args.flush:
        flush()
    else:
        get_all()
