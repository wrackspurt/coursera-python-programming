def main():
    balls = list()
    outfile = open('output.txt', 'w', encoding='utf-8')
    with open('input.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        K = int(line)
        if K == 0:
            print('0', file=outfile)
            return
        line = f.readline()
        while line:
            parts = line.split(' ')
            ball1 = int(parts[-3])
            ball2 = int(parts[-2])
            ball3 = int(parts[-1])

            if ball1 < 40 or ball2 < 40 or ball3 < 40:
                pass
            else:
                total = ball3 + ball2 + ball1
                balls.append(total)

            line = f.readline()

    balls.sort(reverse=True)
    lenB = len(balls)
    if lenB <= K:
        print('0', file=outfile)
        return

    E = balls[0]

    maxK = K + 1 if K + 1 <= lenB else K

    one = True
    for i in range(1, maxK):
        if balls[i] != E:
            one = False
            break

    if one:
        print('1', file=outfile)
        return

    B = balls[K - 1]

    if len(balls) >= K:
        if balls[K-1] == balls[K]:
            j = 1
            while balls[K - j + 1] == balls[K - j]:
                j += 1
            B = balls[K - j]

    print(str(B), file=outfile)


if __name__ == '__main__':
    main()
