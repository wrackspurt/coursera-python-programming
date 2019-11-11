s = input()
a = [int(s) for s in s.split()]
am = 0
for i in a:
    if int(i) > 0:
        am += 1
print(am)
