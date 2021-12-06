from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('inputX.txt') as f:
        lines = f.readlines()
        for line in lines:
            l.append(line.split('\n'))
    return l 





def main():
    start = perf_counter()
    data = open_file()

    # my function here

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()