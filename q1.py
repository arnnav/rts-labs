'''
Print the number of integers in an array that are above the given input and the number that are below.
default inpArr = [1,5,2,1,10], k = 6

RUNNING INSTRUCTIONS:
    - python q1.py [--inpArr InputArray ] [--k valueOfGivenNumber]

EXAMPLE:
    - python q1.py
    - python q1.py --inpArr 1,5,2,1,10 --k 6

OUTPUT:
    - Number of integers in an array that are above or below the given number.
'''

import argparse

def aboveBelow(inpArr,k):
    # Assumption: ignore if equal.
    above,below = 0,0
    for i in inpArr:
        if i>k:
            above += 1
        elif i<k:
            below += 1

    return "above: "+str(above)+", below: "+str(below)


if __name__ == "__main__":
    py_parser = argparse.ArgumentParser(description='Above or Below a number', allow_abbrev=False)
    py_parser.add_argument('--inpArr', action='store', type=str, help='Input Array')
    py_parser.add_argument('--k', action='store', type=int, help='the value of given Number')
    args = py_parser.parse_args()

    inpArr = [1,5,2,1,10]
    k = 6
    if args.inpArr:
    	inpArr = [int(i) for i in args.inpArr.split(',')]
    if args.k:
    	k = args.k

    print(aboveBelow(inpArr,k))
