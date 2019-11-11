def IsPrime(n):
    if n == 2 or n == 3:
        return 'YES'
    if n % 2 == 0 or n < 2:
        return 'NO'
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return 'NO'

    return 'YES'


def main():
    n = int(input())
    print(IsPrime(n))


if __name__ == '__main__':
    main()
