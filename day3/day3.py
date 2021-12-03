def open_file():
    instructions = []
    with open('report.txt') as f:
        lines = f.readlines()
        for line in lines:
            instructions.append(line.rstrip("\n"))
    return instructions 



def calculate_gamma_and_epsilon(numbers):
    occurance_of_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for number in numbers:
        for index, char in enumerate(number):
            if(int(char) == 1):
                occurance_of_ones[index] += 1
    epsilon = ""
    gamma = ""
    for i in occurance_of_ones:
        if(int(i) < 500):
            epsilon += "0"
            gamma += "1"
        else:
            epsilon += "1"
            gamma += "0"
    print("Epsilon = " + epsilon)
    print("Gamma = " + gamma)



def oxygen_generator_rating(numbers):
    new_numbers = numbers
    for i in range(len(numbers[0])):
        new_numbers_2 = []
        if(most_ones_oxygen(new_numbers, i)):
            new_numbers_2 = filter_list(new_numbers, 1, i)
        else:
            new_numbers_2 = filter_list(new_numbers, 0, i)

        if(len(new_numbers_2) == 1):
            integer = int(new_numbers_2[0], 2)
            return integer
        
        new_numbers = new_numbers_2


def CO2_scrubber_rating(numbers):
    new_numbers = numbers
    for i in range(len(numbers[0])):
        new_numbers_2 = []
        if(most_ones_co2(new_numbers, i)):
            new_numbers_2 = filter_list(new_numbers, 0, i)
        else:
            new_numbers_2 = filter_list(new_numbers, 1, i)

        if(len(new_numbers_2) == 1):
            integer = int(new_numbers_2[0], 2)
            return integer
        
        new_numbers = new_numbers_2   
    
   


def filter_list(numbers, number_to_keep, index):
    new_numbers = []
    for number in numbers:
        if(int(number[index]) == number_to_keep):
            new_numbers.append(number)
    return new_numbers
                
    
def most_ones_oxygen(numbers, index):
    occurance_of_ones = 0
    for number in numbers:
        occurance_of_ones += int(number[index])
    if(occurance_of_ones > (len(numbers) / 2)):
        return True
    else: 
        return False
            
def most_ones_co2(numbers, index):
    
    occurance_of_ones = 0
    for number in numbers:
        occurance_of_ones += int(number[index])
    if(occurance_of_ones > (len(numbers) / 2)):
        return True
    else: 
        return False


def main():
    numbers = open_file()
    # calculate_gamma_and_epsilon(numbers)
    oxygen = oxygen_generator_rating(numbers)
    co2 = CO2_scrubber_rating(numbers)
    print(f"life support: oxygen {oxygen} * {co2} = {oxygen * co2}")
    print("denne er feil! bruk den andre")

if __name__ == "__main__":
    main()

