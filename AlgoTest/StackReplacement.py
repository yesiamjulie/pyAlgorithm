def solution(arrangement):
    answer = 0
    arrangement = arrangement.replace("()","L")
    lst = []
    for idx, c in enumerate(arrangement):
        if c == '(':
            lst.append('(')
            answer += 1
        elif c == ')':
            lst.pop()
        else:
            answer += len(lst)
    return answer