# Day 2: 1202 Program Alarm
# Process IntCode, then move forward 4 positions
# Should be array manipulation
from itertools import product

""" Instructions
An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0).
Here, you will find an opcode - either 1, 2, or 99.
The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt.
Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position.
The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values,
and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20,
add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
"""
# Provided intcode
intCodeProg = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]

def function(noun, verb, array):
    i = 0
    codes = array.copy()
    codes[1] = noun
    codes[2] = verb
    while i < len(codes):
        opcode = codes[i]
        if opcode == 99:
            break
        if opcode == 1:
            codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
            i = i + 4
        if opcode == 2:
            codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
            i = i + 4
        opcode = codes[i]
    return codes

#ALWAYS DEFINE FUNCTIONS BEFORE CALLING THEM

test1 = [1, 0, 0, 0, 99]
test2 = [2, 3, 0, 3, 99]
test3 = [2, 4, 4, 5, 99, 0]
test4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]

result1 = function(0,0,test1)
result2 = function(3,0,test2)
result3 = function(4,4,test3)
result4 = function(1,1,test4)

# Testing
print("----HERE IS THE TESTING----")
print([1, 0, 0, 0, 99])
print(" after opcode should be: ", [2, 0, 0, 0, 99])
print("But is : ", result1)
print("So result is... ", result1 == [2, 0, 0, 0, 99])
print("")

print([2, 3, 0, 3, 99])
print(" after opcode should be: ", [2, 3, 0, 6, 99])
print("But is : ", result2)
print("So result is... ", result2 == [2, 3, 0, 6, 99])
print("")

print([2, 4, 4, 5, 99, 0])
print(" after opcode should be: ", [2, 4, 4, 5, 99, 9801])
print("But is : ", result3)
print("So result is... ", result3 == [2, 4, 4, 5, 99, 9801])
print("")

print([1, 1, 1, 4, 99, 5, 6, 0, 99])
print(" after opcode should be: ", [30, 1, 1, 4, 2, 5, 6, 0, 99])
print("But is : ", result4)
print("So result is... ", result4 == [30, 1, 1, 4, 2, 5, 6, 0, 99])
print("")


##print("BEFORE replacing ", function(intCodeProg))
print("REPLACING INDEX 1 with 12 and INDEX 2 with 2")
#intCodeProg[1] = 12
#intCodeProg[2] = 2
print(".....")
print("RUNNING FUNCTION")
print(function(12,2,intCodeProg))
tempArr = function(12,2,intCodeProg)
print("Value at 0: ", tempArr[0], " followed by ", tempArr[1], tempArr[2], tempArr[3])
# 3790689

print("Part 2")
print("here")
for noun, verb in product(range(0,100), range(0,100)):
    tempArr2 = function(noun,verb,intCodeProg)
    if tempArr2[0] == 19690720:
        print(100 * noun, " | ",  verb)
        break

#print(tempArr2[1], " : ", tempArr2[2])
#print(100 * tempArr2[1] + tempArr2[2])
