p = int(input())
x = int(input())
y = int(input())
previous = x * 100 + y
following = int(previous * (p + 100) / 100)
a = following // 100
b = following % 100
print(a, b)
