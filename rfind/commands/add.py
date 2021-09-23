import io
import subprocess
import sys

from .command import Command


class Add(Command):

    def __init__(self, args):
        super().__init__(args)
        self. command = None

        if args.add:
            if sys.stdin.isatty():
                raise Exception('stdin waits input')
            else:
                self.command = self.cleanup_input(args.add, args.num)

    def cleanup_input(self, inputs: io.TextIOWrapper, rownum: int = None) -> str:
        lines = [s.lstrip(' ').lstrip('0123456789').strip() for s in inputs.readlines()]

        if len(lines) == 0:
            raise Exception("There's no valid lines in input")

        if rownum is None:
            return lines[max(len(lines)-2, 0)]  # get a last line except "history" command itself

        if 1 <= rownum <= len(lines):
            return lines[rownum-1]  # get a specified line

        raise Exception(f"Invalid rownum is specified. rownum={rownum}")

    def run_command(self, command: str) -> None:
        args = command.split(' ')

        r = subprocess.run(args, capture_output=True)

        if r.returncode != 0:
            raise Exception(f'command failed. code={r}')

        print(r)

    def run(self) -> None:
        try:
            print(self.command)
            # self.run_command(self.command)
        except FileNotFoundError as e1:
            # raise from r
            print(f'invalid command: {e1}')
            return
        except Exception as e2:
            print(f'command failed: {e2}')
            return

        payload = {'instruction': 'add', 'body': self.command}
        self.call_server(payload=payload)
