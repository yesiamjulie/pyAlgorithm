
from itertools import permutations

def solution(numbers):
    answer= set()
    max = 10000000
    prime = [False, False] + [True]*max


    for idx, number in enumerate(prime):
        if number :
            k = idx * 2
            while k <= max:
                prime[k] = False
                k += idx
    for i in range(1, len(numbers) + 1):
        perm = permutations(list(numbers), i)
        for i in list(perm):
            num = int("".join(list(i)))
            if prime[num]:
                answer.add(num)
    return len(answer)

# Other Solution
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)