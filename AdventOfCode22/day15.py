import re

input = []
with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day15_input.txt", "r") as f:
    lines = f.readlines()
    pattern = r"Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    for line in lines:
        line = line.strip()
        print(line)
        matches = re.findall(pattern, line)
        input_line = { 
            "location": {"x": int(matches[0][0]), "y": int(matches[0][1])},
            "beacon": {"x": int(matches[0][2]), "y": int(matches[0][3])}
        }
        input.append(input_line)

target_row = 2000000
covered = set()

for sensor in input:
    radius = abs(sensor["location"]["x"] - sensor["beacon"]["x"]) + abs(sensor["location"]["y"] - sensor["beacon"]["y"])
    if sensor["location"]["y"] + radius < target_row or sensor["location"]["y"] - radius > target_row:
        # print("Sensor at", sensor["location"], "is NOT in target row", target_row)  
        continue
    # print("Sensor at", sensor["location"], "is in target row", target_row, "with radius", radius) 
    row_distance = abs(sensor["location"]["y"] - target_row)
    reach = radius - row_distance
    
    for i in range(sensor["location"]["x"] - reach, sensor["location"]["x"] + reach + 1):
        covered.add(i)
    
for sensor in input:
    if sensor["beacon"]["y"] == target_row and covered.__contains__(sensor["beacon"]["x"]):
        covered.remove(sensor["beacon"]["x"])
    
print(len(covered))