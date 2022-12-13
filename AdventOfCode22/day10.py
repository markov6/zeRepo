x_register = 1 
cycle = 1

values = []
screen = [[], [], [], [], [], []]



def draw_screen(cycle, x_register):
    sprite_positions = [x_register - 1, x_register, x_register + 1]
    if cycle in range(1, 41):
        if cycle -1 in sprite_positions:
            screen[0].append("#")
        else: 
            screen[0].append('.')
    elif cycle in range(41, 81):
        if cycle - 41 in sprite_positions:
            screen[1].append("#")
        else: 
            screen[1].append('.')
    elif cycle in range(81, 121):
        if cycle - 81 in sprite_positions:
            screen[2].append("#")
        else: 
            screen[2].append('.')
    elif cycle in range(121, 161):
        if cycle - 121 in sprite_positions:
            screen[3].append("#")
        else: 
            screen[3].append('.')
    elif cycle in range(161, 201):
        if cycle - 161 in sprite_positions:
            screen[4].append("#")
        else: 
            screen[4].append('.')
    elif cycle in range(201, 241):
        if cycle - 201 in sprite_positions:
            screen[5].append("#")
        else: 
            screen[5].append('.')


def check_cycle(value):
    global cycle
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        values.append(value)
    
with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day10_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "noop":
            draw_screen(cycle, x_register)
            cycle += 1
            check_cycle(x_register)
            continue    
        else:
            line = line.split(" ")
            instruction = line[0]
            draw_screen(cycle, x_register)
            cycle += 1
            check_cycle(x_register)
            value = int(line[1])
            draw_screen(cycle, x_register)
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

for row in screen:
    print("".join(row))
    