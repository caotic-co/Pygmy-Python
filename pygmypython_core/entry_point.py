from pygmypython_core import __version__
from typing import List


def main(argv: List[str]):
    print("Pygmy Python v{}".format(__version__))
    print("Argv: {}".format(argv))