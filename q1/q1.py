file = open("q1.txt","r")
f_data = file.read()
f_lines = f_data.splitlines()
sum = 0
for line in f_lines:
    intarr = []
    for character in range(0,len(line)):
        if (line[character].isdigit()):
            intarr.append(line[character])
    sum = sum + int(intarr[0]+intarr[len(intarr)-1])
    print(sum);
file.close()