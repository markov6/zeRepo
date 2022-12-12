center = {"x": 3000, "y": 3000}
visited = {}

knots = [{"x": 0, "y": 0}, {"x": 0, "y": 0},
         {"x": 0, "y": 0}, {"x": 0, "y": 0},
         {"x": 0, "y": 0}, {"x": 0, "y": 0},
         {"x": 0, "y": 0}, {"x": 0, "y": 0},
         {"x": 0, "y": 0}, {"x": 0, "y": 0},]
head_x = center["x"]
head_y = center["y"]
tail_x = center["x"]
tail_y = center["y"]


def followKnot(head, tail):
    # move tail
    # if head is touching tail don't move tail
    if abs(head["x"] - tail["x"]) <= 1 and abs(head["y"] - tail["y"]) <= 1:
        return
    # else move the tail
    if head["y"] > tail["y"]:
        tail["y"] += 1
    elif head["y"] < tail["y"]:
        tail["y"] -= 1  

    if head["x"] > tail["x"]:
        tail["x"] += 1
    elif head["x"] < tail["x"]:
        tail["x"] -= 1         




with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day9_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(" ")
        direction = line[0]
        distance = line[1]

        for step in range(int(distance)): 
            head = knots[0]
            # move head
            if direction == "R":
                head["x"] += 1
                # continue
            elif direction == "U":
                head["y"] += 1
                # continue
            elif direction == "L":
                head["x"] -= 1
                # continue
            elif direction == "D":
                head["y"] -= 1
                # continue
            else:
                raise Exception("Invalid direction")
                
            for i in range(1, len(knots)):
                followKnot(knots[i-1], knots[i])
                
            tail = knots[-1]
            if tail["y"] not in visited:
                visited[tail["y"]] = {tail["x"]}
            else:
                visited[tail["y"]].add(tail["x"])
    #   move_head(line[0], line[1])


# visited = 0
# for row in matrix:
#     for element in row:
#         if element == 1:
#             visited += 1
            
# print(visited)
result = 0

for row in visited:
    result += len(visited[row])
print(result)