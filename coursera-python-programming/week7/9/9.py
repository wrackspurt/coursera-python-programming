def main():
    fin = open('input.txt', encoding='utf8')
    d = {}
    for line in fin:
        words = line.strip().split()
        for word in words:
            d[word] = d.get(word, 0) + 1
    print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])


if __name__ == '__main__':
    main()
