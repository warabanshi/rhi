import subprocess

from .command import Command


class Run(Command):

    def __init__(self, args):
        self.num: int = args.run

    def run_command(self, command: str) -> None:
        args = command.split(' ')

        r = subprocess.run(args, capture_output=True)

        if r.returncode != 0:
            raise Exception(f'command failed. code={r}')

        print(r)

    def run(self) -> None:
        payload = {'instruction': 'get', 'body': self.num}
        r = self.call_server(payload)

        self.run_command(r.text)
