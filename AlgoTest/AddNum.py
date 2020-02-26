"""
자연수 n이 주어졌을 때 각 자릿수를 더하는 과정을 반복하여 한 자리 숫자를 만들어 반환하는 함수를 완성해 주세요.
"""

def solution(n):
    x = sum(int(digit) for digit in str(n))
    if len(str(x)) <= 1:
        return x
    else:
        return solution(x)



