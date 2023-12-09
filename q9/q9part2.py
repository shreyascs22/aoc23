lines = open("q9.txt").read().split('\n')
seq = [line.split() for line in lines]
seq = [[0,3,6,9,12,15],[1,3,6,10,15,21],[10,13,16,21,30,45]]
differences,temp = [],[]
count = 1
def difference(arr,power):
    diff = []
    global temp,count
    if temp != [] and (all(x == 0 for x in temp)):
        return differences
    if (arr in seq):
        differences.append(int(arr[0]))
    for i in range(len(arr)-1):
        num = int(arr[i+1]) - int(arr[i])
        diff.append(num)
    differences.append(diff[0]*power)
    temp = diff
    count += 1
    return difference(diff,(-1**count))
for s in seq:
    #print(s)
    output = sum(difference(s,1))
    #print(output)
    temp = []
    count = 0