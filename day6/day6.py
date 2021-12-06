from time import perf_counter
from typing import List

def open_file():
    fish = []
    with open('input6.txt') as f:
        lines = f.readlines()
        fish = lines[0].split(',')

    for index, value in enumerate(fish):
        fish[index] = int(value)

    return fish 




def calc_fish(fish : List[int]):
    updated_fish = fish
    for i in range(80):
        new_fish = []
        for index, value in enumerate(updated_fish):
            if(value == 0):
                updated_fish[index] = 6
                new_fish.append(8)
            else: 
                updated_fish[index] -= 1
            
        for y in new_fish:
            updated_fish.append(y)
    print("first: ", len(updated_fish))



def calc_fish_2(fish_list):

    fish_counts = fish_list

    for i in range(256):
        updated_fish = [0 for x in range(9)]
        # updated_fish = [0] * 9
        for index, value in enumerate(fish_counts):
            if(index == 0):
                updated_fish[-1] = value
                updated_fish[6] = value
            else:
                updated_fish[index - 1] += value
        fish_counts = updated_fish
    
    print(f"Amount of fish after 256 days: {sum(fish_counts)}")
   


def format_fish(fish):
    fish_list = []
    
    for i in range(9):
        fish_list.append(0)

    for value in fish:
        fish_list[value] += 1
    
    return fish_list

        




def main():
    
    
    test_fish = [2,1,2]
    fish = open_file()

    #calc_fish(fish)

    formatted_fish = format_fish(fish)


    start = perf_counter()
    calc_fish_2(formatted_fish)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()