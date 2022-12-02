#Rock = A 
#Paper = B
#Scissors = C

#You 2 
#Rock = X = loose
#Paper = Y = draw 
#Scissors = Z = win

codes ={"A":"rock", "B":"paper", "C":"scissors", "X":"rock", "Y":"paper", "Z":"scissors"}
points = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

#open file with while loop 
def compare(Opponent, you):
  if codes[Opponent] == codes[you]:
    return 3
  elif codes[Opponent] == "rock" and codes[you] == "paper":
    return 6
  elif codes[Opponent] == "rock" and codes[you] == "scissors":
    return 0
  elif codes[Opponent] == "paper" and codes[you] == "scissors":
    return 6
  elif codes[Opponent] == "paper" and codes[you] == "rock":
    return 0
  elif codes[Opponent] == "scissors" and codes[you] == "rock":
    return 6
  elif codes[Opponent] == "scissors" and codes[you] == "paper":
    return 0
  else:
    print(Opponent, you)
    Exception("Invalid input")
    return "Error"

def determine_move(opponent, expected_result):
  if expected_result == "Y": #draw
    return opponent
  elif expected_result == "X": #you should lose
    if codes[Opponent] == "rock":
      return "Z"
    elif codes[Opponent] == "paper":
      return "X"
    return "Y"
  elif expected_result == "Z": #you should win
    if codes[Opponent] == "rock":
      return "Y"
    elif codes[Opponent] == "paper":
      return "Z"
    return "X"
  

with open("/Users/dmarkov/Projects/zeRepo/AdventOfCode22/day2_input.txt", "r") as f:
    lines = f.read().splitlines()

result = 0
for line in lines: 
  round = (line.split(" "))
  Opponent = round[0]
  expected_result = round[1]
  you = determine_move(Opponent, expected_result)
  round_score = points[you] + compare(Opponent, you)
  result += round_score
  
  
print(result)