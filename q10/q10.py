lines = open("q10.txt").read().split()
print(lines)
count = 0
def path(row,index,arr,dir):
    global count
    match(dir):
        case "R":
            if(lines[row][index] in arr):
                if(lines[row][index] == "-"):
                    count += 1
                    print(count,"-")
                    return (row,index+1,["-","7","J"],"R")
                elif(lines[row][index] == "7"):
                    count += 1
                    print(count,"7")
                    return (row+1,index,["L","|","J"],"D")
                else:
                    count += 1
                    print(count,"J")
                    return (row-1,index,["7","|","F"],"U")
        case "L":
            if(lines[row][index] in arr):
                if(lines[row][index] == "-"):
                    count += 1
                    print(count,"-")
                    return (row,index-1,["-","L","F"],"L")
                elif(lines[row][index] == "L"):
                    count += 1
                    print(count,"L")
                    return (row-1,index,["7","|","F"],"U")
                else:
                    count += 1
                    print(count,"F")
                    return (row+1,index,["L","|","J"],"D")
        case "U":
            if(lines[row][index] in arr):
                if(lines[row][index] == "7"):
                    count += 1
                    print(count,"7")
                    return (row,index-1,["L","-","F"],"L")
                elif(lines[row][index] == "|"):
                    count += 1
                    print(count,"|")
                    return (row-1,index,["7","|","F"],"U")
                else:
                    count += 1
                    print(count,"F")
                    return (row,index+1,["-","7","J"],"R")
        case "D":
            if(lines[row][index] in arr):
                if(lines[row][index] == "L"):
                    count += 1
                    print(count,"L")
                    return (row,index+1,["-","7","J"],"R")
                elif(lines[row][index] == "|"):
                    count += 1
                    print(count,"|")
                    return (row+1,index,["L","|","J"],"D")
                else:
                    count += 1
                    print(count,"J")
                    return (row,index-1,["L","-","F"],"L")
for i in range(len(lines)):
    if("S" in lines[i]):
        rno = i
        index = lines[i].index("S")
        #c = path(rno-1,index,["7","|","F"],"U")
        r,i,arr,dir = path(rno+1,index,["L","|","J"],"D")
        while(1):
            r,i,arr,dir = path(r,i,arr,dir)
            print(r,i,arr,dir)
        break