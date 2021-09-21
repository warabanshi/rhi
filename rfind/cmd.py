import argparse
import io
import json
import requests
import os
import sys

from typing import List

import config

from commands.add import Add
from commands.flush import Flush
from commands.run import Run
from commands.get_all import GetAll


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', nargs='?', const=sys.stdin, help="add a command (expects stdin)")
    parser.add_argument('-n', '--num', type=int, default=None, help="history number")
    parser.add_argument('-f', '--flush', help="flush registered data", action='store_true')
    parser.add_argument('-r', '--run', help="run a specified command")

    args = parser.parse_args()

    if args.add:
        cmd = Add(args)
    elif args.flush:
        cmd = Flush()
    elif args.run:
        cmd = Run(args)
    else:
        cmd = GetAll()

    cmd.run()


if __name__ == '__main__':
    main()
