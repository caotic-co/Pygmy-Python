import subprocess
from shutil import which
from typing import List
from typing import NewType
from src.python.pygmypython import __version__

ReturnCode = NewType("ReturnCode", int)


def main(argv: List[str]) -> ReturnCode:
    if not which("java"):
        print("'java' is not available in the system path")
        return ReturnCode(1)

    if not which("javac"):
        print("'javac' is not available in the system path")
        return ReturnCode(1)

    print("Pygmy Python v{}".format(__version__))
    print("Argv: {}".format(argv))
    print(subprocess.check_output(["java", "-version"], universal_newlines=True))
    return ReturnCode(0)