from .command import Command


class Delete(Command):

    def __init__(self, args):
        num_csv: str = args.num
        self.numbers = [s.strip() for s in num_csv.split(',') if s.strip().isdigit()]

    def invoke(self) -> None:
        valid_numbers_csv: str = "#" + ", #".join(self.numbers)
        yn = input(f"Delete commands {valid_numbers_csv}? (y/n) >> ")

        if yn.upper() == "Y":
            r = self.call_delete(operation="/delete/")
            msg = r.json().get("result")
            print(msg)
        else:
            print("Delete cancelled")
