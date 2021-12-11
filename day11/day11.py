from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('input11.txt') as f:
        lines = f.readlines()
        for line in lines:
            x = (line.split('\n')[0])
            y = []
            for i in x:
                y.append(int(i))
            l.append(y)
    return l 

def calculate_octopi_flash(data):
    new_data: List[int] = data
    total_flash = []

    for i in range(5000):
        blinked = []

        for index_row, row in enumerate(new_data):
            for index_col, value in enumerate(row):
                if(value == 9):
                    new_data[index_row][index_col] = 0
                    blinked.append([index_row, index_col])
                    blink(new_data, blinked, index_row, index_col, total_flash)
                else:
                    if(not has_blinked(blinked, index_row, index_col)):
                        new_data[index_row][index_col] += 1
        

        if(i == 100):
            print(f"Part1: Total flash after {i} iterations: {len(total_flash)}")

        if(len(blinked) == 100):
            print(f"Part2: All octopi flashed in step {i + 1}")
            break


def blink(data, blinked: List, index_row, index_col, total_flash: List):

    total_flash.append(1)
    
    for i in range(index_row - 1, index_row + 2):
        for j in range(index_col - 1, index_col + 2):
            if 0 <= i < len(data) and 0 <= j < len(data[index_row]):
                if data[i][j] == 9:
                    data[i][j] = 0
                    blinked.append([i, j])
                    blink(data, blinked, i, j, total_flash)
                else:
                    if(not has_blinked(blinked, i, j)):
                        data[i][j] += 1    


def has_blinked(blinked, index_row, index_col):
    return [index_row, index_col] in blinked


def main():
    start = perf_counter()
    data = open_file()

    # my function here
    calculate_octopi_flash(data)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()