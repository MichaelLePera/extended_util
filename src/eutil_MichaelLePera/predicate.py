from typing import Iterable, Callable, TypeVar, Any

T = TypeVar('T')


class Predicate:

    @staticmethod
    def match_variable(attr_name: str, value: Any) -> Callable[[T], bool]:
        def predicate(obj: T) -> bool:
            if hasattr(obj, attr_name):
                raise ValueError()
            return getattr(obj, attr_name) == value
        return predicate
