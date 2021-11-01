import argparse
import io
import re
import sys

from typing import List

from rhi.commands.command import Command


class Add(Command):
    def __init__(self, args: argparse.Namespace):
        super().__init__(args)
        self.command = None
        self.message = args.message
        self.tags = self.cleanup_tags(args.tags)

        if args.commands:
            if sys.stdin.isatty():
                raise Exception("stdin waits input")
            else:
                self.command = self.cleanup_commands(args.commands, args.num)

    def is_history(self, line):
        return True if re.match(r"^ +[0-9]+ +history", line) else False

    def cleanup_commands(self, inputs: io.TextIOWrapper, rownum: int = None) -> str:
        lines = [line.rstrip("\n") for line in inputs.readlines()]

        if len(lines) == 0:
            raise Exception("There's no valid lines in input")

        if not self.is_history(lines[-1]):
            return "\n".join(
                lines
            )  # return whole input when it's not a result of history

        def split_line(line: str) -> List[str]:
            s = line.strip()
            return [s[: s.find(" ")].strip("* "), s[s.find(" ") + 1 :].strip()]

        history_lines = [
            split_line(line) for line in lines if not self.is_history(line)
        ]
        histories = {num: command for (num, command) in history_lines}

        if rownum is None:
            return history_lines[-1][
                1
            ]  # get a last line except "history" command itself

        max_num = max([int(key) for key in histories.keys()])
        if 1 <= rownum <= max_num:
            return histories[str(rownum)]  # get a specified line

        raise Exception(f"Invalid rownum is specified. rownum={rownum}")

    def cleanup_tags(self, tags: str) -> List[str]:
        try:
            return tags.strip(" ,").split(",")
        except Exception:
            return []

    def invoke(self) -> None:
        payload = {"command": self.command, "message": self.message, "tags": self.tags}
        r = self.call_post(operation="/add", payload=payload)

        msg = r.json().get("result")
        print(msg)
