import subprocess
from typing import List
from typing import NewType
from src.python.pygmypython import __version__
from src.python.pygmypython.paths import JAVA

ReturnCode = NewType("ReturnCode", int)


def main(argv: List[str]) -> ReturnCode:
    print("Pygmy Python v{}".format(__version__))
    print("Argv: {}".format(argv))
    print(subprocess.check_output([JAVA, "-version"], universal_newlines=True))
    return ReturnCode(0)