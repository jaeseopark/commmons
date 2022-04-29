import os
from pathlib import Path

__all__ = [
    "get_filesize_in_bytes",
    "touch_file",
    "touch_directory",
    "walk"
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


def walk(path: str, include_dirs=True, include_files=True, force_absolute_path=False):
    if not os.path.isdir(path):
        raise ValueError("path should be a directory")

    if force_absolute_path:
        path = os.path.abspath(path)

    paths = []
    for root, dirs, files in os.walk(path):
        if include_dirs:
            for dir in dirs:
                paths.append(os.path.join(root, dir))
        if include_files:
            for file in files:
                paths.append(os.path.join(root, file))
