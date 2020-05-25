import os.path

def is_dev_environment() -> bool:
    """Returns True if the current directory has the source code structure"""
    if os.path.isdir("dist") \
            and os.path.isdir("vendor") \
            and os.path.isfile("caos.yml"):
        return True
    return False