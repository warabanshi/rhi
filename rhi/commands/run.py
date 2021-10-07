import subprocess

from rhi.commands.command import Command


class Run(Command):
    def __init__(self, args):
        self.number: int = args.number

    def invoke_command(self, command: str) -> None:
        r = subprocess.run(command, shell=True)

        if r.returncode != 0:
            raise Exception(f"command failed. code={r}")

    def invoke(self) -> None:
        r = self.call_get(operation=f"/get/{self.number}")
        cmd = r.json().get("result")

        self.invoke_command(cmd)
