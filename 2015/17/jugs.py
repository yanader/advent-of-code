from helpers import *
import sys

MIN_CONTAINERS = 100
TIMES_COUNTED = 0

def search(containers, index, total):
    if total == TARGET:
        return 1
    
    if total > TARGET or index == len(containers):
        return 0
    
    return (
        search(containers, index + 1, total + containers[index]) +
        search(containers, index + 1, total)
    )


def main():
    if len(sys.argv) != 2:
        return
    if sys.argv[1] == '1':
        containers = importFile("input.txt")
        count = search(containers, 0, 0)
        print(count)


main()