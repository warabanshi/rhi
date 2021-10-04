from typing import Dict, List

from .command import Command


class Get(Command):
    def __init__(self, args):
        self.num: int = args.num if args.num else 0

    def invoke(self) -> None:
        output: List[str] = []

        if self.num > 0:
            output = self.get_single()
        else:
            output = self.get_all()

        print("\n".join(output))

    def parse_line(self, one_command: Dict[str, str]) -> str:
        if one_command["message"]:
            return f'{one_command["command"]}   # {one_command["message"]}'
        else:
            return f'{one_command["command"]}'

    def get_single(self) -> List[str]:
        r = self.call_get(operation=f"/get/{self.num}")

        result = r.json().get("result")
        return [self.parse_line(result)]

    def get_all(self) -> List[str]:
        r = self.call_get(operation="/get/")

        results = r.json().get("result")
        length = len(results)
        digits = len(str(length))

        output: List[str] = []
        for i in range(length):
            r = self.parse_line(results[i])
            output.append(f" {i+1:{digits}}: {r}")

        return output
