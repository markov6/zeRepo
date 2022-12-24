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
        }
        points.append(point)


for i in range(0,len(points)):
    for j in range(i + 1, len(points)):
        point = points[i]
        other = points[j]
        if point == other:
            continue
        distance = abs(point["x"] - other["x"]) + abs(point["y"] - other["y"]) + abs(point["z"] - other["z"])
        if distance == 1:
            point["sides"] -= 1
            other["sides"] -= 1

result = 0          
for point in points:
    result += point["sides"]

print(result)