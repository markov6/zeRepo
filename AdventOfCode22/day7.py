def handle_command(params):
    global current_tree_key
    if params[0] == "cd":
        if params[1] == "..":
            current_dir.pop()
        else:
            current_dir.append(params[1])
            if params[1] not in tree:
                tree[params[1]] = []          
    elif params[0] == "cd":
        print("Handle cd")
    elif params[0] == "ls":
        string_key = current_dir[-1]
        print(string_key)
        current_tree_key = string_key
    else:
        print("Handle unknown command")


current_dir = []

tree = {}

current_tree_key = ""
# tree = {
#     'A': ['B', 'C'],
#     'B': [],
#     'C': [],
# }

with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day7_input.txt", "r") as f:
    lines = f.readlines()
    
for line in lines:
    line = line.strip().split(" ")
    print(line)
    if line[0] == "$":
        params = line[1:]
        handle_command(params)
        print("Handle command")
    elif line[0] == "dir":
        tree[current_tree_key].append(line[1])
    else:
        file_dict = {
            "name": line[1],
            "size": line[0]
        }
        tree[current_tree_key].append(file_dict)
    
current_dir = []

print(tree)
result_list = {}
def calc_dir_size(dir, tree):
    sizes_dict = {}
    size = 0
    for item in tree[dir]:
        if type(item) == str and item not in sizes_dict:
            size = calc_dir_size(item, tree)
        elif type(item) == str and item in sizes_dict:
            size += sizes_dict[item]
        else:
            size += int(item["size"])
    result_list[dir] = size
    return size

def calc_tree_size(tree):
    total_size = 0
    for item in tree:
        print(item)
        calc_dir_size(item, tree)
    #     if type(item) == str:
    #         total_size += 1
    #     else:
    #         total_size += int(item["size"])
    # return total_size


calc_dir_size("/" , tree)
print(result_list)

total = 0
for dir in result_list:
    if result_list[dir] < 100000:
        total += result_list[dir]

print(total)