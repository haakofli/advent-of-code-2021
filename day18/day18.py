from time import perf_counter
from typing import List
import ast
import itertools
import math

def open_file():
    l = []
    with open('test_input18.txt') as f:
        lines = f.readlines()
        for line in lines:
            l.append(line.split('\n')[0])
    return l 

def format_data(data):
    new_data = []
    for line in data:
        x = ast.literal_eval(line)
        new_data.append(x)
    return new_data


def part1(data):
    prev_line = []

    '''x = [[[[[9,8],1],2],3],4]
    print(x)
    prev_line = explode_list(x)
    print(prev_line)
    if prev_line == [[[[0,9],2],3],4]: print("Riktig!")
    else: print("Feil!")

    print("---------------------------------------")

    x = [7,[6,[5,[4,[3,2]]]]]
    print(x)
    prev_line = explode_list(x)
    print(prev_line)
    if prev_line == [7,[6,[5,[7,0]]]]: print("Riktig!")
    else: print("Feil!")

    print("---------------------------------------")

    x = [[6,[5,[4,[3,2]]]],1]
    print(x)
    prev_line = explode_list(x)
    print(prev_line)
    if prev_line == [[6,[5,[7,0]]],3]: print("Riktig!")
    else: print("Feil!")

    print("---------------------------------------")

    x = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
    print(x)
    prev_line = explode_list(x)
    print(prev_line)
    if prev_line == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]: print("Riktig!")
    else: print("Feil!")

    print("---------------------------------------")

    x = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
    print(x)
    prev_line = explode_list(x)
    print(prev_line)
    if prev_line == [[3,[2,[8,0]]],[9,[5,[7,0]]]]: print("Riktig!")
    else: print("Feil!")'''

    for index, line in enumerate(data):
        if prev_line == []: 
            prev_line = line
        else: 
            prev_line = add_lines(prev_line, line) 
            print("--------------------- One addition --------------------------")
            print(prev_line)
    
    # new_l = increment_first_element([[[4, 5], [2, 6]], [9, 5]], 3)
    # print(new_l)
    

    # x = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    # y = [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
    
    # prev_line = add_lines(x, y)
    # print(prev_line)

    #z = 13 / 2

    # print(int(z))
    # print(int(math.ceil(13/2)))
    '''for x in traverse(data):           
        if x > 9:
            print("h")'''

    #print(prev_line)
    # x = [[[[0, [5, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]], [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]]]
    # new_x = explode_list(x)
    #print(new_x)


def add_lines(pair_1, pair_2):
    new_line = [pair_1, pair_2]
    
    continue_to_reduce = True
    #print(new_line)
    while continue_to_reduce:   
        x = reduce_list(new_line)
        new_depth = depth(x)
        continue_to_reduce = False
        if new_depth < 5 and not should_split(x):
            continue_to_reduce = False
        else:
            new_line = x
        
    return new_line


def reduce_list(line):
    #print("----------------------------------------------------------")
    x = depth(line)
    if x > 4:
        #print("explode")
        #print(line)
        new_line = explode_list(line)
        #print(new_line)
        return new_line
    elif should_split(line):
        #print("split")
        #print(line)
        new_line, done = split_list(line)
        #print(new_line)
        return new_line
    return line



