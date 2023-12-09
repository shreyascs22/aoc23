lines = open("q9.txt").read().split('\n')
seq = [line.split() for line in lines]
differences,temp = [],[]
def difference(arr):
    diff = []
    global temp
    if temp != [] and (all(x == 0 for x in temp)):
        return differences
    if (arr in seq):
        differences.append(int(arr[len(arr)-1]))
    for i in range(len(arr)-1):
        num = int(arr[i+1]) - int(arr[i])
        diff.append(num)
    print(differences)
    differences.append(diff[len(diff)-1])
    temp = diff
    return difference(diff)
for s in seq:
    output = sum(difference(s))
    print(output)
    temp = []