lines = open("q6.txt").readlines()
times = lines[0].split(':')[1].split()
distance = lines[1].split(':')[1].split()
count_arr = [0,0,0,0]
j = 0
for time in times:
    for i in range(int(time)+1):
        dist = i*(int(time)-i)
        if(dist > int(distance[j])):
            count_arr[j] += 1
    j += 1
print(count_arr[0]*count_arr[1]*count_arr[2]*count_arr[3])