def explode_list(line):
    x = line

    # Find index and value of pair to explode
    index_explode_pair, explode_pair = find_explode_pair(x)
    
    # Find index and whether or not a value to the left exists
    index_of_value_to_the_left, exists_value_to_the_left = find_left_value(index_explode_pair)
    
    # Find index and whether or not a value to the right exists
    index_of_value_to_the_right, exists_value_to_the_right = find_right_value(explode_pair, x)
    
    # increase left value with first value in explode pair
    if exists_value_to_the_left:
        y = index_of_value_to_the_left
        if len(index_of_value_to_the_left) == 1:
            x[y[0]] += explode_pair[0]
        elif len(index_of_value_to_the_left) == 2:
            x[y[0]][y[1]] += explode_pair[0]
        elif len(index_of_value_to_the_left) == 3:
            x[y[0]][y[1]][y[2]] += explode_pair[0]
        elif len(index_of_value_to_the_left) == 4:
            print("-------------")
            print(y)
            print(explode_pair)
            print(x[0][0][0][0])
            print("---------------")
            x[y[0]][y[1]][y[2]][y[3]] += explode_pair[0]
        
    # increase right value with second value in explode pair
    if exists_value_to_the_right:
        y = index_of_value_to_the_right
        if len(index_of_value_to_the_right) == 1:
            x[y[0]] += explode_pair[1]
        elif len(index_of_value_to_the_right) == 2:
            x[y[0]][y[1]] += explode_pair[1]
        elif len(index_of_value_to_the_right) == 3:
            x[y[0]][y[1]][y[2]] += explode_pair[1]
        elif len(index_of_value_to_the_right) == 4:
            x[y[0]][y[1]][y[2]][y[3]] += explode_pair[1]

    # set explode pair to 0
    x[index_explode_pair[0]][index_explode_pair[1]][index_explode_pair[2]][index_explode_pair[3]] = 0

    return x

def find_explode_pair(line):
    for i_1, v_1 in enumerate(line):
        if depth(v_1) >= 4:
            for i_2, v_2 in enumerate(v_1):
                if depth(v_2) >= 3:
                    for i_3, v_3 in enumerate(v_2):
                        if depth(v_3) >= 2:
                            for i_4, v_4 in enumerate(v_3):
                                if depth(v_4) == 1:
                                    index = [i_1, i_2, i_3, i_4]
                                    pair = v_4
                                    return index, pair                    
    return -1, -1
        
def find_left_value(index_list: List[int]):
    new_index_list = index_list.copy()
    new_index_list.reverse()
    
    for i, index in enumerate(new_index_list):
        if index > 0:
            new_index_list[i] -= 1
            new_index_list.reverse()
            return new_index_list, True
    return index_list, False
        
def find_right_value(explode_pair, line):
    start_to_look_for_right_value = False
    for i_1, v_1 in enumerate(line):
        # sjekk if int og start look == True
        if type(v_1) is int and start_to_look_for_right_value:
            return [i_1], True
        
        if type(v_1) is list:
            for i_2, v_2 in enumerate(v_1):
                # sjekk if int og start look == True
                if type(v_2) is int and start_to_look_for_right_value:
                    return [i_1, i_2], True

                if type(v_2) is list:
                    for i_3, v_3 in enumerate(v_2):
                        if type(v_3) is int and start_to_look_for_right_value:
                            return [i_1, i_2, i_3], True
                        # sjekk if int og start look == True
                        
                        if type(v_3) is list:
                            for i_4, v_4 in enumerate(v_3):
                                if type(v_4) is int and start_to_look_for_right_value:
                                    return [i_1, i_2, i_3, i_4], True
                                # sjekk if int og start look == True

                                elif type(v_4) is list and start_to_look_for_right_value:
                                    return [i_1, i_2, i_3, i_4, 0], True

                                if v_4 == explode_pair:
                                    start_to_look_for_right_value = True
                                    print(v_4)
                                
    return [], False

