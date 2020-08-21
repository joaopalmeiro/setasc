import re
import shlex
from pathlib import Path

CLASSIFIERS = re.compile(r"classifiers=\[[^\]]*\]", re.DOTALL)
CLASSIFIERS_LIST = re.compile(r"classifiers=\[([^\]]*)\]", re.DOTALL)


def remove_empty_strings(lst):
    return [el for el in lst if el.strip()]


def sort_classifiers(lst, ascending=True):
    # This `key` is used to easily "ignore" quote marks within strings.
    return sorted(lst, reverse=False if ascending else True, key=shlex.split)


def get_indentation(el):
    whitespaces = len(el) - len(el.lstrip())
    ignoring_newline_whitespaces = len(el) - len(el.lstrip("\n"))

    return whitespaces - ignoring_newline_whitespaces


def get_classifiers_data(data):
    classifiers_data = CLASSIFIERS_LIST.findall(data)
    classifiers_data = classifiers_data[0].split(",")

    return sort_classifiers(remove_empty_strings(classifiers_data))


def join_classifiers_data(lst):
    classifiers_str = ",".join(lst)

    indentation = get_indentation(classifiers_str) // 2
    end_whitespaces = " " * indentation

    return f"classifiers=[{classifiers_str},\n{end_whitespaces}]"


def main(file_path):
    try:
        path = Path(file_path)
        data = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"🚫 File {repr(file_path)} not found.")
    except IsADirectoryError:
        print(f"🚫 {repr(file_path)} is a directory, not a file.")
    else:
        classifiers_data = join_classifiers_data(get_classifiers_data(data))
        updated_data = CLASSIFIERS.sub(classifiers_data, data)
        path.write_text(updated_data)


if __name__ == "__main__":
    main("setup.py")
