def IsPointInCircle(x, y, xc, yc, r):
    if (x - xc) ** 2 + (y - yc) ** 2 <= r * r:
        return 'YES'
    else:
        return 'NO'


def main():
    x, y, xc, yc, r = (float(input()) for i in range(5))
    print(IsPointInCircle(x, y, xc, yc, r))


if __name__ == "__main__":
    main()
