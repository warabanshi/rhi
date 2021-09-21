from .command import Command

class Flush(Command):

    def run(self) -> None:
        payload = {'instruction': 'flush'}
        self.call_server(payload)
