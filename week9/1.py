from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, li):
        self.li = deepcopy(li)

    def __str__(self):
        rows = []
        for row in self.li:
            rows.append('\t'.join(map(str, row)))
        return '\n'.join(rows)

    def size(self):
        return len(self.li), len(self.li[0])


exec(stdin.read())