'''
def explode_list(line):
    new_line = line
    index_prev = []

    value_for_next = -1

    incremented_last_element = False
    for i_1, l_1 in enumerate(new_line):
        if depth(l_1) > 0:
            for i_2, l_2 in enumerate(l_1):
                if depth(l_2) > 0:
                    for i_3, l_3 in enumerate(l_2):
                        if type(l_3) is not int:
                            for i_4, l_4 in enumerate(l_3):
                                if type(l_4) is int and value_for_next != -1:
                                    new_line[i_1][i_2][i_3][i_4] += value_for_next
                                    return new_line
                                
                                if type(l_4) is not int:
                                        print(l_4)
                                        print(l_4[1])
                                        print("val", value_for_next)
                                    
                                        
                                        if value_for_next != -1:
                                            print(l_4)
                                            print(value_for_next)
                                            new_l_4 = increment_first_element(l_4, value_for_next)
                                            new_line[i_1][i_2][i_3][i_4] = new_l_4
                                            return new_line
                                            

                                        # THIS IS DEPTH 4!!! 
                                        value_for_next = l_4[1]

                                        if len(index_prev) == 1:
                                            new_line[index_prev[0]] += l_4[0]
                                        elif len(index_prev) == 2:
                                            new_line[index_prev[0]][index_prev[1]] += l_4[0]
                                        elif len(index_prev) == 3:
                                            new_line[index_prev[0]][index_prev[1]][index_prev[2]] += l_4[0]
                                        elif len(index_prev) == 4:
                                            new_line[index_prev[0]][index_prev[1]][index_prev[2]][index_prev[3]] += l_4[0]

                                        new_line[i_1][i_2][i_3][i_4] = 0
                                        

                                else:
                                    index_prev = [i_1, i_2, i_3, i_4]
                        else:
                            index_prev = [i_1, i_2, i_3]
                            if value_for_next != -1:
                                new_line[i_1][i_2][i_3] += value_for_next
                                return new_line
                
                else:
                    index_prev = [i_1, i_2]
                    if value_for_next != -1:
                        new_line[i_1][i_2] += value_for_next
                        return new_line

        else:
            index_prev = [i_1]
            if value_for_next != -1:
                new_line[i_1] += value_for_next
                return new_line
            


    return line
'''
def increment_first_element(l_4, value_for_next):
    new_l_4 = l_4
    
    if type(l_4) is int:
        new_l_4 += value_for_next
    else:
        for index, l in enumerate(new_l_4):
            if index == 0:
                if type(l) is int:
                    new_l_4[index] += value_for_next
                else:
                    new_l_4[index] = increment_first_element(l, value_for_next)
    return l_4


