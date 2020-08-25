from collections import OrderedDict


def sort_dict_based_on_list(dct, lst):
    index_map = {val: idx for idx, val in enumerate(lst)}
    return OrderedDict(sorted(dct.items(), key=lambda map_pair: index_map[map_pair[0]]))
