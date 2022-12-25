import numpy as np


points = []
with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day18_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(",")
        print(line)
        point = {
          "x": int(line[0]),
          "y": int(line[1]),
          "z": int(line[2]),
          "sides": 6,
          "front": True,
          "back": True,
          "left": True,
          "right": True,
          "top": True,
          "bottom": True,
        }
        points.append(point)


# for i in range(0,len(points)):
#     for j in range(i + 1, len(points)):
#         point = points[i]
#         other = points[j]
#         if point == other:
#             continue
#         distance = abs(point["x"] - other["x"]) + abs(point["y"] - other["y"]) + abs(point["z"] - other["z"])
#         if distance == 1:
#             point["sides"] -= 1
#             other["sides"] -= 1

# result = 0          
# for point in points:
#     result += point["sides"]

maxx = max(point["x"] for point in points)
maxy = max(point["y"] for point in points)
maxz = max(point["z"] for point in points)


allSpace = np.zeros((maxx + 2, maxy + 2, maxz + 2))

for point in points: 
    allSpace[point["x"]][point["y"]][point["z"]] = int(1000)
    print(point["x"], point["y"], point["z"])
    print(allSpace[point["x"]][point["y"]][point["z"]])
    
    
queue = [{"x": 0, "y": 0, "z": 0}]

while len(queue) > 0:
    current = queue.pop(0)
    
    if allSpace[current["x"]][current["y"]][current["z"]] != 0:
        continue
    
    allSpace[current["x"]][current["y"]][current["z"]] = 1
    
    neighbours = [
        {"x": current["x"] + 1, "y": current["y"], "z": current["z"]},
        {"x": current["x"] - 1, "y": current["y"], "z": current["z"]},
        {"x": current["x"], "y": current["y"] + 1, "z": current["z"]},
        {"x": current["x"], "y": current["y"] - 1, "z": current["z"]},
        {"x": current["x"], "y": current["y"], "z": current["z"] + 1},
        {"x": current["x"], "y": current["y"], "z": current["z"] - 1},
    ]
    
    for neighbour in neighbours:
        
        if neighbour["x"] < 0 or neighbour["x"] > maxx + 1 :
            continue
        
        if neighbour["y"] < 0 or neighbour["y"] > maxy + 1:
            continue
        
        if neighbour["z"] < 0 or neighbour["z"] > maxz + 1:
            continue
        
        if allSpace[neighbour["x"]][neighbour["y"]][neighbour["z"]] == 0:
            queue.append(neighbour)

zeroes = set()
for xindex in range(0, len(allSpace)):
    xplane = allSpace[xindex]
    for yindex in range(0, len(xplane)):
        yline = xplane[yindex]
        for zindex in range(0, len(yline)):
            zpoint = yline[zindex]
            if zpoint == 0:
                zeroes.add("{},{},{}".format(xindex, yindex, zindex))
                 
for i in range(0, len(points)):
    first = points[i]
    top = f"{first['x']},{first['y']},{first['z'] + 1}"
    if zeroes.__contains__(top):
        first["top"] = False
    bottom = f"{first['x']},{first['y']},{first['z'] - 1}"
    if zeroes.__contains__(bottom):
        first["bottom"] = False
    left = f"{first['x'] - 1},{first['y']},{first['z']}"
    if zeroes.__contains__(left):
        first["left"] = False
    right = f"{first['x'] + 1},{first['y']},{first['z']}"
    if zeroes.__contains__(right):
        first["right"] = False
    front = f"{first['x']},{first['y'] + 1},{first['z']}"
    if zeroes.__contains__(front):
        first["front"] = False
    back = f"{first['x']},{first['y'] - 1},{first['z']}"
    if zeroes.__contains__(back):
        first["back"] = False
    
    for j in range(i + 1, len(points)):
        second = points[j]
        
        if first["x"] == second["x"]:
            if first["y"] == second["y"]:
                if first["z"] - second["z"] == 1:
                    first["bottom"] = False
                    second["top"] = False
                elif first["z"] - second["z"] == -1:
                    first["top"] = False
                    second["bottom"] = False
            elif first["z"] == second["z"]:
                if first["y"] - second["y"] == 1:
                    first["back"] = False
                    second["front"] = False
                elif first["y"] - second["y"] == -1:
                    first["front"] = False
                    second["back"] = False
        elif first["y"] == second["y"]:
            if first["z"] == second["z"]:
                if first["x"] - second["x"] == 1:
                    first["left"] = False
                    second["right"] = False
                elif first["x"] - second["x"] == -1:
                    first["right"] = False
                    second["left"] = False
        
                           
        # if point == other:
        #     continue
        # distance = abs(point["x"] - other["x"]) + abs(point["y"] - other["y"]) + abs(point["z"] - other["z"])
        # if distance == 1:
        #     point["sides"] -= 1
        #     other["sides"] -= 1              
        
sum = 0
for point in points:
    for side in ["front", "back", "left", "right", "top", "bottom"]:
        if point[side]:
            sum += 1
print(sum)