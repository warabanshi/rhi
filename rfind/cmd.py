import argparse
import sys

from commands.add import Add
from commands.flush import Flush
from commands.run import Run
from commands.get_all import GetAll


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', nargs='?', const=sys.stdin, help='add a command')
    parser.add_argument('-m', '--memo', type=str, help='add memo for the command')
    parser.add_argument('-n', '--num', type=int, default=None, help='history number')
    parser.add_argument('-f', '--flush', help='flush registered data', action='store_true')
    parser.add_argument('-r', '--run', type=int, help='run a specified command')

    args = parser.parse_args()

    try:
        if args.add:
            cmd = Add(args)
        elif args.flush:
            cmd = Flush()
        elif args.run:
            cmd = Run(args)
        else:
            cmd = GetAll()

        cmd.run()
    except Exception as e:
        print(f'Exception occurred. message = {e}')


if __name__ == '__main__':
    main()
