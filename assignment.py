#! python3

import math

def tempConversion(tempnum, tipe):
    if "F" in tipe:
        answer = float(((tempnum - 32) * (5 / 9)))
    else:
        answer = float((((tempnum * (5 / 9)) + 32)))
    answer = round(answer, 1)
    return answer



def factorPair(number, factor):
    fact = int(number / factor)
    number = int(number)
    answer = [fact,number]
    return answer
    


def cosineLaw():
    pass

def toRadians():
    pass

def solution():
    pass

def quadratic():
    pass
