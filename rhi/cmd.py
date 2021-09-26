import argparse
import sys

from rhi.commands.add import Add
from rhi.commands.flush import Flush
from rhi.commands.run import Run
from rhi.commands.get import Get
from rhi.commands.get_all import GetAll


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", nargs="?", const=sys.stdin, help="add a command")
    parser.add_argument("-m", "--msg", type=str, help="add msg for the command")
    parser.add_argument(
        "-f", "--flush", help="flush registered data", action="store_true"
    )
    parser.add_argument("-r", "--run", type=int, help="run a specified command")
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=None,
        help="history number (adopted for add or get instructions",
    )

    args = parser.parse_args()

    try:
        if args.add:
            cmd = Add(args)
        elif args.flush:
            cmd = Flush()
        elif args.run:
            cmd = Run(args)
        elif args.num:
            cmd = Get(args)
        else:
            cmd = GetAll()

        cmd.invoke()
    except Exception as e:
        print(f"Exception occurred. message = {e}")


if __name__ == "__main__":
    main()
