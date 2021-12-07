from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('input7.txt') as f:
        lines = f.readlines()
        temp_list = lines[0].split(',')
        for i in temp_list:
            l.append(int(i))
    return l 


def find_number(data):
    maximum = max(data)
    fuel = 1000000000
    
    for i in range(maximum):
        x = calc_fuel_use(data, i)
        if(x < fuel):
            fuel = x
    return fuel


def calc_fuel_use(data, number):
    fuel = 0
    for i in data:
        fuel += binomial_coefficient(abs(number - i) - 1) + abs(number - i)            
    return fuel


def binomial_coefficient(n):
    return int((n*n + n)/2)


def main():
    start = perf_counter()
    data = open_file()
    #test_data = [16,1,2,0,4,2,7,1,2,14]
    
    result = find_number(data)
    print(f"{result} units of fuel")


    end = perf_counter()
    print(f"{end-start} seconds to execute code")


if __name__ == "__main__":
    main()