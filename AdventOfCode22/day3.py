with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day3_input.txt", "r") as f:
    lines = f.read().splitlines()
  
letter_values = {}
for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start=27):
  letter_value = ord(char)
  letter_key = chr(letter_value)
  letter_values[letter_key] = i
  
for i, char in enumerate('abcdefghijklmnopqrstuvwxyz', start=1):
  letter_value = ord(char)
  letter_key = chr(letter_value)
  letter_values[letter_key] = i

def determine_priority(letter): 
  return(letter_values[letter])
  
result = 0
#split lines in subaraays of 3 elements

  
# for line in lines: 
#   #split the string in half 
#   length = len(line)
#   first_rucksack = line[:length//2]
#   second_rucksack = line[length//2:]
#   print(first_rucksack, second_rucksack)
#   #find matching pairs in both rucksacks
#   already_found = False
#   for letter in first_rucksack: 
#     if already_found:
#       break
#     elif letter in second_rucksack:
#       already_found = True
#       result += determine_priority(letter) 

groups = []
for i in range(0, len(lines), 3):
  group = lines[i:i+3]
  groups.append(group)
  
result = 0
for group in groups:
  letters1 = set(group[0])
  letters2 = set(group[1])
  letters3 = set(group[2])
  common_letter = list(letters1.intersection(letters2, letters3))[0]
  result += determine_priority(common_letter)

print(result)
