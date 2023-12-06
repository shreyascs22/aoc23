file = open("q4.txt")
lines = file.readlines()
a=[]
arr = []
firstpart = []
secondpart = []
winningnum = []
mynum = []
sum = 0
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
    if(count != 0):
        sum = sum + 2**(count-1)
    print(sum)