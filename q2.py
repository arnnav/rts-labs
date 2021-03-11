'''
Rotate the characters in a string by a given input and have the overflow appear at the beginning.
default inpStr = MyString, k = 2

RUNNING INSTRUCTIONS:
    - python q2.py [--inpStr InputString ] [--k valuToRotateBy]

EXAMPLE:
    - python q2.py
    - python q2.py --inpStr MyString --k 2

OUTPUT:
    - Rotated String
'''

import argparse

def rotateStr(string,k):
    if k > len(string):
        k %= len(string)
    if k <= 0:
        return string
    return string[-k:]+string[:len(string)-k]

if __name__ == "__main__":
    py_parser = argparse.ArgumentParser(description='Rotate characters of a String', allow_abbrev=False)
    py_parser.add_argument('--inpStr', action='store', type=str, help='Input String')
    py_parser.add_argument('--k', action='store', type=int, help='the value to Rotate the String by')
    args = py_parser.parse_args()

    inpStr = "MyString"
    k = 2
    if args.inpStr:
    	inpStr = args.inpStr
    if args.k:
    	k = args.k

    print(rotateStr(inpStr,k))
