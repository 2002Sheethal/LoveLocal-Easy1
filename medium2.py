# -*- coding: utf-8 -*-
"""

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times

"""

def majority_repeated_elements(n):
    if not n:
        return []

    entries1, count1 = None, 0
    entries2, count2 = None, 0

    # Count occurrences of entries and update counters
    for num in n:
        if num == entries1:
            count1 += 1
        elif num == entries2:
            count2 += 1
        elif count1 == 0:
            entries1, count1 = num, 1
        elif count2 == 0:
            entries2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Reset counters for the second pass
    count1, count2 = 0, 0

    # Count occurrences of entries in the second pass
    for num in n:
        if num == entries1:
            count1 += 1
        elif num == entries2:
            count2 += 1

    # Check entries against the threshold ⌊ n/3 ⌋
    result = []
    if count1 > len(n) // 3:
        result.append(entries1)
    if count2 > len(n) // 3:
        result.append(entries2)

    return result

user_input = input("Enter integers separated by comma: ")
n = [int(num) for num in user_input.split(',')]

result = majority_repeated_elements(n)
print(result)
