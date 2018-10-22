hr1 = int(input())
min1 = int(input())
sec1 = int(input())
hr2 = int(input())
min2 = int(input())
sec2 = int(input())

total1 = ((hr1 * 3600) + (min1 * 60) + (sec1))
total2 = ((hr2 * 3600) + (min2 * 60) + (sec2))

subtraction = (total2 - total1)
print(subtraction)