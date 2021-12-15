from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('test_input15.txt') as f:
        lines = f.readlines()
        for line in lines:
            y = []
            x = line.split('\n')[0]
            for num in x:
                y.append(int(num))
            l.append(y)
    return l 


def part1(data):
    x = dijkstra(data, '0,0')
    print(x)


def part2(data):
    new_data = expand_graph(data)
    x = dijkstra(new_data, '0,0')
    print(f"Dette er svaret hvis jeg bruker test data: {x[list(x)[-1]]}")
    print(f"Dette er svaret hvis jeg bruker real data: {x[list(x)[-2]]}")

    '''print("Skriver til fil...")
    with open('output.txt', 'a') as the_file:
        for key in x:
            the_file.write(f"{key} -> {x[key]} \n")'''


def expand_graph(data):
    temp_graph = []
    expanded_horizontally = [] 
    expanded_graph = []

    for row in data:
        new_row = []
        for i in range(5):
            for col in row:
                x = col + i
                if x > 9: x = x % 9
                new_row.append(x)
        expanded_horizontally.append(new_row)

    for i in range(5):
        new_rows = []
        for row in expanded_horizontally:
            new_row = []
            for col in row:
                x = col + i
                if x > 9: x = x % 9
                new_row.append(x)
            new_rows.append(new_row)
        temp_graph.append(new_rows)

    for row in temp_graph:
        for y in row:
            expanded_graph.append(y)

    return expanded_graph


def dijkstra(graph, source):
    dist = {}
    dist[source] = 0

    Q = []

    for index_row, row in enumerate(graph):
        for index_col, col in enumerate(row):
            v = str(index_row) + ',' +  str(index_col)
            if v != source:
                dist[v] = 1000000
            Q.append(v)

    while Q:
        v = find_low_value(dist, Q)
        Q.remove(v)
        index_row = int(v.split(',')[0])
        index_col = int(v.split(',')[1])
        
        neighboor = ""
        alt = 0


        if index_col != len(graph[index_row]) - 1:
            neighboor = str(index_row) + ',' + str(index_col + 1)
            alt = dist[v] + graph[int(neighboor.split(',')[0])][int(neighboor.split(',')[1])]
            if alt < dist[neighboor]:
                dist[neighboor] = alt
        
        
        if index_row != len(graph) - 1:
            neighboor = str(index_row + 1) + ',' + str(index_col)
            alt = dist[v] + graph[int(neighboor.split(',')[0])][int(neighboor.split(',')[1])]
            if alt < dist[neighboor]:
                dist[neighboor] = alt

        '''if len(Q) % 50 == 0:
            print(len(Q))'''

    return dist


def find_low_value(dist, Q):
    lowest = 100000000000000000000000
    key = ""
    for _key in Q:
        if dist[_key] < lowest:
            lowest = dist[_key]
            key = _key
    return key


def main():
    start = perf_counter()
    data = open_file()
    
    # my function here
    # part1(data)
    part2(data)

    # not: 
    # 2845 (too high)
    # 2844 (too high)
    # correct (2838)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()