previous = -1
current_len = 0
max_len = 0
n = int(input())
while n != 0:
    if previous == n:
        current_len += 1
    else:
        previous = n
        max_len = max(max_len, current_len)
        current_len = 1
    n = int(input())
max_len = max(max_len, current_len)
print(max_len)
