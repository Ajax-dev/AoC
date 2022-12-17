import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
DAY = "day_<num>"
# RESOURCE_PATH = os.path.join(ROOT_DIR, ('../resources/%s_sample.txt' % DAY)) ## test
RESOURCE_PATH = os.path.join(ROOT_DIR, ('../resources/%s.txt' % DAY)) ## real

def day_0():
    file = open(RESOURCE_PATH, 'r')
    Lines = file.readlines()
    print(RESOURCE_PATH)
    return

if __name__ == "__main__":
    day_0()