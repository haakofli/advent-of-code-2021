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
    lowpoints = find_lowpoints(data)

    #basin = find_basin(data, lowpoints[1][0], lowpoints[1][1], lowpoints[1][2])
    #print(data, lowpoints[2][0], lowpoints[2][1], lowpoints[2][2])

    for lowpoint in lowpoints:
        basin = find_basin(data, lowpoint[0], lowpoint[1], lowpoint[2])
        
        



def find_basin(data, lowpoint, line_index, index):  
    basin = []
    # basin.append([lowpoint, line_index, index])    
    point = [lowpoint, line_index, index]

    continue_while = True
    points_to_check = [[lowpoint, line_index, index]]

    next_iteration_points_to_check = [[lowpoint, line_index, index]]

    while(continue_while):
        # next_iteration_points_to_check = []
        for point in points_to_check:

            basin.append(point)
            
            x = find_basin_horizontally(data, point[1], point[2], point[0])
            # next_iteration_points_to_check.append([point[0], point[1], point[2]])
            

            for point_2 in x:
                basin.append(point_2)
                
                x_2 = find_basin_vertically(data, point_2[1], point_2[2], point_2[0])
                #next_iteration_points_to_check.append([point_2[0], point_2[1], point_2[2]])

                for point_3 in x_2:
                    next_iteration_points_to_check.append(point_3)
                    

        points_to_check = next_iteration_points_to_check
        if(len(points_to_check) == 0):
            continue_while = False 
        next_iteration_points_to_check = []
    
    return basin









def find_lowpoints(data):
    low_points = []

    for line_index, line in enumerate(data):
        for index, value in enumerate(line):
            if(is_low_point(data, line_index, index, value)):
                low_points.append([value, line_index, index])
    return low_points

    
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
