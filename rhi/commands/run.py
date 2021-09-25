import subprocess

from .command import Command


class Run(Command):
    def __init__(self, args):
        self.num: int = args.run

    def invoke_command(self, command: str) -> None:
        r = subprocess.run(command, shell=True)

        if r.returncode != 0:
            raise Exception(f"command failed. code={r}")

    def invoke(self) -> None:
        r = self.call_get(operation=f"/get/{self.num}")
        cmd = r.json().get("result")

        self.invoke_command(cmd)
