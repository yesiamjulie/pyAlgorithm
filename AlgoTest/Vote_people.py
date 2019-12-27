def solution(people, limit):
    people.sort()
    answer = 0

    start = 0
    end = len(people) -1

    while start <= end:
        if people[end] + people[start] > limit:
            end -= 1
        else:
            start += 1
            end -= 1
        answer = answer + 1

    return answer