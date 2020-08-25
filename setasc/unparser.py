import ast

from constants import BINOPS


def unparse_name(value):
    return value.id


def unparse_call(value):
    fn_name = value.func.id
    args = ", ".join([UNPARSERS[arg.__class__.__name__](arg) for arg in value.args])

    return f"{fn_name}({args})"


def unparse_binop(value):
    left = UNPARSERS[value.left.__class__.__name__](value.left)
    op = f" {BINOPS[value.op.__class__.__name__]} "
    right = UNPARSERS[value.right.__class__.__name__](value.right)

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
