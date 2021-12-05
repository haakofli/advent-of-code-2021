def open_file():
    data = []
    sequence = []
    boards = []
    with open('input4.txt') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.rstrip("\n"))
    sequence = data[0]
    del data[0]
    del data[0]
    
    board = []
    for x in data:
        row = x.split(' ')
        formated_row = []
        if(row == ['']):
            boards.append(board)
            board = []
        else:
            for i in row:
                if(i != ""):
                    formated_row.append(i)
            board.append(formated_row)


    
    return sequence.split(','), boards




def play_bingo(sequence, boards):

    updated_boards = boards
    bingo = False

    bingo_index = []
    
    print(len(updated_boards))
    for char in sequence:
        bingo = False
        
        for index, board in enumerate(updated_boards):
            bingo = False
            if(index_already_bingo(index, bingo_index)): continue
            
            new_board = remove_char_from_board(char, board)
        
            updated_boards[index] = new_board
           
            bingo = look_for_bingo(new_board)
            if(bingo): 
                bingo_index.append(index)
    
            

def index_already_bingo(index, list_of_index):
    for x in list_of_index:
        if(x == index):
            return True
    return False


def look_for_bingo(board):
    for i in board:
        if(i[0] == 'x'):
            bingo_horizontally = check_bingo_horizontally(i)
            if(bingo_horizontally):
                print("BINGO horisontalt")
                return True


    for index, value in enumerate(board[0]):
        if(value == 'x'):
            bingo_vertically = check_for_bingo_vertically(board, index)
            if(bingo_vertically):
                print("BINGO vertikalt")
                return True
    
    return False
                


def check_bingo_horizontally(row):
    for value in row:
        if(value != 'x'):
            return False
    return True


def check_for_bingo_vertically(board, index):
    for i in board:
        if(i[index] != 'x'):
            return False
    return True
    




def remove_char_from_board(char, board):
    new_board = board
    for row_index, row in enumerate(board):
        for char_in_row_index, char_in_row in enumerate(row):
            if(char_in_row == char):
                new_board[row_index][char_in_row_index] = 'x'
                bingo = look_for_bingo(new_board)
                if(bingo):
                    sum = get_sum(new_board)
                    #print("sum = ", sum)
                    #print("char = " , char)
                    print("result = " , sum * int(char))
                    #print(new_board)
    
    return new_board
        

def get_sum(board):
    sum = 0
    for row in board:
        for element in row:
            if(element != 'x'):
                sum += int(element)

    return sum




def main():
    sequence, boards = open_file()
    play_bingo(sequence, boards)
    
if __name__ == "__main__":
    main()