
n = int(input())
count = 0

for i in range(n):
    str = input()
    word = []
    word.append(str[0])

    if len(str) == 1:
        count += 1

    for i in range(1, len(str)):
        if str[i] != str[i-1]:
            if str[i] in word:
                break
            else:
                word.append(str[i])
        if i == len(str) -1:
            count += 1


print(count)
