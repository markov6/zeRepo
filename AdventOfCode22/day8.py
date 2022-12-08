forrest = []

with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day8_input.txt", "r") as f:
    lines = f.readlines()
    
for line in lines: 
    line = line.strip()
    digits = []
    for char in line:
        digits.append(char)
    # split after each digit
    forrest.append(digits)
    print(digits)

print(forrest)

def is_edge(i, j, forrest):
    if i == 0 or j == 0 or i == len(forrest) - 1 or j == len(forrest[0]) - 1:
        return True
    return False

def check_surrounding(i, j, value):
    surrounding_left = []
    surrounding_right = []
    surrounding_top = []
    surrounding_bottom = []
  
    # add all elements to the left of the tree
    counter_left = j - 1
    counter_right = j + 1
    counter_top = i - 1
    counter_bottom = i + 1
    while counter_left >= 0:
        surrounding_left.append(forrest[i][counter_left])
        counter_left -= 1
    # add all elements to the right of the tree
    while counter_right < len(forrest[0]):
        surrounding_right.append(forrest[i][counter_right])
        counter_right += 1
    # add all elements to the top of the tree
    while counter_top >= 0:
        surrounding_top.append(forrest[counter_top][j])
        counter_top -= 1
    # add all elements to the bottom of the tree
    while counter_bottom < len(forrest):
        surrounding_bottom.append(forrest[counter_bottom][j])
        counter_bottom += 1
    
    # merge the 4 lists into one
    surrounding_trees = [surrounding_left, surrounding_right, surrounding_top, surrounding_bottom]
    for line_of_sight in surrounding_trees:
        if all(tree < value for tree in line_of_sight):
            return True
    return False 


visible = 0
for i, row in enumerate(forrest):
    for j, val in enumerate(row): # values is the value at forrest[i][j]
        if is_edge(i, j, forrest):
            visible += 1
            print(f'The element at index [{i}, {j}] is on the edge and has a value of {val}')
        else:
            if check_surrounding(i, j, val):
                visible += 1
        
print(visible)