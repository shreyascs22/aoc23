lines = open("q13.txt").read().split('\n\n')
lava = [lines[i].split('\n') for i in range(len(lines))]
transposed_matrices = [[''.join(row[i] for row in matrix) for i in range(len(matrix[0]))] for matrix in lava]

def mirror(arr,length,list):
    if (length-(arr[0]+2)) < arr[0]:
        selected_stringsbefore = list[-(length-(arr[0]+2)) + arr[0]:arr[0]]
        selected_stringsafter = list[arr[0]+2:]
        result = " ".join(reversed(selected_stringsbefore))
        result1 = " ".join(selected_stringsafter)
        if result == result1:
            return arr
        else:
            return [0,0]
    else:
        selected_stringsbefore = list[:arr[0]]
        selected_stringsafter = list[arr[0]+2:arr[0]+2+(length-(arr[0]+2))-arr[0]+1]
        result = " ".join(reversed(selected_stringsbefore))
        result1 = " ".join(selected_stringsafter)
        if result == result1:
            return arr
        else:
            return [0,0]
hflag, vflag = 0, 0
horizontal, vertical = [],[]
for i in range(len(lava)):
    for j in range(len(lava[i])-1):
        if lava[i][j] == lava[i][j+1]:
            pos = [j,i]
            hflag = 1
    if hflag:
        if i != len(lava[i][j]):
            horizontal.append(pos)
        hflag = 0
for i in range(len(transposed_matrices)):
    for j in range(len(transposed_matrices[i])-1):
        if transposed_matrices[i][j] == transposed_matrices[i][j+1]:
            pos = [j,i]
            vflag = 1
    if vflag:
        if i != len(transposed_matrices[i][j]):
            vertical.append(pos)
        vflag = 0
href,vref = [],[]
sum = 0
print(horizontal)
for i in range(len(horizontal)):
    sum = sum+horizontal[i][0] + 1
print(sum)
# for i in range(len(horizontal)):
#     href.append(mirror(horizontal[i],len(lava[horizontal[i][1]]),lava[horizontal[i][1]]))
# finalh = [href[i] for i in range(len(href))]
# for i in range(len(vertical)):
#     vref.append(mirror(vertical[i],len(transposed_matrices[vertical[i][1]]),transposed_matrices[vertical[i][1]]))
# finalv = [vref[i] for i in range(len(vref))]
# finalh= [item for item in finalh if item != [0,0]]
# finalv= [item for item in finalv if item != [0,0]]
# row = [fh[0]+1 for fh in finalh]
# col = [fv[0]+1 for fv in finalv]
#print(sum(row)*100 + sum(col))