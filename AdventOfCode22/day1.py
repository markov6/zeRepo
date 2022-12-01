def uppercase_decorator(function):
    def wrapper():
        func = function()
        #func will equal to result of passed in funciton 
        make_uppercase = func.upper() #manipulate the result
        return make_uppercase #return the result

    return wrapper #return the wrapper function

@uppercase_decorator
def say_hi():
    return 'hello there'
  
#

#decorator is function that accepts another function as an argument

#read a txt file from filesystem
counter = 1
while   True:
    try:
        file = open("/Users/dmarkov/Workspace/input.txt", "r")
        break
    except FileNotFoundError:
        print("File not found, please try again")

input = file.readlines()
print(input)
#for line in input if it's empty print "empty file" else print line

#function to create new array

count = 0
for line in input:
    count += 1
    if line == "":
        print("Empty file")
    else:
        print(line.strip())
        
with open("/Users/dmarkov/Workspace/input.txt", "r") as file:
    lines = file.readlines()
    result = 0
    best_result = 0
    results = []
    for line in lines:
        if line.strip():
            print('The line is NOT empty ->', line.strip())
            result = result + int(line.strip())
        else:
            print('The line is empty', result)
            
            if result > best_result:
                best_result = result
            results.append(int(result))
            result = 0
# sort the array and show first 3 elements
results.sort(reverse=True)
#sum first 3 elements
print(results[0] + results[1] + results[2])
