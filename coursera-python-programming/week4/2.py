def isPointInSquare(x, y, v):
    return (v ** 2 >= x ** 2) and (v ** 2 >= y ** 2)


x, y = float(input()), float(input())

print("YES" if isPointInSquare(x, y, 1) else "NO")
