from .command import Command


class Get(Command):
    def __init__(self, args):
        self.num: int = args.num if args.num else 0

    def invoke(self) -> None:
        if self.num > 0:
            self.get_single()
        else:
            self.get_all()

    def get_single(self) -> None:
        r = self.call_get(operation=f"/get/{self.num}")

        result = r.json().get("result")
        print(result)

    def get_all(self) -> None:
        r = self.call_get(operation="/get/")

        results = r.json().get("result")
        length = len(results)
        digits = len(str(length))

        for i in range(length):
            print(f" {i+1:{digits}}: {results[i]}")
