from rhi.commands.command import Command


class Delete(Command):
    def __init__(self, args):
        self.numbers = [
            s.strip() for s in args.numbers.split(",") if s.strip().isdigit()
        ]

    def invoke(self) -> None:
        valid_numbers_csv: str = "#" + ", #".join(self.numbers)
        yn = input(f"Delete commands {valid_numbers_csv}? (y/n) >> ")

        arg_numbers = ",".join(self.numbers)
        if yn.upper() == "Y":
            r = self.call_delete(operation=f"/delete/{arg_numbers}")
            msg = r.json().get("result")
            print(msg)
        else:
            print("Delete cancelled")
