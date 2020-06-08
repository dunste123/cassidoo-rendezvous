# Given a number n, return the number of 1s in the binary representation of n.


def print_binary_ones(n):
    print("========================================")
    print("The number {}".format(n))
    print("Binary representation {0:b}".format(n))
    print("Binary representation (2) {}".format(bin(n)))

    count = 0
    x = n

    while x > 0:
        count += 1
        x = x & (x - 1)

    print("1's in binary {}".format(count))
    print("========================================")
    return None


print_binary_ones(2)
print_binary_ones(4)
print_binary_ones(3)
print_binary_ones(10)
print_binary_ones(37)
