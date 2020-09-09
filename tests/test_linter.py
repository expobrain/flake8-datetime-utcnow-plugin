import ast

import pytest

from flake8_datetime_utcnow.linter import DatetimeUtcnowPlugin


@pytest.mark.parametrize(
    "code",
    [
        "now = datetime.utcnow()",
        "datetime.utcnow()",
        "datetime.datetime.utcnow()",
    ],
)
def test_linter_positive(code: str):
    tree = ast.parse(code)
    checker = DatetimeUtcnowPlugin(tree)

    for lineno, col_offset, msg, instance in checker.run():
        assert msg.startswith("U100 Avoid using utcnow()")


@pytest.mark.parametrize("code", ["random_symbol.utcnow()"])
def test_linter_negative(code: str):
    tree = ast.parse(code)
    checker = DatetimeUtcnowPlugin(tree)

    assert len(list(checker.run())) == 0
