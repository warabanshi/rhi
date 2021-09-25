from .command import Command


class Get(Command):

    def __init__(self, args):
        self.num: int = args.num

    def invoke(self) -> None:
        r = self.call_get(operation=f'/get/{self.num}')

        result = r.json().get('result')
        print(result)
