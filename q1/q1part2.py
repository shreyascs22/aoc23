'''file = open("q1.txt","r")
f_data = file.read()
f_lines = f_data.splitlines()
output = 0
sum = 0
stringnum = ["zero","one","two","three","four","five","six","seven","eight","nine"]
count_stringnum = 0    #To iterate through the stringnum array
min_pos = 0
max_pos = 0        #To find the index of the element having minium and maximum index value in stringarr
first_ele = 0
last_ele = 0
for line in f_lines:
    intarr = []
    stringarr = []
    count_stringnum = 0
    #adding stringed or worded numbers into array
    while(count_stringnum < 10):
        index = line.find(stringnum[count_stringnum])
        stringarr.extend([stringnum[count_stringnum], index])
        count_stringnum = count_stringnum + 1

    #adding number to array
    for character in range(0,len(line)):
        if (line[character].isdigit()):
            intarr.extend([int(line[character]), character])

    #Finding minimum and maximum index value
    if (len(stringarr)):
        min_pos = 100
        max_pos = stringarr[len(stringarr)-1]
        for ele in range(1,len(stringarr),2):
            if(min_pos > stringarr[ele] and stringarr[ele] != -1):
                min_pos = stringarr[ele]
                first_ele = int(ele/2);
            if(max_pos < stringarr[ele] and stringarr[ele] != -1):
                max_pos = stringarr[ele]
                last_ele = int(ele/2)
        #Comparing which is was present before in the line
        if(intarr[1]<min_pos):
            output =int(intarr[0])*10
        else:
            output = first_ele*10
        if(intarr[len(intarr)-1]>max_pos):
            output = output + int(intarr[len(intarr)-1])
        else:
            output = output + last_ele
    print(output)
    sum = sum + int(output)
    print(sum);
file.close()'''

with open("q1.txt") as file:
    data = []
    for line in file.readlines():
        line = line.replace('one','o1ne')
        line = line.replace('two','t2wo')
        line = line.replace('three','t3hree')
        line = line.replace('four','f4our')
        line = line.replace('five','f5ive')
        line = line.replace('six','s6ix')
        line = line.replace('seven','s7even')
        line = line.replace('eight','e8ight')
        line = line.replace('nine','n9ine')
        line = line.replace('zero','z0ero')
        item = []
        for character in line:
            if character>='0' and character<='9':
                item.append(int(character))
        data.append(item)
total = 0
for item in data:
    total += item[0]*10
    total += item[-1]
print(total)