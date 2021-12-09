from time import perf_counter
from typing import List


def open_file():
    l = []
    with open('input9.txt') as f:
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

    basin_sizes = []
    largest_basins = []
    #basin = find_basin(data, lowpoints[1][0], lowpoints[1][1], lowpoints[1][2])
    #print(data, lowpoints[2][0], lowpoints[2][1], lowpoints[2][2])

    for lowpoint in lowpoints:
        basin = find_basin(data, lowpoint[0], lowpoint[1], lowpoint[2])
        basin_sizes.append(len(basin))
    
    highest = 0
    second_highest = 0
    third_highest = 0
    for index, value in enumerate(basin_sizes):
        if(value > highest):
            third_highest = second_highest
            second_highest = highest
            highest = value
        elif(value > second_highest):
            third_highest = second_highest
            second_highest = value
        elif(value > third_highest):
            third_highest = value
    print(highest * second_highest * third_highest)
    
        



def find_basin(data, lowpoint, line_index, index):
    visited = []
    
    #visited.append([lowpoint, line_index, index])
    
    dfs(visited, data, [lowpoint, line_index, index])
    return visited
    

def dfs(visited, graph, node):
    if node not in visited:
        
        
        current = node[0]
        next_neighboor = graph[node[1]][node[2]]

        visited.append(node)
        if(node[1] != 0):
            next_neighboor = graph[node[1]-1][node[2]]
            if(next_neighboor != 9 and next_neighboor > current):
                dfs(visited, graph, [graph[node[1] - 1][node[2]], node[1] - 1, node[2]])

        if(node[2] != 0):
            next_neighboor = graph[node[1]][node[2]-1]
            if(next_neighboor != 9 and next_neighboor > current):
                dfs(visited, graph, [graph[node[1]][node[2] - 1], node[1], node[2] - 1])

        if(node[1] != len(graph) - 1):
            next_neighboor = graph[node[1]+1][node[2]]
            if(next_neighboor != 9 and next_neighboor > current):
                dfs(visited, graph, [graph[node[1] + 1][node[2]], node[1] + 1, node[2]])

        if(node[2] != len(graph[node[1]]) - 1):
            next_neighboor = graph[node[1]][node[2]+1]
            if(next_neighboor != 9 and next_neighboor > current):
                dfs(visited, graph, [graph[node[1]][node[2] + 1], node[1], node[2] + 1])





def find_lowpoints(data):
    low_points = []

    for line_index, line in enumerate(data):
        for index, value in enumerate(line):
            if(is_low_point(data, line_index, index, value)):
                low_points.append([value, line_index, index])
    return low_points


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
