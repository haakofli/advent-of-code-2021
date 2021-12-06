import numpy as np

def open_file():
    instructions = []
    with open('input5.txt') as f:
        lines = f.readlines()
        for line in lines:
            x = line.rstrip().split(' ')
            del x[1]
            for index, value in enumerate(x):
                x[index] = value.split(',')
            for i in x:
                i[0] = int(i[0])
                i[1] = int(i[1])

            instructions.append(x)
    return instructions 




def create_board(lines):
    # create 1000 x 1000 board
    board = np.ones((1000,1000)) 
    count = 0
    for line in lines:
        coords = find_line_coords(line)      
        if(len(coords) != 0):
            for i in coords:
                board[i[0]][i[1]] += 1
                if(board[i[0]][i[1]] == 3):
                    count += 1
    print(count)


# param line = [['x1','y1'],['x2','y2']]
def find_line_coords(line):
    coords = []
    if(line[0][0] == line[1][0]):
        r = abs(line[0][1] - line[1][1])
        for i in range(r+1):
            if(line[0][1] > line[1][1]):
                coords.append([line[0][0], line[0][1] - i])
            else:
                coords.append([line[0][0], line[1][1] - i])

    elif(line[0][1] == line[1][1]):
        r = abs(line[0][0] - line[1][0])
        for i in range(r+1):
            if(line[0][0] > line[1][0]):
                coords.append([line[0][0] - i, line[0][1]])
            else:
                coords.append([line[1][0] - i, line[0][1]])   

    elif(abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1])):
        r = abs(line[0][0] - line[1][0])
        for i in range(r + 1):
            # 5,5 -> 2,8
            if(line[0][0] == line[0][1] and line[1][0] < line[1][1]):
                coords.append([line[0][0] - i, line[0][1] + i])
            
            # 5,5 -> 8,2
            elif(line[0][0] == line[0][1] and line[1][0] > line[1][1]):
                coords.append([line[0][0] + i, line[0][1] - i])

            # 2,8 -> 5,5
            elif(line[0][0] < line[0][1] and line[1][0] == line[1][1]):
                coords.append([line[0][0] + i, line[0][1] - i])

            # 8,2 -> 5,5
            elif(line[0][0] > line[0][1] and line[1][0] == line[1][1]):
                coords.append([line[0][0] - i, line[0][1] + i])

            # 9,7 -> 7,9
            elif(line[0][0] > line[1][0] and line[0][1] < line[1][1]):
                coords.append([line[0][0] - i, line[0][1] + i])
            
            # 7,9 -> 9,7
            elif(line[0][0] < line[1][0] and line[0][1] > line[1][1]):
                coords.append([line[0][0] + i, line[0][1] - i])
            
            # 7,9 -> 5,11
            else:
                # 3,3 -> 1,1    
                if(line[0][0] > line[1][0]):
                    coords.append([line[0][0] - i, line[0][1] - i])
                
                # 1,1 -> 3,3
                else:
                    coords.append([line[0][0] + i, line[0][1] + i])

    return coords


def main():
    lines = open_file()
    create_board(lines)
    #find_highest(lines)
    
    # not:
    # 19785
    
if __name__ == "__main__":
    main()