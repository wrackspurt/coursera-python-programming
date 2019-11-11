def main():
    students = [{input() for _ in range(int(input()))} for _
                in range(int(input()))]
    known_by_everyone, known_by_someone = \
        set.intersection(*students), set.union(*students)
    print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
    print(len(known_by_someone), *sorted(known_by_someone), sep='\n')


if __name__ == '__main__':
    main()
