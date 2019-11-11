maximum = 0
num = 0
n = -1
while n != 0:
    n = int(input())
    if n > maximum:
        maximum, num = n, 1
    elif n == maximum:
        num += 1
print(num)
