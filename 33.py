i = 0
numbers = []


# while loop(modified as the study drills told me to
"""
def popNumbers(start, Stop,step):
        while start < Stop:
            print(f"At the top i is {start}")
            numbers.append(start)

            start = start + step
            print("Numbers now: ", numbers)
            print(f"At the bottom i is {start}")
"""


#study drill #5(make a for loop instead)
def popNumbers(start, stop, step):
    for i in range(start,stop,step):
            print(f"At the top i is {i}")
            numbers.append(i)
            print("Numbers now: ", numbers)
            print(f"At the bottom i is {i}")





popNumbers(15,30,2)


print("The numbers: ")

for num in numbers:
    print(num)

# är på study drill #2
