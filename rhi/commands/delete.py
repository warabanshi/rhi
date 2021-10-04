import subprocess

from .command import Command


class Delete(Command):
    def __init__(self, args):
        self.numbers: int = args.numbers

    def invoke(self) -> None:
        r = self.call_delete(operation=f"/delete/{self.numbers}")

        msg = r.json().get("result")
        print(msg)
