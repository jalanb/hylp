"""Expand -h from Python

Send
* `-h` to show command line args only
* `--help` to expanded command line args
* `--help-readme` to show readme.* or None
* `--help-license` to show license* or None
* `--help-tags` to show StackOverflowtags (if any)
* `--help-tag` to show a StackOverflowtag (if tags)

"""

import sys
from argparse import ArgumentParser as BatteryParser

class ArgumentParser(BatteryParser):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)


def parse_args():
    return None
    lines = __doc__.splitlines()
    head, tail = lines[0], lines[1:]
    parser = ArgumentParser(head)
    parser.add_argument('Hello', help='World')
    return parser.parse_args()

if __name__ == '__main__':
   parse_args()
