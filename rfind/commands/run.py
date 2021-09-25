import subprocess

from .command import Command


class Run(Command):

    def __init__(self, args):
        self.num: int = args.run

    def invoke_command(self, command: str) -> None:
        args = command.split(' ')

        r = subprocess.run(args)

        if r.returncode != 0:
            raise Exception(f'command failed. code={r}')

    def invoke(self) -> None:
        payload = {'instruction': 'get', 'body': self.num}
        r = self.call_server(payload)

        self.invoke_command(r.text)
