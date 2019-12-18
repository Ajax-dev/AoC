"""
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 136818-685979.
"""

def getList(number):
    """
    Now count the doubling up of digits,
    -1 if it breaks any of rules
    2 if it has a double in it and follows rules
    """
    str1 = str(number)
    for i,j in enumerate(str1):
        if i > 0 and str1[i-1] > j:
            return -1
    list1 = list(str1)
    counter = set(list1.count(j) for j in set(str1))
    return 2 if 2 in counter else max(counter)

digit_countable = list(getList(n) for n in range(136818,685979))

print("Day 04")
print(f"1. {sum(1 for n in digit_countable if n > 1)}")
print(f"2. {sum(1 for n in digit_countable if n == 2)}")
