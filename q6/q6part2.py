import math
time = 46828479
distance = 347152214061471
start = int((-time - math.sqrt(time**2 - 4*distance))/2)
end = int((-time + math.sqrt(time**2 - 4*distance))/2)
value_range = abs(end-start)
print(value_range)