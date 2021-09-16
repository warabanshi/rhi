import argparse
import io
import json
import requests
import os
import subprocess
import sys

from typing import List


URL = 'http://localhost:8000/'
HEADERS = {'content-type': 'application/json'}
HISTTIMEFORMAT = os.getenv('HISTTIMEFORMAT')


def call_server(payload=None):
    r = requests.post(URL, data=json.dumps(payload), headers=HEADERS)

    print(f"send payload: {payload}")
    print(f"response = {r}")
    print(f"response = {r.text}")

    return r


def run_command(command: str) -> None:
    args = command.split(' ')

    r = subprocess.run(args, capture_output=True)

    if r.returncode != 0:
        raise Exception(f'command failed. code={r}')

    print(r)


def add(command: str) -> None:
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

    payload = {'instruction': 'add', 'body': command}
    call_server(payload=payload)


def flush() -> None:
    payload = {'instruction': 'flush'}
    call_server(payload)


def run(num: int) -> None:
    payload = {'instruction': 'get', 'body': num}
    r = call_server(payload)

    run_command(r.text)


def get_all() -> None:
    payload = {'instruction': 'get_all'}
    r = call_server(payload)

    results = json.loads(r.text)
    for i in range(len(results)):
        print(f"{i+1}: {results[i]}")


def cleanup_input(inputs: io.TextIOWrapper, rownum: int=None) -> str:
    lines = [s.lstrip(' ').lstrip('0123456789').strip() for s in inputs.readlines()]

    if len(lines) == 0:
        raise Exception("There's no valid lines in input")
    
    if rownum is None:
        return lines[max(len(lines)-2, 0)]

    if 1 <= rownum <= len(lines):
        return lines[rownum-1]

    raise Exception(f'Invalid rownum is specified. rownum={rownum}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', nargs='?', const=sys.stdin, help="add a command (expects stdin)")
    parser.add_argument('-n', '--num', type=int, default=0, help="history number")
    parser.add_argument('-f', '--flush', help="flush registered data", action='store_true')
    parser.add_argument('-r', '--run', help="run a specified command")

    args = parser.parse_args()

    command = None
    if args.add:
        if sys.stdin.isatty():
            print('stdin waits input')
            sys.exit()
        else:
            command = cleanup_input(args.add, args.num)

    if command:
        add(command)
    elif args.flush:
        flush()
    elif args.run:
        run(args.run)
    else:
        get_all()
