"""
ID: araoudu1
LANG: PYTHON3
PROG: dualpal
"""
from typing import List

numbers: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9']


def convert(number: float, base: int) -> str:
    result: str = ""
    while number > 0:
        result += numbers[int(number % base)]
        number -= number % base
        number /= base

    return result[::-1]


fin = open('dualpal.in')
fout = open('dualpal.out', 'w')

N, S = [int(num) for num in fin.read().strip().strip('\n').split()]
count_of_palindromes = 0
i = S + 1

while count_of_palindromes < N:
    num_bases = 0
    for base in range(2, 11):
        result: str = convert(i, base)

        if result == result[::-1]:
            num_bases += 1

    if num_bases >= 2:
        count_of_palindromes += 1
        fout.write(str(i) + "\n")

    i += 1

fin.close()
fout.close()
