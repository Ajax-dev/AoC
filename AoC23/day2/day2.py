def main():
    my_file = open("./day2/day2.txt", "r")
    data = my_file.read()
    data_in_list = data.split("\n")
    #print(data_in_list)
    print(type(data_in_list))

    # Check which games are possible, record IDs and sum them
    sum = 0

    
    #test line
    print("file read as data var is ", type(data))
    index = 1
    string = data_in_list[index]
    print(string)
    day2(string)
    # sum += int(day2(my_file[index]))

def day2(file_string):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    # split up the string around the colon
    splitValues = file_string.split(':')
    gameId = splitValues[0]
    # print(gameId)
    gameId = gameId[5:]
    print(gameId)
    
    cubes = splitValues[1].split(';')
    print("checking cube validity")
    if isValidCubes(cubes):
        return gameId
    
    return 0

def isValidCubes(cubes):
    isValid = False
    print(cubes)

    return isValid


if __name__ == "__main__":
    main()