a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = pow(p * (p - a) * (p - b) * (p - c), 0.5)
print('{:.6f}'.format(s))
