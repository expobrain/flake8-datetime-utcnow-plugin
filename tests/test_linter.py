import ast
import textwrap
from typing import List, Tuple

import pytest

from flake8_datetime_utcnow.linter import DatetimeUtcnowLinter


@pytest.mark.parametrize(
    "code, expected",
    [
        ["datetime.utcnow()", [DatetimeUtcnowLinter.error(1, 0, "U100", "Avoid using utcnow()")]],
        [
            "now = datetime.utcnow()",
            [DatetimeUtcnowLinter.error(1, 6, "U100", "Avoid using utcnow()")],
        ],
        [
            "datetime.datetime.utcnow",
            [DatetimeUtcnowLinter.error(1, 0, "U100", "Avoid using utcnow()")],
        ],
        [
            "datetime.datetime.utcnow()",
            [DatetimeUtcnowLinter.error(1, 0, "U100", "Avoid using utcnow()")],
        ],
        [
            textwrap.dedent(
                """
                datetime.datetime.utcnow()
                datetime.datetime.utcnow()
                """
            ).strip(),
            [
                DatetimeUtcnowLinter.error(1, 0, "U100", "Avoid using utcnow()"),
                DatetimeUtcnowLinter.error(2, 0, "U100", "Avoid using utcnow()"),
            ],
        ],
    ],
)
def test_linter_positive(code: str, expected: List[Tuple]) -> None:
    tree = ast.parse(code)
    checker = DatetimeUtcnowLinter(tree)

    actual = list(checker.run())

    assert actual == expected


@pytest.mark.parametrize("code", ["random_symbol.utcnow()"])
def test_linter_negative(code: str) -> None:
    tree = ast.parse(code)
    checker = DatetimeUtcnowLinter(tree)

    assert len(list(checker.run())) == 0


@pytest.mark.parametrize("lineno", range(2))
@pytest.mark.parametrize("offset", range(2))
@pytest.mark.parametrize("code, message", [["U100", "my message"]])
def test_linter_error(lineno: int, offset: int, code: str, message: str) -> None:
    actual = DatetimeUtcnowLinter.error(lineno, offset, code, message)

    assert actual == (lineno, offset, f"{code} {message}", DatetimeUtcnowLinter)
