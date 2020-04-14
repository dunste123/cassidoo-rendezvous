# Given a number n, write a function to generate all combinations of well-formed parentheses.
#
# Example:
#
# generateParens(3)
# [“((()))”,
#  “(()())”,
#  “(())()”,
#  “()(())”,
#  “()()()”
# ]

# copied from https://www.programcreek.com/2014/01/leetcode-generate-parentheses-java/


def generate_parens(n):
    array = []

    _actual_generate_parens(array, "", n, n)

    return array


def _actual_generate_parens(array, string, open_pos, close_pos):
    if open_pos > close_pos:
        return

    if open_pos == 0 and close_pos == 0:
        array.append(string)
        return

    if open_pos > 0:
        _actual_generate_parens(array, string + "(", open_pos - 1, close_pos)

    if close_pos > 0:
        _actual_generate_parens(array, string + ")", open_pos, close_pos - 1)


print(generate_parens(3))  # I have no idea how it works but it does