'''
def explode_list(line):
    new_line = line

    increment_next_value = 0

    last_checked_element = []

    already_added_last_checked = False
    print("--------------------------")
    print(new_line)
    for i, l in enumerate(line):
        
        # -------------------------
        if type(l) is not int:
            for i_4, l_4 in enumerate(l):
                if increment_next_value != 0 and type(l_4) is int:
                    new_line[i][i_4] += increment_next_value
                    increment_next_value = 0
                    return new_line
        # -------------------------
        
        # Element to the left of the explosion
        if type(l) is int and not already_added_last_checked:
            last_checked_element = [i, l]

        x = depth(l)
        if x == 4:
            for i_1, l_1 in enumerate(l):
                
                # -------------------------
                if type(l_1) is not int:
                    for i_4, l_4 in enumerate(l_1):
                        if increment_next_value != 0 and type(l_4) is int:
                            new_line[i][i_1][i_4] += increment_next_value
                            increment_next_value = 0
                            return new_line
                # -------------------------
                
                # Element to the left of the explosion
                if type(l_1) is int and not already_added_last_checked:
                    last_checked_element = [i, i_1, l_1]

                y = depth(l_1)
                if y == 3:
                    for i_2, l_2 in enumerate(l_1):
                        
                        # -------------------------
                        if type(l_2) is not int:
                            for i_4, l_4 in enumerate(l_2):
                                if increment_next_value != 0 and type(l_4) is int:
                                    new_line[i][i_1][i_2][i_4] += increment_next_value
                                    increment_next_value = 0
                                    return new_line
                        # -------------------------
                        
                        # Element to the left of the explosion
                        if type(l_2) is int and not already_added_last_checked:
                            last_checked_element = [i, i_1, i_2, l_2]

                        z = depth(l_2)
                        if z == 2:
                            for i_3, l_3 in enumerate(l_2):

                                # ------------------------------
                                if type(l_3) is not int:
                                    for i_4, l_4 in enumerate(l_3):
                                        if increment_next_value != 0 and type(l_4) is int:
                                            new_line[i][i_1][i_2][i_3][i_4] += increment_next_value
                                            increment_next_value = 0
                                            return new_line
                                # --------------------------------- 
                                
                                # Element to the left of the explosion
                                if type(l_3) is int and not already_added_last_checked:
                                    last_checked_element = [i, i_1, i_2, i_3, l_3]
                                elif type(l_3) is not int and not already_added_last_checked:
                                    for i_4, l_4 in enumerate(l_3):
                                        last_checked_element = [i, i_1, i_2, i_3, i_4, l_4]
                                
                                # Increase value to the left
                                if last_checked_element != [] and not already_added_last_checked:
                                    value = 0
                                    if type(l_3) is int:
                                        value = l_3
                                    else:
                                        value = l_3[0]

                                    _i = last_checked_element[0]
                                    if len(last_checked_element) == 2:
                                        
                                        new_line[_i] += value
                                    elif len(last_checked_element) == 3:
                                        _i_2 = last_checked_element[1]
                                        new_line[_i][_i_2] = new_line[_i][_i_2] + value
                                    elif len(last_checked_element) == 4:
                                        _i_2 = last_checked_element[1]
                                        _i_3 = last_checked_element[2]
                                        new_line[_i][_i_2][_i_3] = new_line[_i][_i_2][_i_3] + value
                                    elif len(last_checked_element) == 5:
                                        _i_2 = last_checked_element[1]
                                        _i_3 = last_checked_element[2]
                                        _i_4 = last_checked_element[3]
                                        new_line[_i][_i_2][_i_3][_i_4] = new_line[_i][_i_2][_i_3][_i_4] + value
                                    elif len(last_checked_element) == 6:
                                        _i_2 = last_checked_element[1]
                                        _i_3 = last_checked_element[2]
                                        _i_4 = last_checked_element[3]
                                        _i_5 = last_checked_element[4]
                                        new_line[_i][_i_2][_i_3][_i_4][_i_5] = new_line[_i][_i_2][_i_3][_i_4][_i_5] + value
                                    print("last checked: ", value)
                                    already_added_last_checked = True
                                    last_checked_element = 0
                                    
                                    
                                if not already_added_last_checked and increment_next_value != 0:
                                    try:
                                        
                                        
                                        if type(l_3) is int: 
                                            new_line[i][i_1][i_2][i_3-1][1] += l_3
                                        else:
                                            new_line[i][i_1][i_2][i_3-1][1] += l_3[0]
                                    except:
                                        pass
                                    try:
                                        if type(l_3) is int: 
                                            new_line[i][i_1][i_2-1][1] += l_3
                                        else:
                                            new_line[i][i_1][i_2-1][1] += l_3[0]
                                    except:
                                        pass
                                    try:
                                        if type(l_3) is int: 
                                            new_line[i][i_1-1][1] += l_3
                                        else:
                                            new_line[i][i_1-1][1] += l_3[0]
                                    except:
                                        pass
                                    try:
                                        if type(l_3) is int: 
                                            new_line[i-1][1] += l_3
                                        else:
                                            new_line[i-1][1] += l_3[0]
                                    except:
                                        pass
                                    already_added_last_checked = True


                                if type(l_3) is not int:
                                    increment_next_value = new_line[i][i_1][i_2][i_3][1]
                                    
                                new_line[i][i_1][i_2][i_3] = 0

                               
                                
                                
                                
    return new_line
'''

def split_list(line):
    done = False
    new_line = line
    for index, l in enumerate(new_line):
        if type(l) is int:
            if l > 9:
                new_line[index] = [int(l/2), int(math.ceil(l/2))]
                return new_line, True
        else:
            new_line[index], done = split_list(l)
            if done:
                return new_line, done

    return new_line, done

def should_split(line):
    for value in traverse(line):
        if value > 9:
            return True
    return False

def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o                       

def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0


def main():
    start = perf_counter()
    data = open_file()
    

    # my function here
    new_data = format_data(data)
    part1(new_data)



    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()