def CountSort(l):
    sortedList = [0] * 101
    for i in l:
        sortedList[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sortedList[i], end='')


lst = [int(i) for i in input().split()]
CountSort(lst)
