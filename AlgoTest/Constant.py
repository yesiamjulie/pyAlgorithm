
word = list(map(int, input().split()))

reverse = []


for i in word:
    reverse.append(int(str(i)[::-1]))


print(max(reverse))