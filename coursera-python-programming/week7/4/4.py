def main():
    fl = open('input.txt', 'r', encoding='utf-8')
    l = []
    for i in fl.read().split('\n'):
        l += i.split()
    print(len(set(l)))


if __name__ == '__main__':
    main()
