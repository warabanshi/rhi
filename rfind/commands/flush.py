from .command import Command


class Flush(Command):

    def run(self) -> None:
        yn = input('Flush all commands? (y/n) >> ')

        if yn.upper() == 'Y':
            payload = {'instruction': 'flush'}
            self.call_server(payload)
        else:
            print('Flush cancelled')
