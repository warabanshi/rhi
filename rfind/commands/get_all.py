import json

from .command import Command


class GetAll(Command):

    def run(self) -> None:
        payload = {'instruction': 'get_all'}
        r = self.call_server(payload)

        results = json.loads(r.text)
        for i in range(len(results)):
            print(f"{i+1}: {results[i]}")
