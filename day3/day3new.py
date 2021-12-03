def open_file():
    instructions = []
    with open('report.txt') as f:
        lines = f.readlines()
        for line in lines:
            instructions.append(line.rstrip("\n"))
    return instructions 


def remove_numbers_from_list(numbers, number_to_keep, index):
    new_list = []
    for number in numbers:
        if(int(number[index]) == number_to_keep):
            new_list.append(number)
    return new_list


def count_ones(numbers, index):
    ones = 0
    for number in numbers:
        ones += int(number[index])
    return ones


def oxygen_rating(numbers):
    new_numbers = numbers
    for i in range(len(numbers[0])):
        ones = count_ones(new_numbers, i)
        if(ones >= len(new_numbers) / 2):
            new_numbers = remove_numbers_from_list(new_numbers, 1, i)
            
        else:
            new_numbers = remove_numbers_from_list(new_numbers, 0, i)
            
        if(len(new_numbers) == 1):
            return int(new_numbers[0], 2)

def co2_rating(numbers):
    new_numbers = numbers
    for i in range(len(numbers[0])):
        ones = count_ones(new_numbers, i)
        if(ones < len(new_numbers) / 2):
            new_numbers = remove_numbers_from_list(new_numbers, 1, i)
            
        else:
            new_numbers = remove_numbers_from_list(new_numbers, 0, i)
            
        if(len(new_numbers) == 1):
            return int(new_numbers[0], 2)


def main():
    numbers = open_file()
    oxygen = oxygen_rating(numbers)
    co2 = co2_rating(numbers)
    print(f"life support: {oxygen} * {co2} = {oxygen * co2}")
    
if __name__ == "__main__":
    main()