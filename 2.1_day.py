'''
--- Day 2, part 1: Inventory Management System ---

Adventofcode from: https://adventofcode.com

To make sure you didn't miss any, you scan the likely candidate boxes again,
counting the number that have an ID containing exactly two of any letter and then
separately counting those with exactly three of any letter. You can multiply those
two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice,
and three of them contain a letter which appears exactly three times.
Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
'''

two_count = 0
three_count = 0
count = {}

# open file with letters:
with open('2_input.txt') as file:
    for line in file:
        is_two_in_line = False  # True if a pair of letters already counted in line
        is_three_in_line = False    # True if three of letters already counted in line
        line = line.strip('\n')
        # dictionary comprehension
        count = {i: line.count(i) for i in line}
        for key in count:
            if count[key] == 2 and is_two_in_line is False:
                # 2 same letters found in line
                two_count += 1
                is_two_in_line = True
            if count[key] == 3 and is_three_in_line is False:
                # 3 same letters found in line
                three_count += 1
                is_three_in_line = True

checksum = two_count * three_count
print('checksum', checksum)
