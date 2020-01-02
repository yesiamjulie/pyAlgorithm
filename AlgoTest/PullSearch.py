def solution(answers):
    answer = []

    stu1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    res = [0,0,0]

    for index, ans in enumerate(answers):
        if ans == stu1[index%len(stu1)]:
            res[0] += 1
        if ans == stu2[index % len(stu2)]:
            res[1] += 1
        if ans == stu3[index % len(stu3)]:
            res[2] += 1

    for index, stu in enumerate(res):
        if max(res) == stu:
            answer.append(index+1)

    return answer