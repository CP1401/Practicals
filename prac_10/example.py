"""
CP1401 - Practical 10 - Files
Example Program - Scores

Pseudocode:

total = 0
count = 0
open "scores.txt" for reading as in_file
for line in in_file
    score = line converted to float
    total = total + score
    count = count + 1
close in_file
average = total / count
print average
"""

total = 0.0
count = 0

filename = "scores.txt"
# filename = input("Filename: ")
in_file = open(filename, 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
    print(f"Score = {score:4.1f}   Total so far = {total:6.1f}")
in_file.close()
average = total / count
print(f"Average = {average:.1f}")
