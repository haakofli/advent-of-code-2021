from time import perf_counter
from typing import Counter, List

def open_file():
    p_template = ""
    p_rules = []
    append_to_rules = False
    with open('input14.txt') as f:
        lines = f.readlines()
        
        for line in lines:
            x = line.split('\n')[0]
            if x == '': 
                append_to_rules = True
            else:
                if append_to_rules: p_rules.append(x.split(' -> '))
                else: p_template = x
            
    return p_rules, p_template

    

# PART 2
def part2(p_rules, p_template):
    count_pairs_prev = {}
    count_pairs = {}
    length_polymer = len(p_template)
    
    for i in range(len(p_template)-1):
        if p_template[i] + p_template[i+1] in count_pairs_prev:
            count_pairs_prev[p_template[i] + p_template[i+1]] += 1
        else:
            count_pairs_prev[p_template[i] + p_template[i+1]] = 1
    
    for iteration in range(1,41):
        for pair in count_pairs_prev:
            if count_pairs_prev[pair] != 0:
                for rule in p_rules:
                    if rule[0] == pair:
                        if pair[0]+rule[1] in count_pairs:
                            count_pairs[pair[0]+rule[1]] += count_pairs_prev[pair]
                        else:
                            count_pairs[pair[0]+rule[1]] = count_pairs_prev[pair]

                        if rule[1]+pair[1] in count_pairs:
                            count_pairs[rule[1]+pair[1]] += count_pairs_prev[pair]
                        else:
                            count_pairs[rule[1]+pair[1]] = count_pairs_prev[pair]
        
        count_pairs_prev = count_pairs
        count_pairs = {}
        length_polymer = (length_polymer * 2) - 1
        
    unique_chars = find_unique_chars(count_pairs_prev)
    
    occurences = find_occurances(count_pairs_prev, unique_chars)
    
    print(f"Answer to part 2: {int(max(occurences) - min(occurences))}")
    
def find_occurances(count_pairs_prev, unique_chars):
    occurences = []
    for char in unique_chars:
        count = count_for_char(count_pairs_prev, char)
        occurences.append(count / 2)
    return occurences

def find_unique_chars(count_pairs_prev):
    unique_chars = []
    for key in count_pairs_prev:
        for char in key:
            if char not in unique_chars:
                unique_chars.append(char)
    return unique_chars

def count_for_char(count_pairs_prev, char):
    count = 0
    for pair in count_pairs_prev:
        for c in pair:
            if char == c:
                count += count_pairs_prev[pair]
    return count




# PART 1
def part1(p_rules, p_template):
    polymer = p_template
    for i in range(10):
        polymer = polymerization_step(p_rules, polymer)
    find_most_and_least_common(polymer)

def polymerization_step(p_rules, polymer):
    new_polymer = ""
    for i in range(len(polymer) - 1):
        pair = polymer[i] + polymer[i+1]
        for rule in p_rules:
            if pair == rule[0]: 
                pair = pair[0] + rule[1]
                break
        new_polymer += pair    
    new_polymer += polymer[-1]
    return new_polymer    

def find_most_and_least_common(polymer):
    max_count = 0
    min_count = 100000000000000
    for char in polymer:
        if polymer.count(char) > max_count: max_count = polymer.count(char)
        if polymer.count(char) < min_count: min_count = polymer.count(char)

    print(f"Answer to part1: {max_count - min_count}")
    

def main():
    start = perf_counter()
    p_rules, p_template = open_file()

    # my function here
    part1(p_rules, p_template)
    part2(p_rules, p_template)


    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()