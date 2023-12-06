file = open("q4.txt")
lines = file.readlines()
a=[]
arr = []
firstpart = []
secondpart = []
winningnum = []
mynum = []
sum = 0
counts = []
for i in range(199):
    counts.append(1)
for i in range(len(lines)):
    arr = lines[i].split('|')
    firstpart.append(arr[0])
    secondpart.append(arr[1])
for i in range(len(firstpart)):
    array = firstpart[i].split(':')
    a.append(array[1])
    winningnum = a[i].split()
    mynum = secondpart[i].split()
    count = 0
    for j in range(len(winningnum)):
        if(winningnum[j] in mynum):
            count = count+1
    for k in range(i+1,i+count+1):
        counts[k] = counts[k] + counts[i]
sumcount = 0
for i in range(len(counts)):
    sumcount = sumcount + counts[i]
    print(sumcount)