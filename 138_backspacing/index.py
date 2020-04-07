# Given two strings n and m, return true if they are equal when both are typed into empty text editors. The twist: #
# means a backspace character.
#
# Example:
#
# > compareWithBackspace("a##c", "#a#c")
# > true      // both strings become "c"
#
# > compareWithBackspace("xy##", "z#w#")
# > true      // both strings become ""

# import re

# regex = r"(.?#)"


def do_replace(str):
    chars = []

    for s in str:
        if s != "#":
            chars.append(s)
        elif len(chars) > 0:
            chars.pop()

    # return str.replace("#", "\b").strip()
    # return re.sub(regex, "", str).strip()
    return "".join(chars)


def compare_with_backspace(n, m):
    # Using == here https://stackoverflow.com/a/1504742/4807235
    return do_replace(n) == do_replace(m)


print(compare_with_backspace("a##c", "#a#c"))  # True
print(compare_with_backspace("xy##", "z#w#"))  # True
print(compare_with_backspace("##xy", "z#w#"))  # False
