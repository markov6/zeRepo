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

class FsItem:
    def __init__(self, name):
        self.name = name
        
    def size():
        return 0
      
class RootFolder(FsItem):
    def __init__(self, name):
        self.name = name   
        self.children = []
        self.__name = "/" 
    
    def size(self):
        return sum([child.size() for child in self.children])
        
class Folder(FsItem):
    def __init__(self, name, parent):   
        self.name = name
        self.parent = parent
        self.children = []
    
    def size(self):
        return sum([child.size() for child in self.children])


class File(FsItem):
    def __init__(self, name, size, parent):
        self.name = name
        self.__size = size
         
    def size(self):
        return self.__size


root = RootFolder("root")
current_folder = root
print(root)



with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day7_input.txt", "r") as f:
    lines = f.readlines()
    
for line in lines:
    line = line.strip()
    print(line)
    if line == "$ cd /" or line == "$ ls":
        continue
    if line == "$ ls":
        continue
    if line == "$ cd ..":
        if isinstance(current_folder, RootFolder):
            raise Exception("Cannot go up from root")
        else: 
            current_folder = current_folder.parent
            continue
    if line.startswith("$ cd"):
        folder_name = line.split(" ")[-1]
        try:
            folder_index = [folder.name for folder in current_folder.children].index(folder_name)
        except ValueError:
            folder_index = None
        if folder_index:
            folder = current_folder.children[folder_index]
        else:
            folder = Folder(folder_name, current_folder)
            current_folder.children.append(folder)
        current_folder = folder
    else:
        #process file 
        parts = line.split(" ")
        file_name = parts[1]
        try:
            file_index = [item.name for item in current_folder.children].index(file_name)
        except ValueError:
            file_index = None
        if not file_index:
            if parts[0] == "dir":
                child = Folder(file_name, current_folder)
                current_folder.children.append(child)
            else:
                size = int(parts[0])
                child = File(file_name, size, current_folder)
                current_folder.children.append(child)


used_space = root.size()
total_space = 70000000
needed_space = 30000000
free_space = total_space - used_space
required_size = needed_space - free_space
print(used_space, needed_space)

queue = [root]
delete_candidates = []

while len(queue) > 0:
    item = queue.pop(0)
    size = item.size()
    if (size > required_size):
        delete_candidates.append(size)
    for child in item.children:
        if isinstance(child, Folder):
            queue.append(child)


print(min(delete_candidates))
# print(tree)
# result_list = {}
# def calc_dir_size(dir, tree):
#     sizes_dict = {}
#     size = 0
#     for item in tree[dir]:
#         if type(item) == str and item not in sizes_dict:
#             size = calc_dir_size(item, tree)
#         elif type(item) == str and item in sizes_dict:
#             size += sizes_dict[item]
#         else:
#             size += int(item["size"])
#     result_list[dir] = size
#     return size

# def calc_tree_size(tree):
#     total_size = 0
#     for item in tree:
#         print(item)
#         calc_dir_size(item, tree)
#     #     if type(item) == str:
#     #         total_size += 1
#     #     else:
#     #         total_size += int(item["size"])
#     # return total_size


# calc_dir_size("/" , tree)
# print(result_list)

# total = 0
# for dir in result_list:
#     if result_list[dir] < 100000:
#         total += result_list[dir]

# print(total)