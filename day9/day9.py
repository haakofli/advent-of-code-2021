from time import perf_counter
from typing import List


def open_file():
    l = []
    with open('test_input9.txt') as f:
        lines = f.readlines()
        for line in lines:
            x = line.split('\n')[0]
            x_map = map(int, x)
            l.append(list(x_map))
    return l


def find_sum_of_lowpoints(data):
    total_risk_level = 0

    for line_index, line in enumerate(data):
        for index, value in enumerate(line):
            if(is_low_point(data, line_index, index, value)):
                total_risk_level += (value + 1)
                
    
    print(total_risk_level)


def part2(data):
    low_points = find_lowpoints(data)
    basins = []
    continue_to_look = True
    basins = low_points

    i = 0
    while(continue_to_look):
        print(f"--------------------------- ITERATION NUMBER {i}---------------------------------")
        i += 1
        if(i == 2):
            continue_to_look = False
        
        new_basins = find_basins(data, basins)
        newer_basins = []
        
        for index, value in enumerate(basins):

            print("basin: ", value)
            print("new_basins: ", new_basins[index])

            if(len(value) < len(new_basins[index])):
                newer_basins.append(new_basins[index])
            else:
                newer_basins.append(value)

        #print(basins)
        
        

        if(new_basins == basins or len(new_basins) < len(basins)):
            
            continue_to_look = False
        
        basins = newer_basins
    
    
    #for basin in basins:
    #    print(len(basin))



def find_lowpoints(data):
    low_points = []

    for line_index, line in enumerate(data):
        for index, value in enumerate(line):
            if(is_low_point(data, line_index, index, value)):
                low_points.append([[value, line_index, index]])
    return low_points



def find_basins(data, basins):
    new_basins = []
    new_basins_2 = []
    points_horizontally = []
    points_vertically = []

    for index, basin in enumerate(basins):
        for point in basin:
            y = []
            x = find_basin_horizontally(data, point[1], point[2], point[0])
            
            if(len(x) != 0):
                for i in x:
                    if(i not in basin):
                        y.append(i)
            
            if(len(y) != 0):
                new_basin = []
                for j in y:
                    new_basin.append(j)
                for j in basin:
                    new_basin.append(j)
                
                points_horizontally = new_basin
            else:
                points_horizontally.append(basin[0])
            
            if(len(points_horizontally) > len(basin)):
                new_basins.append(points_horizontally)
            else:
                new_basins.append(basins[index])
                #print(b)
            
            #print("points horizontally: ", points_horizontally)
        
            points_horizontally = []

    
    new_points = []    
    for index, basin in enumerate(new_basins):
        for point in basin:
            y = []
            x = find_basin_vertically(data, point[1], point[2], point[0])
            
            if(len(x) != 0):
                for i in x:
                    if(i not in basin):
                        y.append(i)
            
            if(len(y) != 0):
                new_basin = []
                for j in y:
                    new_basin.append(j)
                for j in basin:
                    new_basin.append(j)
                
                points_vertically = new_basin
        
            else:
                points_vertically.append(basin[0])
            
            if(len(points_vertically) > len(basin)):
                new_basins_2.append(points_vertically)
            else:
                new_basins_2.append(basins[index])
        
        
    
    return new_basins_2
    
    
def find_basin_vertically(data, line_index, index, low_point):
    basin_vertically = []
    continue_look_up = True
    continue_look_down = True
    next_index_up = line_index - 1
    next_index_down = line_index + 1
    prev_point = low_point

    while(continue_look_down):
        if(next_index_down != len(data)):
            if(data[next_index_down][index] != 9 and data[next_index_down][index] > prev_point):
                prev_point = data[next_index_down][index]
                basin_vertically.append([prev_point, next_index_down, index])
                next_index_down += 1
            else:
                continue_look_down = False
        else:
            continue_look_down = False
    
    prev_point = low_point
    while(continue_look_up):
        if(next_index_up != -1):
            if(data[next_index_up][index] != 9 and data[next_index_up][index] > prev_point):
                prev_point = data[next_index_up][index]
                basin_vertically.append([prev_point, next_index_up, index])
                next_index_up -= 1
            else:
                continue_look_up = False
        else:
            continue_look_up = False

    return basin_vertically



def find_basin_horizontally(data, line_index, index, low_point):
    basin_horizontally = []
    continue_look_left = True
    continue_look_right = True
    next_index_right = index + 1
    next_index_left = index - 1
    prev_point = low_point

    while(continue_look_left):
        if(next_index_left != -1):
            if(data[line_index][next_index_left] != 9 and data[line_index][next_index_left] > prev_point):
                prev_point = data[line_index][next_index_left]
                basin_horizontally.append([prev_point, line_index, next_index_left])
                next_index_left -= 1


            else:
                continue_look_left = False
        else:
            continue_look_left = False


    prev_point = low_point
    while(continue_look_right):
        if(next_index_right != len(data[line_index])):
            if(data[line_index][next_index_right] != 9 and data[line_index][next_index_right] > prev_point):
                prev_point = data[line_index][next_index_right]
                basin_horizontally.append([prev_point, line_index, next_index_right])
                next_index_right += 1

            else:
                continue_look_right = False
        else:
            continue_look_right = False
    return basin_horizontally



def is_low_point(data, line_index, index, value):
    neighboors = []
    
    if(line_index != 0):
        neighboors.append(data[line_index - 1][index])

    if(index != 0):
        neighboors.append(data[line_index][index - 1])

    if(line_index != len(data) - 1):
        neighboors.append(data[line_index + 1][index])

    if(index != len(data[line_index]) - 1):
        neighboors.append(data[line_index][index + 1])

    
    for i in neighboors:
        if(i <= value):
            return False

    
    return True


def main():
    start = perf_counter()
    data = open_file()
    
    # my function here
    # part 1
    #find_sum_of_lowpoints(data)

    # part 2
    part2(data)
    # find_basins(data)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")


if __name__ == "__main__":
    main()
