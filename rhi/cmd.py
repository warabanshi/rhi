import argparse
import sys

from rhi.commands.add import Add
from rhi.commands.delete import Delete
from rhi.commands.flush import Flush
from rhi.commands.init import Init
from rhi.commands.run import Run
from rhi.commands.get import Get


def add_command(subparsers: argparse._SubParsersAction) -> None:
    add = subparsers.add_parser("add", aliases=["a"], help="add a command from stdin")
    add.add_argument(
        "commands", nargs="?", default=sys.stdin, help="give commands via PIPE"
    )
    add.add_argument("--num", "-n", type=int, default=None, help="history number")
    add.add_argument("--message", "-m", type=str, default="", help="comment")
    add.set_defaults(command=Add)


def flush_command(subparsers: argparse._SubParsersAction) -> None:
    flush = subparsers.add_parser("flush", aliases=["f"], help="flush all commands")
    flush.set_defaults(command=Flush)


def delete_command(subparsers: argparse._SubParsersAction) -> None:
    delete = subparsers.add_parser(
        "delete", aliases=["d"], help="delete specified commands"
    )
    delete.add_argument(
        "numbers", type=str, help="desired history numbers for deleting (CSV allowed)"
    )
    delete.set_defaults(command=Delete)


def run_command(subparsers: argparse._SubParsersAction) -> None:
    print(subparsers)
    run = subparsers.add_parser("run", aliases=["r"], help="run a specifiec command")
    run.add_argument(
        "number", type=int, default=None, help="desired history number for running"
    )
    run.set_defaults(command=Run)


def init_command(subparsers: argparse._SubParsersAction) -> None:
    init = subparsers.add_parser("init", help="init rhi command configuration")
    init.set_defaults(command=Init)


def get_command(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=None,
        help="get a specified command",
    )


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    add_command(subparsers)
    flush_command(subparsers)
    delete_command(subparsers)
    run_command(subparsers)
    init_command(subparsers)
    get_command(parser)

    args: argparse.Namespace = parser.parse_args()

    try:
        if "command" in args:
            cmd = args.command(args)
        else:
            cmd = Get(args)

        cmd.invoke()
    except Exception as e:
        print(f"Exception occurred. message = {e}")


if __name__ == "__main__":
    main()
