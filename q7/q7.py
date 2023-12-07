lines = open("q7.txt").read().split('\n')
cards = [line.split()[0] for line in lines]
bet = [line.split()[1] for line in lines]
arr = [list(pair) for pair in zip(cards,bet)]
rank, first, second, third, fourth, fifth = [],[],[],[],[],[]
order = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
for card in cards:
    unique_count = len(set(card))
    if(unique_count == 1):
        rank.append(5)
    elif(unique_count == 2):
        rank.append(4)
    elif(unique_count == 3):
        rank.append(3)
    elif(unique_count == 4):
        rank.append(2)
    else:
        rank.append(1)
priority = [list(pair) for pair in zip(arr,rank)]
for i in range(1000):
    if(priority[i][1] == 1):
        first.append(priority[i][0])
    elif(priority[i][1] == 2):
        second.append(priority[i][0])
    elif(priority[i][1] == 3):
        third.append(priority[i][0])
    elif(priority[i][1] == 4):
        fourth.append(priority[i][0])
    else:
        fifth.append(priority[i][0])
first = sorted(first, key=lambda lst: [order.get(char, 0) for char in lst[0]], reverse=True)
second = sorted(second, key=lambda lst: [order.get(char, 0) for char in lst[0]], reverse=True)
third = sorted(third, key=lambda lst: [order.get(char, 0) for char in lst[0]], reverse=True)
fourth = sorted(fourth, key=lambda lst: [order.get(char, 0) for char in lst[0]], reverse=True)
fifth = sorted(fifth, key=lambda lst: [order.get(char, 0) for char in lst[0]], reverse=True)
hands = []
hands.append(first)
hands.append(second)
hands.append(third)
hands.append(fourth)
hands.append(fifth)
print(hands[2])
sum = 0
count = 1
for i in range(5):
    for j in range(len(hands[i])):
        sum = sum + int(hands[i][j][1])*count
        count += 1
        print(sum,hands[i][j][1])
print(sum)
