def solution(n, k):
    from math import factorial as facto

    pool = [e+1 for e in range(n)]
    answer = []
    f = facto(n)

    k-=1

    while n>0:
        f //= n
        n-=1
        answer.append(pool.pop(k//f))
        k %= f
    return answer