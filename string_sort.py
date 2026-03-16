def sort_strings(strings):
    """
    Sorts a list of strings alphabetically.

    :param strings: List of strings to sort.
    :return: A new list of sorted strings.
    """
    return sorted(strings)

# Example usage
if __name__ == "__main__":
    sample_strings = ["apple", "orange", "banana", "kiwi"]
    sorted_strings = sort_strings(sample_strings)
    print("Sorted strings:", sorted_strings)
