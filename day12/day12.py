from collections import Counter
from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('input12.txt') as f:
        lines = f.readlines()
        for line in lines:
            l.append(line.split('\n')[0].split('-'))
    return l 


def get_paths(data):
    neighboor_dict = create_neighboor_dict(data)
    print(neighboor_dict)
    
    count = []
    for node in neighboor_dict['start']:
        dfs(['start'], neighboor_dict, node, count)
    print(len(count))


def dfs(path, neighboor_dict, node, count):
    path.append(node)
    if node == 'end':
        count.append(1)
    
    else:
        for neighboor in neighboor_dict[node]:
            if can_visit_node_part2(neighboor, path):
                dfs(path, neighboor_dict, neighboor, count)
    del path[-1]


def can_visit_node_part1(node, path):
    
    if node != node.upper() and node in path: return False
    return True

def can_visit_node_part2(node, path):
    if node != node.upper() and node in path:
        if lower_repeat(path):
            return False
    return True


def lower_repeat(path):
    small_caves = [x for x in path if x.islower()]
    return len(small_caves) != len(set(small_caves))
    

def create_neighboor_dict(data):
    unique_nodes = []    
    for edge in data:
        if edge[0] not in unique_nodes: unique_nodes.append(edge[0])
        if edge[1] not in unique_nodes: unique_nodes.append(edge[1])
    
    neighboor_dict = {}
    for node in unique_nodes:
        if node != 'end':
            neighboor_dict[node] = []
            for edge in data:
                if node == edge[0] and edge[1] not in neighboor_dict[node] and edge[1] != 'start': neighboor_dict[node].append(edge[1])
                if node == edge[1] and edge[0] not in neighboor_dict[node] and edge[0] != 'start': neighboor_dict[node].append(edge[0])
    return neighboor_dict



def main():
    start = perf_counter()
    data = open_file()

    # my function here
    get_paths(data)


    end = perf_counter()
    print(f"{end-start} seconds to execute code")   




if __name__ == "__main__":
    main()


