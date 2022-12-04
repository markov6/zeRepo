with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day4_input.txt", "r") as f:
    lines = f.read().splitlines()
    
score = 0 
for pair in lines:
  pairAssignments = pair.split(",")
  elf1 = pairAssignments[0]
  elf2 = pairAssignments[1]
  elf1_start, elf1_end = elf1.split("-")
  elf2_start, elf2_end = elf2.split("-")
  elf1_assignments = range(int(elf1_start), int(elf1_end)+1)
  elf2_assignments = range(int(elf2_start), int(elf2_end)+1)
  if (int(elf1_start) in elf2_assignments or int(elf1_end) in elf2_assignments) or (int(elf2_start) in elf1_assignments or int(elf2_end) in elf1_assignments):
    score += 1

print(score)

