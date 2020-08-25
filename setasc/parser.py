import ast
import json

from .constants import SETUP_KEYWORD_ARGUMENTS
from .unparser import UNPARSERS
from .utils import get_class_name, sort_dict_based_on_list


class SetupVisitor(ast.NodeVisitor):
    def __init__(self):
        self.arguments = []

    def visit_Call(self, node):
        if hasattr(node.func, "id") and node.func.id == "setup":
            self.arguments.append(
                sort_dict_based_on_list(
                    {
                        kw.arg: UNPARSERS[get_class_name(kw.value)](kw.value)
                        for kw in node.keywords
                    },
                    SETUP_KEYWORD_ARGUMENTS,
                )
            )
        self.generic_visit(node)

    def report(self):
        print(json.dumps(self.arguments, indent=4))
