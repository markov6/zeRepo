import numpy as np 
import matplotlib.pyplot as plt

matrix = np.full((1000, 1000), ".")
matrix[0][500] = "+"

R = set()
with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day14_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        coordinates = line.split("->")
        index = 0
        previous_x = None
        previous_y = None
        prev = None
        for point in line.split("->"):
            x,y = point.split(",")
            x,y = int(x), int(y)
            if prev is not None:
                dx = x-prev[0]
                dy = y-prev[1]
                len_ = max(abs(dx), abs(dy))
                # print(len_, dx, dy)
                for i in range(len_ + 1):
                    xx = prev[0] + i * (1 if dx > 0 else (-1 if dx < 0 else 0))
                    yy = prev[1] + i * (1 if dy > 0 else (-1 if dy < 0 else 0))
                    R.add((xx, yy))
            prev = (x,y)
            # print(line, point, sorted(R))
            
floor = 2 + max(r[1] for r in R)
for x in range(-10000, 10000):
    R.add((x, floor))
            
for t in range(1000000):
    rock = (500,0)
    while True:
        # if rock[1] >= floor:
        #     break
        if (rock[0], rock[1] + 1) not in R:
            rock = (rock[0], rock[1] + 1)
        elif (rock[0] - 1, rock[1] + 1) not in R:
            rock = (rock[0] - 1, rock[1] + 1)
        elif (rock[0] + 1, rock[1] + 1) not in R:
            rock = (rock[0] + 1, rock[1] + 1)
        else:
            break
    if rock == (500,0):
        assert False, t
    R.add(rock)
            
    #         matrix[y][x] = "#"
    #         index += 1
    #         if previous_x is not None and previous_y is not None:
    #             if x > previous_x:
    #                 for i in range(previous_x, x):
    #                     matrix[y][i] = "#"
    #             elif x < previous_x:
    #                 for i in range(x, previous_x):
    #                     matrix[y][i] = "#"
    #             elif y > previous_y:
    #                 for i in range(previous_y, y):
    #                     matrix[i][x] = "#"
    #             elif y < previous_y:
    #                 for i in range(y, previous_y):
    #                     matrix[i][x] = "#"
    #         previous_x = x
    #         previous_y = y
    
    # print(coordinates)


# for t in range(1e6):
#     rock = (500, 0)
#     while True:
        