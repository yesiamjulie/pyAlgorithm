'''
#1157


word = list(input().upper())

voca_list = [0] * 26

for i in word:
    voca_list[ord(i) - 65] += 1

if voca_list.count(max(voca_list)) >= 2:
    print('?')
else:
    print(chr(voca_list.index(max(voca_list)) + 65 ))
'''

n = input().upper()
t = []

for i in set(n):
  t.append(n.count(i))

idx =[i for i,x in enumerate(t) if x == max(t)]

if len(idx) > 1 :
  print("?")
else:
  print(list(set(n))[t.index(max(t))])