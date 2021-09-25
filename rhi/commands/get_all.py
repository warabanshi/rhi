from .command import Command


class GetAll(Command):
    def invoke(self) -> None:
        r = self.call_get(operation="/get/")

        results = r.json().get("result")
        length = len(results)
        digits = len(str(length))

        for i in range(length):
            print(f" {i+1:{digits}}: {results[i]}")
