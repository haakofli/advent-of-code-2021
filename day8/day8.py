from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('input8.txt') as f:
        lines = f.readlines()
        for line in lines:
            x = line.rstrip().split('|')[0].split(' ')
            del x[-1]

            y = line.rstrip().split('|')[1].split(' ')
            del y[0]
            
            l.append({'input': x, 'output': y})
    return l 


def find_numbers(data):
    total = 0
    for i in data:
        numbers_dict = find_numbers_dict(i['input'])
        
        x = add_number_together(numbers_dict, i['output'])
        total += x

    return total


def add_number_together(numbers_dict, output_list):
    total = ""
    for i in output_list:
        for x in numbers_dict:
            if(sorted(i) == sorted(numbers_dict[x][0])):
                total += str(numbers_dict[x][1])
    return int(total)



def find_numbers_dict(input_code):
    sorted_input = sorted(input_code, key=len)
    numbers = {}

    numbers['one'] = [sorted_input[0], 1]
    numbers['seven'] = [sorted_input[1], 7]
    numbers['four'] = [sorted_input[2], 4]
    numbers['eight'] = [sorted_input[-1], 8]

    for i in sorted_input[6:9]:
        for char in sorted_input[0]:
            if char not in i:
                
                numbers['six'] = [i, 6]
                for y in sorted_input[3:6]:
                    if char not in y:
                        numbers['five'] = [y, 5]
    
    for i in sorted_input[6:9]:
        if(i != numbers['six'][0]):
            for char in numbers['four'][0]:
                if(char not in i):
                    numbers['zero'] = [i, 0]

    for i in sorted_input[6:9]:
        if(i != numbers['six'][0] and i != numbers['zero'][0]):
            numbers['nine'] = [i, 9]


    for i in sorted_input[3:6]:
        for char in numbers['five'][0]:
            for char2 in numbers['seven'][0]:
                if(char not in i and char2 not in i):
                    numbers['two'] = [i, 2]
    

    for i in sorted_input[3:6]:
        if(i != numbers['two'][0] and i != numbers['five'][0]):
            numbers['three'] = [i, 3]
           
    return numbers




def part1(o):
    count = 0
    for i in o:
        if(len(i) == 2 or len(i) == 4 or len(i) == 7 or len(i) == 3):
            count += 1
    return count
            
        


def main():
    start = perf_counter()
    data = open_file()
    total = find_numbers(data)
    print(f"Svaret er: {total}")

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()

