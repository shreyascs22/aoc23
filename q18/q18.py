from itertools import groupby
from operator import itemgetter
lines = open("q18.txt").read().split('\n')
directions,grid = [],[[0,0]]
[directions.append([line.split()[0],line.split()[1]]) for line in lines]
for direction in directions:
    ele = grid[-1]
    if direction[0] == "R":
        [grid.append([ele[0],ele[1]+i+1]) for i in range(int(direction[1]))]
    elif direction[0] == "L":
        [grid.append([ele[0],ele[1]-i-1]) for i in range(int(direction[1]))]
    elif direction[0] == "U":
        [grid.append([ele[0]-i-1,ele[1]]) for i in range(int(direction[1]))]
    else:
        [grid.append([ele[0]+i+1,ele[1]]) for i in range(int(direction[1]))]
grid.pop()
sorted_grid = sorted(grid, key=itemgetter(0, 1))
grouped_grid = [list(group) for key, group in groupby(sorted_grid, key=itemgetter(0))]
grid =  [item for sublist in grouped_grid for item in sublist]
other_ele = []
for i in range(grid[0][0],grid[-1][0]+1):
    arr = []
    for coordinate in grid:
        if coordinate[0] == i:
            arr.append(coordinate)
        else:
            if len(arr) != 0:
                break
    for j in range(arr[0][1],arr[-1][1]):
        if [i,j] not in arr:
            other_ele.append([i,j])
# print(len(grid))
# print("Area : ",len(grid) + len(other_ele))   