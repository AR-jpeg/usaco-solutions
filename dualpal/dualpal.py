"""
ID: araoudu1
LANG: PYTHON3
PROG: dualpal
"""
from typing import List

numbers = ['0', '1', '2', '3', '4', '5', '6', '7',
           '8', '9']


def convert(n: float, base: int, numbers: List[str]) -> str:
    result: str = ""
    while n > 0:
        result += numbers[int(n % base)]
        n -= n % base
        n /= base

    return result[::-1]


fin = open('dualpal.in')
fout = open('dualpal.out', 'w')

N, S = [int(num) for num in fin.read().strip().strip('\n').split()]
countOfPalindromes = 0
i = S + 1

while countOfPalindromes < N:
    numBases = 0
    for base in range(2, 11):
        result: str = convert(i, base, numbers)

        if result == result[::-1]:
            numBases += 1

    if numBases >= 2:
        countOfPalindromes += 1
        fout.write(str(i) + "\n")

    i += 1

fin.close()
fout.close()
