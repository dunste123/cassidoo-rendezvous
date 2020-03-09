# Given an array of unsorted integers, return the mean, median, and mode.

import statistics
import random

ints = [random.randrange(1, 101, 1) for _ in range(100)]

print(ints)


def mean(nums):
    return statistics.mean(nums)


def median(nums):
    return statistics.median(nums)


def mode(nums):
    return statistics.mode(nums)


print(mean(ints))
print(median(ints))
print(mode(ints))
