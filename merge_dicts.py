def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries into one.
    If there are duplicate keys, the values from dict2 will overwrite those in dict1.
    """
    merged_dict = dict1.copy()  # Start with keys and values of dict1
    merged_dict.update(dict2)   # Update with keys and values of dict2, overwri  ting duplicates
    return merged_dict

# Example usage:
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
result = merge_dicts(dict_a, dict_b)
print(result)  # Output: {'a': 1, 'b': 3, 'c': 4}
