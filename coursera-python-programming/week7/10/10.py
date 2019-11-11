fin = open('input.txt', encoding='utf8')
d = {}
for line in fin:
    words = line.strip().split()
    for word in words:
        d[word] = d.get(word, 0) + 1

for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])