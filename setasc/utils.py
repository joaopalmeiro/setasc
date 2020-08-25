from collections import OrderedDict


def sort_dict_based_on_list(dct, lst):
    index_map = {val: idx for idx, val in enumerate(lst)}
    return OrderedDict(sorted(dct.items(), key=lambda map_pair: index_map[map_pair[0]]))


def get_class_name(obj):
    return obj.__class__.__name__


def convert_dict_to_single_str(dct, item_sep=", ", pair_sep=" = "):
    return item_sep.join(f"{key}{pair_sep}{value}" for key, value in dct.items())
