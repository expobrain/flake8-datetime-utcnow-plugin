# flake8_datetime_utcnow_plugin

## Rationale

Plugin for `flake8` to warn the developer of the usage of [datetime.utcnow()](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow).

The problem with `datetme.utcnow()` is that indeed returns the current timestamp in the UTC timzone but the object is a naive `datetime`, that is doesn't have the `tzinfo` argument set.

Instead [datetime.now()](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow) should be used passing the UTC timezone:

```python
from datetime import datetime, timezone

datetime.now(timezone.utc)
```

## Installation

To install the plugin and `flake8`:

```
pip install flake8_datetime_utcnow_plugin
```
