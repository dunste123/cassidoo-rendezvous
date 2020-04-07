# You're given a broken calculator that has a number showing on its display. You can only perform two operations:
#
#     Double the number on the display
#     Subtract 1 from the number on the display
#
# Write a function that takes in the number X (the initial number on the display) and Y (the result that you want)
# and returns the minimum number of operations needed to display Y.
#
# Example:
#
# > brokenCalc(3, 10)
# > 3                // 3 -> 6 -> 5 -> 10
#
# I cheated: https://twitter.com/tzyinc/status/1244877646103605248?s=21


def broken_calc(numX, numY):
    steps = 0

    while numY > numX:
        steps += 1

        if numY % 2 is 0:
            numY = numY >> 1
        else:
            numY += 1

    return steps + numX - numY


print(broken_calc(3, 10))
