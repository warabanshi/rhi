import io
import sys

from .command import Command


class Add(Command):

    def __init__(self, args):
        super().__init__(args)
        self.command = None

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

    def invoke(self) -> None:
        payload = {'command': self.command}
        r = self.call_post(operation='/add/', payload=payload)

        msg = r.json().get('result')
        print(msg)
