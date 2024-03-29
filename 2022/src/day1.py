import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
# RESOURCE_PATH = os.path.join(ROOT_DIR, '../resources/day_1_sample.txt') ## test
RESOURCE_PATH = os.path.join(ROOT_DIR, '../resources/day_1.txt') ## real

def day_1():
    ## Figuring out from file day_1.txt calories carried
    ## total cals per elf is based on new line separator
    ## Find elf carrying most, how many is that total
    print(ROOT_DIR)
    file = open(RESOURCE_PATH, 'r')
    Lines = file.readlines()
    result = 0
    tempVal = 0
    totalCals = []

    for line in Lines:
        if line.strip():
            tempVal += int(line)
            # print(line)            
        else:
            totalCals.append(tempVal)
            if (result < tempVal):
                result = tempVal
            # print("Elf total: ", tempVal)
            tempVal = 0
    if (result < tempVal):
        result = tempVal
    print("Elf total: ", result)
    # print(totalCals)
    top3Cals = sorted(totalCals, reverse=True)[:3]
    print("Part 2 (top 3 sum) = " , sum(top3Cals))
        
    return result

if __name__ == "__main__":
    day_1()