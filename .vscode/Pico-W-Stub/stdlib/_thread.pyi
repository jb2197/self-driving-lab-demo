import sys
from collections.abc import Callable
from threading import Thread
from types import TracebackType
from typing import Any, NoReturn, Optional

error = RuntimeError

class LockType:
    def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...
    def __enter__(self) -> bool: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...

def start_new_thread(
    function: Callable[..., ...], args: tuple[..., ...], kwargs: dict[str, Any] = ...
) -> int: ...
def allocate_lock() -> LockType: ...
def exit() -> NoReturn: ...
def get_ident() -> int: ...
def stack_size(size: int = ...) -> int: ...

TIMEOUT_MAX: float

if sys.version_info >= (3, 8):
    class _ExceptHookArgs(
        tuple[
            type[BaseException],
            Optional[BaseException],
            Optional[TracebackType],
            Optional[Thread],
        ]
    ):
        @property
        def exc_type(self) -> type[BaseException]: ...
        @property
        def exc_value(self) -> BaseException | None: ...
        @property
        def exc_traceback(self) -> TracebackType | None: ...
        @property
        def thread(self) -> Thread | None: ...

    _excepthook: Callable[[_ExceptHookArgs], Any]
