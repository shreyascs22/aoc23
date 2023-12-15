line = open("q15.txt").read().split(',')
def algo(str):
    sum = 0
    sum = [((sum + ord(str[i]))*17)%256 for i in range(len(str))]     
    return sum
res = []
[res.append(algo(l)) for l in line]
print(sum(res))