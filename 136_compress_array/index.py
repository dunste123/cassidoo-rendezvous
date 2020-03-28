# Given a sorted array of characters, compress it in-place.
# example:
# compress(["a","a","b","b","b","c","c"])
# > ["a","2","b","3","c","2"]
# // "aa" is replaced by "a2", "bbb" is replaced by "b3", "cc" is replaced by "c2".


def compress(array):
    found_chars = {}

    for item in array:
        if item not in found_chars:
            found_chars[item] = 0

        found_chars[item] += 1

    return found_chars


output = compress(["a", "a", "b", "b", "b", "c", "c"])

print(output)  # {'a': 2, 'b': 3, 'c': 2}
