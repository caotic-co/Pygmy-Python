# Pygmy Python
An **x86_64 Linux Compiler** for a **new** reduced typed version of Python that generates bytecode that runs on a JVM.

## Installation
Go to the [Releases](https://github.com/caotic-co/Pygmy-Python/releases) available in the repo,
download the latest zip available **pygmypython-vX.X.X.zip** extract the content
anywhere on your machine.

**Tip:** You can add the extracted folder to your system's path and use it directly from the Terminal.

## Pygmy Python Language Specification
**Pygmy Python is not Python** and it is not compatible with everything that Python can do, as so the syntax
required although similar can differ from what you are used to. For specific details on the language specification
visit [Pygmy Python Language Specification](https://github.com/caotic-co/Pygmy-Python/tree/master/docs/pygmypython_spec).

## Compile Example
```
$ pygmypython hello_world.py
```

## Run Compiled Code
To run the compiled code you can use any compatible JVM

```
$ java hello_world
```

## Development
For information about how to set up a local environment using the source code of the project
visit [Development Documentation](https://github.com/caotic-co/Pygmy-Python/tree/master/docs/development).