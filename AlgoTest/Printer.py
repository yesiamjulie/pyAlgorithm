def solution(priorities, location):
    answer = 0

    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            answer += 1
            priorities.pop(0)
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

''' other code
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans
'''