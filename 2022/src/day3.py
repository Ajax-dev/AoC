import os
import string
from itertools import islice

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
DAY = "day_3"
# RESOURCE_PATH = os.path.join(ROOT_DIR, ('../resources/%s_sample.txt' % DAY)) ## test
RESOURCE_PATH = os.path.join(ROOT_DIR, ('../resources/%s.txt' % DAY)) ## real

def day_3():
    file = open(RESOURCE_PATH, 'r')
    Lines = file.readlines()
    sum = 0
    values = dict()
    for index, letter in enumerate(string.ascii_letters):
        values[letter] = index + 1
    # print(values)
    for line in Lines:
        # print(len(line.strip()))
        length = len(line.strip())
        str1 = line[0:int(length/2)]
        str2 = line[int(length/2):]
        common = ''.join(set(str1).intersection(str2))
        # print("string first half is: %s " % str1, " and second half is %s" % str2, " \n and common is %s" % common)
        sum += values.get(common)

    return sum

if __name__ == "__main__":
    print(day_3())