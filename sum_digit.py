def solution(x):
    answer = True

    num = str(x)
    sum = 0

    for i in num:
        sum += int(i)

    if int(num) % sum == 0:
        return answer
    else :
        answer = False
        return answer