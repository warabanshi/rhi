import json

from .command import Command


class GetAll(Command):

    def run(self) -> None:
        payload = {'instruction': 'get_all'}
        r = self.call_server(payload)

        results = json.loads(r.text)
        length = len(results)
        digits = len(str(length))

        for i in range(length):
            print(f" {i+1:{digits}}: {results[i]}")
