from typing import List
import ast


class UtcnowVisitor(ast.NodeVisitor):
    def __init__(self):
        self.utcnows: List[ast.Attribute] = []

    def _is_datetime_utcnow(self, node: ast.Attribute) -> bool:
        return (
            isinstance(node.value, ast.Name)
            and node.value.id == "datetime"
            and node.attr == "utcnow"
        )

    def _is_datetime_datetime_utcnow(self, node: ast.Attribute) -> bool:
        return (
            isinstance(node.value, ast.Attribute)
            and isinstance(node.value.value, ast.Name)
            and node.value.value.id == "datetime"
            and node.attr == "utcnow"
        )

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if self._is_datetime_datetime_utcnow(node) or self._is_datetime_utcnow(node):
            self.utcnows.append(node)
