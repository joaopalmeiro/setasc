import ast

from constants import BINOPS
from utils import get_class_name


def unparse_name(value):
    return value.id


def unparse_call(value):
    fn_name = value.func.id
    args = ", ".join([UNPARSERS[get_class_name(arg)](arg) for arg in value.args])

    return f"{fn_name}({args})"


def unparse_binop(value):
    left = UNPARSERS[get_class_name(value.left)](value.left)
    op = f" {BINOPS[get_class_name(value.op)]} "
    right = UNPARSERS[get_class_name(value.right)](value.right)

    return f"{left}{op}{right}"


def unparse_literal(value):
    return repr(ast.literal_eval(value))


UNPARSERS = dict(
    Name=unparse_name,
    Call=unparse_call,
    BinOp=unparse_binop,
    Str=unparse_literal,
    List=unparse_literal,
    NameConstant=unparse_literal,
    Dict=unparse_literal,
)
