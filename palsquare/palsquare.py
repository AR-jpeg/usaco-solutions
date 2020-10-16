"""
ID: araoudu1
LANG: PYTHON3
TASK: palsquare
"""

from typing import List


fin: str = open('palsquare.in').read().strip().strip('\n')
fout = open('palsquare.out', 'w')

base: int = int(fin)
numbers: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def convert(n: float, base: int, numbers: List[str]) -> str:
    result: str = ""
    while n > 0:
        result += numbers[int(n % base)]
        n -= n % base
        n /= base

    return result[::-1]


for i in range(1, 301):
    s: int = i*i

    square: str = convert(s, base, numbers)
    iterate: str = convert(i, base, numbers)
    reverse: str = square[::-1]

    if reverse == square:
        fout.write(iterate + " " + square + "\n")


fout.close()
