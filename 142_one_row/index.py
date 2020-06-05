# Given an array of words, return the words that can be typed using letters of only one row on a keyboard.
#
# Extra credit: Include the option for a user to pick the type of keyboard they are using (ANSI, ISO, etc)!
#
# Example:
#
# $ oneRow(['candy', 'doodle', 'pop', 'shield', 'lag', 'typewriter'])
# $ ['pop', 'lag', 'typewriter']

rows = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]


def one_row(words):
    possible_words = []

    for row in rows:
        for word in words:
            contains = all(letter in row for letter in word)

            if contains:
                possible_words.append(word)

    return possible_words


print(one_row(['candy', 'doodle', 'pop', 'shield', 'lag', 'typewriter']))  # ['pop', 'typewriter', 'lag']
