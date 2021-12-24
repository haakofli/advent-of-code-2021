from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('input24.txt') as f:
        lines = f.readlines()
        for line in lines:
            l.append(line.split('\n')[0].split(' '))
    return l 


def part1(data):
    for line in data:
        print(line)


def main():
    start = perf_counter()
    data = open_file()

    part1(data)
    # my function here

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()