with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day6_input.txt", "r") as f:
    line = list(f.readline())
    
print(line)

def test (chars_list):
  test_set = set(chars_list)
  if len(test_set) == 14:
    return True
#get first 4 chars of line
chars_list = line[0:14]
test(chars_list)
#create set from start_chars and check it's length
index = 0
for char in line:
  chars_list.pop(0)
  chars_list.append(char)
  index += 1
  if test(chars_list):
    print(char)
    print(index)
    break
  
