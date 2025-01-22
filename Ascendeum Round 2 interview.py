# code submitted during the interview

input = int(input("Enter a number"))
for i in range(1,input):
    for j in range(1,i+1):
        print("*", end = "")
    print("")
for i in range(input, 0, -1):
    for j in range(1,i+1):
        print("*", end = "")
    print("")

# Code which I was trying to do but forgot the syntax which converts char to alphabets
input = int(input("Enter a number"))
for i in range(1,input):
    for j in range(1,i+1):
        print(chr(65+j-1), end = "")
        # in the above line, instead of using chr, I tried to convert ASCII values using char which threw error, So I continued with * pattern
    print("")
for i in range(input, 0, -1):
    for j in range(1,i+1):
        print(chr(65+j-1), end = "")
        # in the above line, instead of using chr, I tried to convert ASCII values using char which threw error, So I continued with * pattern
    print("")
    