'''
test 2675
'''

#test case 갯수
test = int(input())

strings = []

for i in range(test):
    strings.append(input())

for s in strings:
    num = int(s[0])
    string = s[2:]

    for ss in string:
        print(ss*num, end="")
    print()