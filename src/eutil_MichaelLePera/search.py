from typing import Iterable, Callable, TypeVar

T = TypeVar('T')


def linear_search(iterable: Iterable[T], predicate: Callable[[T], bool]) -> T:
    for x in iterable:
        if predicate(x):
            return x
    return None

