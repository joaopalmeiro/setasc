import shlex
from collections import OrderedDict


def sort_dict_based_on_list(dct, lst):
    index_map = {val: idx for idx, val in enumerate(lst)}
    return OrderedDict(sorted(dct.items(), key=lambda map_pair: index_map[map_pair[0]]))


def get_class_name(obj):
    return obj.__class__.__name__


def convert_dict_to_single_str(dct, item_sep=", ", pair_sep=" = "):
    return item_sep.join(f"{key}{pair_sep}{value}" for key, value in dct.items())


def convert_list_to_single_str(lst):
    return f"[{', '.join(lst)}]"


def get_indentation(string):
    whitespaces = len(string) - len(string.lstrip())
    ignoring_newline_whitespaces = len(string) - len(string.lstrip("\n"))

    return whitespaces - ignoring_newline_whitespaces


def remove_empty_strings(lst):
    # Strings that contain only the `\n` character or this character and some whitespaces are also removed.
    return [el for el in lst if el.strip()]


def sort_quoted_list(lst, ascending=True):
    # This `key` is used to easily "ignore" quote marks within strings.
    return sorted(lst, reverse=False if ascending else True, key=shlex.split)
