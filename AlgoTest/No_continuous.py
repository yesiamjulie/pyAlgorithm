
def solution(arr):
    result = []
    for i, v in enumerate(arr):
        if i == 0:
            result.append(v)
        elif arr[i-1] == v:
            continue
        else:
            result.append(v)
    return result


''' clean code is .....
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
'''