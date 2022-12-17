import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
DAY = "day_2"
# RESOURCE_PATH = os.path.join(ROOT_DIR, ('../resources/%s_sample.txt' % DAY)) ## test
RESOURCE_PATH = os.path.join(ROOT_DIR, '../resources/%s.txt' % DAY) ## real

def day_2():
    ## A B C : they play rock paper scissors
    ## X Y Z : you play rock paper scissors
    ## you get 1,2,3 points for rock, paper, scissors
    ## you get 0,3,6 for loss, win, draw
    print(RESOURCE_PATH)
    score_dictionary_part1 = {
        "A X" : 4,
        "A Y" : 8,
        "A Z" : 3,
        "B X" : 1,
        "B Y": 5,
        "B Z": 9,
        "C X" : 7,
        "C Y" : 2,
        "C Z": 6
    }

    ## Update so that X, Y, Z means I need to lose,draw,win respectively
    score_dictionary_part2 = {
        "A X" : 3,
        "A Y" : 4,
        "A Z" : 8,
        "B X" : 1,
        "B Y": 5,
        "B Z": 9,
        "C X" : 2,
        "C Y" : 6,
        "C Z": 7
    }
    file = open(RESOURCE_PATH, 'r')
    Lines = file.readlines()
    score = 0

    for line in Lines:
        # print(line)
        line = line.rstrip()
        # print(score_dictionary.get(line))
        score += int(score_dictionary_part2.get(line))
    
    print("The total score is")
    return score

if __name__ == "__main__":
    print(day_2())