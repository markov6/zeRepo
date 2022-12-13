list1 = False
list2 = False
pair_counter = 1

def compare_values(value1, value2):
    if isinstance(value1, int) and isinstance(value2, int):
        if value1 < value2:
            return -1
        elif value1 == value2:
            return 0
        else:
            return 1
    elif isinstance(value1, list) and isinstance(value2, list):
        i = 0
        while i < len(value1) and i < len(value2):
            c = compare_values(value1[i], value2[i])
            if c == -1:
                return -1
            if c == 1:
                return 1
            i += 1
        if i == len(value1) and i < len(value2):
            return -1
        elif i == len(value2) and i < len(value1):
            return 1
        else:
            return 0
    elif isinstance(value1, int) and isinstance(value2, list):
        return compare_values([value1], value2)
    else:
        return compare_values(value1, [value2])


matching_pairs = []
with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day13_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            list1 = False
            list2 = False
            pair_counter += 1
            continue
        if not isinstance(list1, list):
            list1 = eval(line)
        elif not isinstance(list2, list):
            list2 = eval(line)
            result = compare_values(list1, list2)
            if result == - 1:
                matching_pairs.append(pair_counter)
            
print(matching_pairs)
print(sum(matching_pairs))