first = int(input())
second = int(input())
if first < second:
    first, second = second, first
n = int(input())
while n != 0:
    if n > first:
        second, first = first, n
    elif n > second:
        second = n
    n = int(input())
print(second)
