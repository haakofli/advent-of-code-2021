from time import perf_counter
from typing import List

def open_file():
    dots = []
    folds = []

    append_to_dots = True
    with open('input13.txt') as f:
        lines = f.readlines()
        for line in lines:
            if(line.split('\n')[0] == ''):
                append_to_dots = False
            else:
                if(append_to_dots):
                    x = line.split('\n')[0]
                    dots.append([int(x.split(',')[0]), int(x.split(',')[1])])
                else:
                    x = line.split('\n')[0]
                    y = x.split(' ')[-1]
                    folds.append(y)
    return dots, folds




def decode_manual(dots, folds):
    
    maximum_x = 0
    maximum_y = 0
    for dot in dots:
        if(dot[0] > maximum_x): maximum_x = dot[0]
        if(dot[1] > maximum_y): maximum_y = dot[1]

    temp_dots = dots.copy()
    for fold in folds:
        temp_dots = find_new_dots(temp_dots, fold)
        if fold == folds[0]: print("PART1: \n", len(temp_dots))
    
    print("PART2: ")
    print_matrix(temp_dots)
    
    
    
def print_matrix(dots):
    maximum_x = 0
    maximum_y = 0
    for dot in dots:
        if(dot[0] > maximum_x): maximum_x = dot[0]
        if(dot[1] > maximum_y): maximum_y = dot[1]

    matrix = []

    for i in range(maximum_y + 1):
        row = []
        for j in range(maximum_x + 1):
            if [j, i] in dots:
                row.append('X')
            else:
                row.append('|')
        matrix.append(row)

    for row in matrix:
        print(row)


def find_new_dots(dots, fold):
    fold_char = fold.split('=')[0]
    fold_line = int(fold.split('=')[1])
    
    new_dots = []

    if fold_char == 'y':
        for dot in dots:
            if dot[1] > fold_line:
                if [dot[0], (fold_line*2) - dot[1]] not in new_dots and (fold_line*2) - dot[1] > -1:
                    new_dots.append([dot[0], (fold_line*2) - dot[1]])
            else:
                if dot not in new_dots:
                    new_dots.append(dot)
    
    if fold_char == 'x':
        for dot in dots:
            if dot[0] > fold_line:
                if [(fold_line*2) - dot[0], dot[1]] not in new_dots and (fold_line*2) - dot[0] > -1:
                    new_dots.append([(fold_line*2) - dot[0], dot[1]])
            else:
                if dot not in new_dots:
                    new_dots.append(dot)

    return new_dots


def main():
    start = perf_counter()
    dots, folds = open_file()

    # my function here
    decode_manual(dots, folds)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()