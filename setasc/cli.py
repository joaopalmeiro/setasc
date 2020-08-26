"""
Sort the keyword arguments of the `setup()` function of your `setup.py` file.
"""

import argparse
import ast
from pathlib import Path

import black

from .constants import SETUP
from .parser import SetupVisitor
from .utils import (
    convert_dict_to_single_str,
    convert_list_to_single_str,
    sort_quoted_list,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__, epilog="Let's sort!"[::-1], add_help=True
    )

    parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")
    # optional = parser.add_argument_group("optional arguments")

    required.add_argument(
        "-i",
        "--input",
        required=True,
        help="The path to the `setup.py` file to be sorted.",
        metavar="PATH",
        type=str,
        dest="input_path",
    )

    args = parser.parse_args()

    return args


def join_setup_arguments(dct):
    sorted_setup_arguments = convert_dict_to_single_str(dct)

    if r"\n" in sorted_setup_arguments:
        return f"setup({sorted_setup_arguments})".encode("unicode_escape").decode(
            "utf-8"
        )
    else:
        return f"setup({sorted_setup_arguments})"


def sort_classifiers(string):
    classifiers_list = string.lstrip("[").rstrip("]").split(", ")

    sorted_classifers_list = sort_quoted_list(classifiers_list)

    return convert_list_to_single_str(sorted_classifers_list)


def main():
    args = parse_args()

    try:
        path = Path(args.input_path)
        data = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"🚫 File {repr(args.input_path)} not found.")
    except IsADirectoryError:
        print(f"🚫 {repr(args.input_path)} is a directory, not a file.")
    else:
        root = ast.parse(data)
        setup_call = SetupVisitor()
        setup_call.visit(root)

        setup_call.arguments[0]["classifiers"] = sort_classifiers(
            setup_call.arguments[0]["classifiers"]
        )

        sorted_setup_arguments = join_setup_arguments(setup_call.arguments[0])
        updated_data = SETUP.sub(sorted_setup_arguments, data)

        updated_and_formatted_data = black.format_str(
            updated_data,
            mode=black.FileMode(target_versions={black.TargetVersion.PY36}),
        )

        path.write_text(updated_and_formatted_data)


if __name__ == "__main__":
    main()
