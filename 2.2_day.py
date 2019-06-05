'''
--- Day 2, part 2: Inventory Management System ---

Adventofcode from: https://adventofcode.com

Confident that your list of box IDs is complete, you're ready to find
the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same
position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz

The IDs abcde and axcye are close, but they differ by two characters
(the second and fourth). However, the IDs fghij and fguij differ by exactly one character,
the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above,
this is found by removing the differing character from either ID, producing fgij.)
'''

import Levenshtein as levenshtein

text = open("2_input.txt")
lines = text.read().split()
correct = []

for box_one in lines:
    for box_two in lines:
        if levenshtein.distance(box_one, box_two) == 1:     # search for similar lines with only 1 different letter
            correct.append(box_one)
            correct.append(box_two)

# find and print letters common for box_one and box_2
for box_one in correct:
    for box_two in correct:
        for i in range(len(box_one)):
            if box_one[i] != box_two[i]:
                solution = box_one[:i] + box_one[i+1:]

print(solution)
