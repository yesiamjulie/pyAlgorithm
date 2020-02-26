"""

서로 다른 자연수들로 이루어진 배열 arr와 숫자 n이 입력으로 주어집니다.
만약 배열 arr에 있는 서로 다른 2개의 자연수를 합하여 숫자 n을 만드는 것이 가능하면 true를, 불가능하면 false를 반환하는 함수를 작성하세요.

"""

def solution(arr, n):
    answer = False
    length = len(arr)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if arr[i] + arr[j] == n:
                answer = True
    return answer