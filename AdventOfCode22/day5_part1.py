import traceback
import re

instruction_lines = [] #from time move 1 from 2 to 1 
chart_lines = [] #strigs containing positions of crates 

with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day5_input.txt", "r") as f:
    line = f.readline()
    move_instructions = False
    while line:
      if line == "\n":
        move_instructions = True
      if move_instructions:
        instruction_lines.append(line)
      else: 
        chart_lines.append(line)
      line = f.readline()
   
   
# print(chart_lines)
instruction_lines.pop(0) #first is a new line 
chart_lines.pop()  #remove last line from chart_lines


#     [D]    
# [N] [C]    
# [Z] [M] [P]

def print_chart(chart_lines):
  for line in chart_lines:
    print(line.replace("\n", ""))

print_chart(chart_lines)
number_of_columns = int(len(chart_lines[0]) / 4 ) #4 is the number of columns in the chart


reversed_chart_lines = chart_lines[::-1]


columns = ['header', []]
number_of_columns = int(len(chart_lines[0]) / 4 ) #4 is the number of columns in the chart

## create list with empty arrays for columns 
while number_of_columns > 1:
  columns.append([])
  number_of_columns -= 1

for line in reversed_chart_lines:
  index = 1
  column = 1
  while index < len(line):
    if line[index].isalpha():
      columns[column].append(line[index])
    column += 1
    index += 4


print(instruction_lines)

def move_crate(quantity,from_column, to_column, source_list):
  try:
    if quantity == 1:
      source_list[to_column].append(source_list[from_column].pop())
    else:
      temp_list = source_list[from_column][-quantity:]
      del source_list[from_column][-quantity:]
      source_list[to_column] += temp_list
  except Exception:
    (print("Error: ", traceback.format_exc()))
  
for instruction in instruction_lines: 
  numbers = re.findall(r"\d+", instruction)
  quantity = int(numbers[0])
  from_index = int(numbers[1])
  to_index = int(numbers[2])
  try:
    move_crate(quantity, from_index, to_index, columns)
  except Exception:
    print(traceback.format_exc())
  
result = ""
columns.pop(0) #remove header
for column in columns:
  result += column.pop()

print(result)