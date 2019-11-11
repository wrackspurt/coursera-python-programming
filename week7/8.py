def main():
    n = int(input())
    d = {}
    for i in range(n):
        first, second = input().split()
        d[first] = second
        d[second] = first
    print(d[input()])


if __name__ == '__main__':
    main()
