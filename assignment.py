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
    



    

def toRadians(angle):
    anglefl = float(angle)
    answer = (anglefl * (math.pi / 180))
    return answer

def cosineLaw(number1,number2,angle,booli):
    angle = toRadians(angle)
    answer = math.sqrt((((number1 ** 2) + (number2 ** 2)) - 2) * (number1 * number2 * (math.cos(angle)))
    return answer    


def solution(number1,number2,angle,booli):
    if "-" in answer1:
        answer = answer2
    else:
        answer = answer1
    return answer

def quadratic(number1,number2,angle):
    answer1 = ((number + math.sqrt(((number ** 2) - 4) * number1 * angle)) / (2 * number1)
    answer2 = ((number - math.sqrt(((number ** 2) - 4) * number1 * angle)) / (2 * number1)
    return answer1 and answer2
