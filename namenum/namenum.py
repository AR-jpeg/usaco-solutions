"""
ID: araoudu1
LANG: PYTHON3
TASK: namenum
"""

from typing import Dict, List

digits: str = open("namenum.in").read().strip(' ')

fout = open("namenum.out", 'w')
dictIn: List[str] = [word.strip('\n').strip(' ')
                     for word in open("dict.txt").readlines()]
has_one_valid_word: bool = False

mp: Dict[str, str] = {}

mp['A'] = mp['B'] = mp['C'] = '2'
mp['D'] = mp['E'] = mp['F'] = '3'
mp['G'] = mp['H'] = mp['I'] = '4'
mp['J'] = mp['K'] = mp['L'] = '5'
mp['M'] = mp['N'] = mp['O'] = '6'
mp['P'] = mp['R'] = mp['S'] = '7'
mp['T'] = mp['U'] = mp['V'] = '8'
mp['W'] = mp['X'] = mp['Y'] = '9'

for word in dictIn:
    if len(word) != len(digits):
        continue

    isValid: bool = True

    for i in range(len(word)):
        if word[i] == 'Q' or word[i] == 'Z':
            isValid = False
            break

        if mp[word[i]] != digits[i]:
            isValid = False
            break

    if isValid:
        has_one_valid_word = True
        fout.write(word + '\n')

if not has_one_valid_word:
    fout.write('NONE' '\n')
