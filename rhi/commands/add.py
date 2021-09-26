import argparse
import io
import sys

from typing import List

from rhi.commands.command import Command


class Add(Command):
    def __init__(self, args: argparse.Namespace):
        super().__init__(args)
        self.command = None

        if args.add:
            if sys.stdin.isatty():
                raise Exception("stdin waits input")
            else:
                self.command = self.cleanup_input(args.add, args.num)

    def cleanup_input(self, inputs: io.TextIOWrapper, rownum: int = None) -> str:
        def split_line(line: str) -> List[str]:
            s = line.lstrip()
            return [s[: s.find(" ")], s[s.find(" ") + 1 :].strip()]

        lines = [split_line(line) for line in inputs.readlines()]
        histories = {num: command for (num, command) in lines}
        max_num = max([int(key) for key in histories.keys()])

        if len(histories) == 0:
            raise Exception("There's no valid lines in input")

        if rownum is None:
            return lines[max(len(lines) - 2, 0)][
                1
            ]  # get a last line except "history" command itself

        if 1 <= rownum <= max_num:
            return histories[str(rownum)]  # get a specified line

        raise Exception(f"Invalid rownum is specified. rownum={rownum}")

    def invoke(self) -> None:
        payload = {"command": self.command}
        r = self.call_post(operation="/add/", payload=payload)

        msg = r.json().get("result")
        print(msg)
