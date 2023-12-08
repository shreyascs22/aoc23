from math import lcm
lines = open("q8.txt").read().split('\n')
place = [lines[i].split('=') for i in range(len(lines))]
pair = [place[i][1].lstrip() for i in range(2,len(place))]
place = place[2:]
place = [place[i][0].strip() for i in range(len(place))]
pair = [pair.strip('()').split(', ') for pair in pair]
instructions = lines[0]
steps = []
A = []
for i in range(len(place)):
    if(place[i][2] == "A"):
        A.append(place[i][2])
        A.append(place.index(place[i]))
i = 0
count = 0
for j in range(1,12,2):
    step = 0
    index = A[j]
    while(place[index][2] != "Z"):
        if(i == len(instructions)):
            i = 0
        if(instructions[i] == "L"):
            index = place.index(pair[index][0])
        elif(instructions[i] == "R"):
            index = place.index(pair[index][1])
        i += 1
        step += 1
    steps.append(step)
print(lcm(*steps))