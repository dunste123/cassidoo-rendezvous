# Write a function that when given a positive integer n and a digit d (which is not 0),
# outputs a way to represent n using only addition,
# subtraction, multiplication, exponentiation, division,
# concatenation, parenthesis and the digit d.
#
# Example:
#
# n =  6, d = 1  =>  1 + 1 + 1 + 1 + 1 + 1
# n = 10, d = 1  =>  1 | 1 - 1
# n = 12, d = 1  =>  1 | (1 + 1)
# n = 64, d = 2  =>  2 ^ (2 + 2 + 2)
# n =  1, d = 9  =>  9 / 9
#
# (In this example, | represents concatenation)


def oh_fuck(n, d):
    if d <= 0 or n <= 0:
        return 'n and d must be positive'

    return 'help'




