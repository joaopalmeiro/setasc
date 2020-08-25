import ast
from parser import SetupVisitor
from pathlib import Path

from constants import SETUP
from utils import (
    convert_dict_to_single_str,
    convert_list_to_single_str,
    sort_quoted_list,
)


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


def main(file_path):
    try:
        path = Path(file_path)
        data = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"🚫 File {repr(file_path)} not found.")
    except IsADirectoryError:
        print(f"🚫 {repr(file_path)} is a directory, not a file.")
    else:
        root = ast.parse(data)
        setup_call = SetupVisitor()
        setup_call.visit(root)

        setup_call.arguments[0]["classifiers"] = sort_classifiers(
            setup_call.arguments[0]["classifiers"]
        )

        sorted_setup_arguments = join_setup_arguments(setup_call.arguments[0])
        updated_data = SETUP.sub(sorted_setup_arguments, data)

        print(updated_data)
        # path.write_text(updated_data)


if __name__ == "__main__":
    main("setup1.py")
