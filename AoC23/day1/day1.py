import re
def main():
    my_file = open("day1.txt", "r")
    data = my_file.read()
    data_in_list = data.split("\n")
    #print(data_in_list)
    print(type(data_in_list))
    output = day1(data_in_list)
    print(output)

def day1(file):
    #print(len(file))
    total = 0

    #test line
    # index = 1
    # print(file[index])
    # total += int(findNumInString(file[index]))
    
    for i in file:
        res = findNumInString(i)
        total += int(res)
        
    return total

def findNumInString(string):
    # How to find digits in the string with regex - this was part one, then just returned 0 and -1 converted to string
    res = re.findall('\d', string)

    # mapping
    mapOfNums = {
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    # combine patterns
    numStrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    stringRes = re.findall(r"(?=("+'|'.join(numStrings)+r"))", string)
    # stringRes = re.findall("(\d)|(?=one|two|three|four|five|six|seven|eight|nine)", string)
    print(stringRes)

    counter = 0
    for j in stringRes:
        if j in mapOfNums.keys():
            stringRes[counter] = str(mapOfNums[j])
        counter+=1

    print("new after dictionary parsing")
    print(stringRes)
    res = stringRes[0] + stringRes[-1]
    # print(res)
    return res

if __name__ == "__main__":
    main()