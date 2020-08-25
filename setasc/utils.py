def sort_dict_keys_based_on_list(dct, lst):
    index_map = {v: i for i, v in enumerate(lst)}
    return sorted(dct.items(), key=lambda pair: index_map[pair[0]])
