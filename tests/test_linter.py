from typing import List, Tuple
import ast

import pytest

from flake8_datetime_utcnow.linter import DatetimeUtcnowLinter


@pytest.mark.parametrize(
    "code, expected",
    [
        ["datetime.utcnow()", [DatetimeUtcnowLinter.error(1, 1, "U100", "Avoid using utcnow()")]],
        [
            "now = datetime.utcnow()",
            [DatetimeUtcnowLinter.error(1, 7, "U100", "Avoid using utcnow()")],
        ],
        [
            "datetime.datetime.utcnow()",
            [DatetimeUtcnowLinter.error(1, 9, "U100", "Avoid using utcnow()")],
        ],
    ],
)
def test_linter_positive(code: str, expected: List[Tuple]):
    tree = ast.parse(code)
    checker = DatetimeUtcnowLinter(tree)

    actual = list(checker.run())

    assert actual == expected


@pytest.mark.parametrize("code", ["random_symbol.utcnow()"])
def test_linter_negative(code: str):
    tree = ast.parse(code)
    checker = DatetimeUtcnowLinter(tree)

    assert len(list(checker.run())) == 0
