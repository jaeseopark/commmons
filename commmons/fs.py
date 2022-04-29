import os
from pathlib import Path

__all__ = [
    "get_filesize_in_bytes",
    "touch_file",
    "touch_directory",
]


def get_filesize_in_bytes(path: str):
    if os.path.isdir(path):
        raise ValueError('folders are not supported')

    s = os.stat(path)
    return s.st_size


def touch_file(path: str):
    if os.path.exists(path):
        return

    os.makedirs(Path(path).parent, exist_ok=True)
    open(path, "a").close()


def touch_directory(path: str):
    if os.path.exists(path):
        return

    os.makedirs(path, exist_ok=True)
