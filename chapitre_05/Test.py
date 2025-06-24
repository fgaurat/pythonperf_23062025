from typing import Any


class Test:


    def __init__(self) -> None:
        self.toto="Toto"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__")