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
res = []
for i in range(len(transposed_matrices)):
    res.append(shift(transposed_matrices[i]))
index = [[len(res[i]) - i for i, char in enumerate(string) if char == 'O'] for string in res]
ans = 0
for val in index:
    ans = ans + sum(val)
print(ans)