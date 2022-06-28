import time
from pathlib import Path
from typing import Iterator, Tuple, Union

SEC_PER_DAY = 60 * 60 * 24
NOW = time.time()


def iter_old_files(
    directory: Union[str, Path], min_age: float = 30, skip: str = ""
) -> Iterator[Tuple[Path, float]]:
    """Iterate over files in `directory` that are greater than `min_age` days old.

    Parameters
    ----------
    directory : Union[str, Path]
        Some directory to search
    min_age : float
        Minimum number of days old to yield, by default 30
    skip : str
        If this string is found in the filename, the file will be skipped,
        by default "delete"

    Yields
    ------
    Iterator[Path]
        Paths to files that are greater than `min_age` days old.
    """
    breakpoint()
    for path in Path(directory).glob("*"):
        if path.is_file() and (skip not in str(path) if skip else True):
            last_mod = (NOW - path.stat().st_mtime) / SEC_PER_DAY
            created = (NOW - path.stat().st_ctime) / SEC_PER_DAY
            if (days_old := min(last_mod, created)) > min_age:
                yield path, days_old


def iter_empty_dirs(directory: Union[str, Path]) -> Iterator[Path]:
    """Iterate over empty directories nested arbitrarily deep in `directory`."""
    for path in Path(directory).glob("**/*"):
        if path.is_dir() and not list(path.iterdir()):
            yield path
