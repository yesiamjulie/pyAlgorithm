
N = int(input())
low = 0

def get_devided_num(low_n):
    e = list(map(int, str(low_n)))
    devided_num = low_n + sum(e)

    return devided_num

while get_devided_num(low) != N:
    if low == N:
        low = 0
        break
    else:
        low += 1

print(low)

