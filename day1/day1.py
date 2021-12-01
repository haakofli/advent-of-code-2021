

def open_file():
    measurements = []
    with open('measurements.txt') as f:
        lines = f.readlines()
        for line in lines:
            line.rstrip()
            measurements.append(int(line.strip()))
    return measurements
        

def count_increases_part1(measurements):
    count = 0
    for index, measurement in enumerate(measurements):
        if(index != 0):
            if(measurements[index - 1] < measurement):
                count += 1  
    return count


def count_increases_part2(measurements):
    count = 0
    for index, measurement in enumerate(measurements):
        if(index > 2):
            first_sum = sum(measurements[index - 3:index]) 
            second_sum = sum(measurements[index - 2:index + 1])
            
            # alternativ måte
            #first_sum = measurements[index - 3] + measurements[index - 2] + measurements[index - 1]
            #second_sum = measurements[index - 2] + measurements[index - 1] + measurement
            if(first_sum < second_sum):
                count += 1
    return count





def main():
    measurements = open_file()
    # count = count_increases_part1(measurements)
    count = count_increases_part2(measurements)
    print(count)
    

if __name__ == "__main__":
    main()
