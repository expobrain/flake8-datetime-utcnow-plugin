import ast


class UtcnowVisitor(ast.NodeVisitor):
    def __init__(self):
        self.utcnows: List[ast.Attribute] = []

    def visit_Attribute(self, node: ast.Attribute):
        if (
            isinstance(node.value, ast.Name)
            and node.value.id == "datetime"
            and node.attr == "utcnow"
        ):
            self.utcnows.append(node)
