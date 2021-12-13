from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('test_input12.txt') as f:
        lines = f.readlines()
        for line in lines:
            l.append(line.split('\n')[0].split('-'))
    return l 


def part1(data):
    paths = []
    new_data = add_valid_lines(data)
    
    for node in data:
        if node[0] == 'start':
            paths.append([node])

    continue_to_find_new_paths = True

    while continue_to_find_new_paths:
        new_paths = find_new_paths(paths, new_data)
        if(new_paths == paths):
            continue_to_find_new_paths = False
        paths = new_paths
    
        for path in paths:
            string_test = ""
            i = 0
            for val in path:
                string_test += " " + val[i]
                if(i == 1):
                    i = 0
                i += 1
            print(string_test)
    print(len(paths))


def add_valid_lines(data):
    new_data = []
    for line in data:
        new_data.append(line)
        new_data.append([line[1], line[0]])
    return new_data


def can_visit_node(data, node, path):
    if(node[1] == 'start' or node[0] == 'end'):
        return False
    is_lower = node[1] != node[1].upper()
    for line in path:
        if line[1] == node[1] and is_lower:
            return False
    return True


def find_new_paths(paths, data):

    new_paths = []
    for path in paths:
        neighboors = find_neighboors(data, path[-1])
        if(len(neighboors) == 0):
            new_paths.append(path)
        for neighboor in neighboors:
            if(can_visit_node(data, neighboor, path)):
                x = []
                for i in path: x.append(i)
                x.append(neighboor)
                new_paths.append(x)
            

    return new_paths



def find_neighboors(data, node):
    neighboors = []
    for line in data:
        if node[-1] == line[0]:
            neighboors.append(line)
    return neighboors



def dfs(visited: List, data, node):
    if node not in visited:
        visited.append(node)
        neighboors = find_neighboors(data, node)
        for neighboor in neighboors:
            dfs(visited, data, neighboor)


def main():
    start = perf_counter()
    data = open_file()

    # my function here
    part1(data)


    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()