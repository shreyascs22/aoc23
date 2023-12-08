from math import lcm
lines = open("q8.txt").read().split('\n')
place = [lines[i].split('=') for i in range(len(lines))]
pair = [place[i][1].lstrip() for i in range(2,len(place))]
place = place[2:]
place = [place[i][0].strip() for i in range(len(place))]
pair = [pair.strip('()').split(', ') for pair in pair]
instructions = lines[0]
steps = 0
index = place.index("AAA")
i = 0
count = 0
while(place[index] != "ZZZ"):
    if(i == len(instructions)):
        i = 0
    if(instructions[i] == "L"):
        index = place.index(pair[index][0])
    elif(instructions[i] == "R"):
        index = place.index(pair[index][1])
    steps += 1
    i += 1
    print(steps)