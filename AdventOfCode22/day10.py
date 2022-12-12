x_register = 1 
cycle = 0

values = []

def check_cycle(value):
    global cycle
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        values.append(value)
with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day10_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "noop":
            cycle += 1
            check_cycle(x_register)
            continue    
        else:
            line = line.split(" ")
            instruction = line[0]
            cycle += 1
            check_cycle(x_register)
            value = int(line[1])
            cycle += 1
            check_cycle(x_register) 
            x_register += value
        
print(values)

multiplier = 20 
result = 0
for item in values: 
    result += item * multiplier
    multiplier += 40
print(result)