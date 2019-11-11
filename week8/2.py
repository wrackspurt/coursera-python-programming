from sys import stdin
print(len(set((lambda y: (' '.join(y)).split())(list(stdin)))))


