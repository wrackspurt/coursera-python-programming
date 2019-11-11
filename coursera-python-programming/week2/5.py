n = int(input())
if (n >= 11) and (n <= 14):
    print(n, 'korov')
else:
    t = n % 10
    if (t == 0) or ((t >= 5) and (t <= 9)):
        print(n, 'korov')
    if t == 1:
        print(n, 'korova')
    if (t >= 2) and (t <= 4):
        print(n, 'korovy')



