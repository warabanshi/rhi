from .command import Command


class Flush(Command):
    def invoke(self) -> None:
        yn = input("Flush all commands? (y/n) >> ")

        if yn.upper() == "Y":
            r = self.call_post(operation="/flush/")
            msg = r.json().get("result")
            print(msg)
        else:
            print("Flush cancelled")
