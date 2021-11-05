from __future__ import annotations

import ast
from typing import Iterable, Tuple, Type

from flake8_datetime_utcnow.__version__ import __version__
from flake8_datetime_utcnow.visitor import UtcnowVisitor

LintErrorResult = Tuple[int, int, str, Type["DatetimeUtcnowLinter"]]


class DatetimeUtcnowLinter:
    name = "flake8_datetime_utcnow_plugin"
    version = __version__

    def __init__(self, tree: ast.Module) -> None:
        self.tree = tree

    @classmethod
    def error(cls, lineno: int, offset: int, code: str, message: str) -> LintErrorResult:
        return (lineno, offset, f"{code} {message}", cls)

    def run(self) -> Iterable[LintErrorResult]:
        visitor = UtcnowVisitor()
        visitor.visit(self.tree)

        for node in visitor.utcnows:
            yield self.error(node.lineno, node.col_offset, "U100", "Avoid using utcnow()")
