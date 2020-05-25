import os.path
from src.python.pygmypython.utils import environment

OPENJDK_PATH = os.path.abspath("openjdk")
if environment.is_dev_environment():
    OPENJDK_PATH = os.path.abspath("dist/pygmypython/openjdk")

JAVA = os.path.join(OPENJDK_PATH, "bin/java")
JAVAC = os.path.join(OPENJDK_PATH, "bin/javc")
JAR = os.path.join(OPENJDK_PATH, "bin/jar")
