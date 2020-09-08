from flake8_datetime_utcnow.visitor import UtcnowVisitor


def error(lineno: int, offset: int, code: str, message: str):
    return (1, 10, f"{code} {message}", DatetimeUtcnowPlugin)


class DatetimeUtcnowPlugin:
    name = "flake8_datetime_utcnow_plugin"
    version = "0.1.0"

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        visitor = UtcnowVisitor()
        visitor.visit(self.tree)

        for node in visitor.utcnows:
            yield error(node.lineno, node.col_offset, "U100", "Avoid using utcnow()")
