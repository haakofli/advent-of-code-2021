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
    unique_points = []
    neighboors = {}
    complete_paths = []
    paths = []

    path = ['start']

    for line in data:
        if line[0] not in unique_points:
            unique_points.append(line[0])
        if line[1] not in unique_points:
            unique_points.append(line[1])

    for point in unique_points:
        neighboors[point] = []

    for line in data:
        if line[1] != 'start': neighboors[line[0]].append(line[1])
        if line[0] != 'start' and line[0] != 'end': neighboors[line[1]].append(line[0])


    print("neighboors: ", neighboors)
    for i in neighboors['start']:
        x = dfs(['start', i], paths, neighboors, i)
        print(x)
    
    for i in paths:
        print(i)

            
    


def dfs(path, paths, neighboors, node):  #function for dfs 
    print(path)
    if(node == 'end'):
        x = []
        for i in path:
            x.append(i)
        x.append(node)
        paths.append(x)
        
        

    elif can_visit(path, neighboors, node):
        path.append(node)
        for neighbour in neighboors[node]:
            dfs(path, paths, neighboors, neighbour)


def find_neighboors(data, node):
    neighboors = []
    for line in data:
        if node[-1] == line[0]:
            neighboors.append(line)
    return neighboors


def can_visit(path, neighboors, node):
    if node != node.upper() and node in path:
        return False

    for neighboor in neighboors[node]:
        if neighboor.upper() == neighboor or neighboor not in neighboors[node]:
            return True
    return False

    


def main():
    start = perf_counter()
    data = open_file()

    # my function here
    part1(data)


    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()