def solution(operations):
    answer = []
    temp = []
    for i in operations:
        if i.split()[0] == 'I':
            temp.append(int(i.split()[1]))
            print(temp)

        elif i.split()[0] =="D":
            if len(temp) != 0:
                if i.split()[1] == '1':
                    temp.remove(max(temp))
                    print(temp)
                elif i.split()[1] == '-1':
                    temp.remove(min(temp))
                    print(temp)
    if len(temp) == 0:
        answer = [0,0]
    else:
        answer = [max(temp), min(temp)]

    return answer