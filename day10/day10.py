from time import perf_counter
from typing import List

def open_file():
    l = []
    with open('input10.txt') as f:
        lines = f.readlines()
        for line in lines:
            l.append(line.split('\n')[0])
    return l 


def remove_corrupted_lines(data):

    opening_symbols = "([{<"
    symbol_mapper = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_mapper = {")": 3, "]": 57, "}": 1197, ">" : 25137}
    syntax_score = 0
    
    non_currupt_lines = []

    for line in data:
        expected_closing = []
        line_score = 0
        for index, symbol in enumerate(line):
            if(symbol in opening_symbols):
                expected_closing.append(symbol_mapper[symbol])
            else:
                if(expected_closing[-1] == symbol):
                    del expected_closing[-1]
                else:
                    line_score += score_mapper[symbol]
                    syntax_score += score_mapper[symbol]
                    del expected_closing[-1]
        if(line_score == 0): non_currupt_lines.append(expected_closing)

    #print(syntax_score)
    return non_currupt_lines


def get_score_for_incomplete_lines(expected_closing):
    score_mapper = {")": 1, "]": 2, "}": 3, ">": 4}
    total_scores = [0] * len(expected_closing)
    
    for index, line in enumerate(expected_closing):
        line.reverse()
        for symbol in line:
            total_scores[index] = total_scores[index] * 5 + score_mapper[symbol]
            
    print(sorted(total_scores)[len(total_scores) // 2])



def main():
    start = perf_counter()
    data = open_file()
    
    # my function here
    expected_closing = remove_corrupted_lines(data)
    get_score_for_incomplete_lines(expected_closing)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()