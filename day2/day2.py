
def open_file():
    instructions = []
    with open('instructions.txt') as f:
        lines = f.readlines()
        for line in lines:
            instructions.append(line.rstrip("\n"))
    return instructions 



def calculate_position_part_1(instructions):
    horizontal = 0
    depth = 0
    for instruction in instructions:
        if(instruction.split()[0] == 'forward'):
            horizontal += int(instruction.split()[1])
        elif(instruction.split()[0] == 'up'):
            depth -= int(instruction.split()[1])
        else:
            depth += int(instruction.split()[1])
    return horizontal * depth


def calculate_position_part_2(instructions):
    horizontal = 0
    depth = 0
    aim = 0

    for instruction in instructions:
        if(instruction.split()[0] == 'forward'):
            horizontal += int(instruction.split()[1])
            depth += aim * int(instruction.split()[1])
        elif(instruction.split()[0] == 'up'):
            aim -= int(instruction.split()[1])
        else:
            aim += int(instruction.split()[1])
    return horizontal * depth



def main():
    instructions = open_file()
    # result = calculate_position_part_1(instructions)
    result = calculate_position_part_2(instructions)
    print(result)

if __name__ == "__main__":
    main()
