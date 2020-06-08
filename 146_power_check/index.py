# Given a positive integer N, check if N is a power of 2 (N is 2^x for some x).


def is_power_of_2(x):
    # some bit manip shit
    # https://stackoverflow.com/a/57025941/4807235
    return (x & (x-1) == 0) and x != 0


print(is_power_of_2(2))
print(2 ** 20)
print(is_power_of_2(2 ** 20))
