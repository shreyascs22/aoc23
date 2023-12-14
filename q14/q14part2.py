lines = open("q14.txt").read().split('\n\n')
rocks = [lines[i].split('\n') for i in range(len(lines))]
transposed_matrices = [[''.join(row[i] for row in matrix) for i in range(len(matrix[0]))] for matrix in rocks]
transposed_matrices = transposed_matrices[0]
def shift(str):
    count = 0
    for i in range(1,len(str)):
        if str[i-1] == '.' and str[i] == 'O':
            l = list(str)
            l[i-1],l[i] = l[i],l[i-1]
            str = "".join(l)
            count += 1
    if count > 0:
        return shift(str)
    else:
        return str
cycle = 0
cyclevals = []
while(1):
    nres,wres,sres,eres = [],[],[],[]
    [nres.append(shift(transposed_matrices[i])) for i in range(len(transposed_matrices))]
    matrix = ["".join(row) for row in zip(*nres)]
    [wres.append(shift(matrix[i])) for i in range(len(matrix))]
    matrix = ["".join(row) for row in zip(*wres)]
    matrix = [''.join(reversed(matrix[i])) for i in range(len(matrix))]
    [sres.append(shift(matrix[i])) for i in range(len(matrix))]
    matrix = [''.join(reversed(sres[i])) for i in range(len(sres))]
    matrix = ["".join(row) for row in zip(*matrix)]
    matrix = [''.join(reversed(matrix[i])) for i in range(len(matrix))]
    [eres.append(shift(matrix[i])) for i in range(len(matrix))]
    matrix = [''.join(reversed(eres[i])) for i in range(len(eres))]
    cycle += 1
    if matrix in cyclevals:
        ind=0
        for cval in cyclevals:
            if (matrix == cval):
                break
            ind += 1
        break
    cyclevals.append(matrix)
    matrix = ["".join(row) for row in zip(*matrix)]
    transposed_matrices = matrix
ans,h = 0,100
for i in range(h):
    ans += (h - i) * cyclevals[ind+((1000000000-(ind+1))%(cycle - (ind+1)))][i].count("O")
print(ans)