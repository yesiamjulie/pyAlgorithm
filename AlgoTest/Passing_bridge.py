def solution(bridge_length, weight, truck_weights):

    answer =0
    waiting = truck_weights
    length_truck = len(truck_weights)
    passed = []
    passing = []
    on_bridge = []

    while len(passed) != length_truck:
        for i in range(len(passing)):
            passing[i] += - 1
        if passing and passing[0] == 0:
            del passing[0]
            passed.append(on_bridge.pop(0))
        if waiting and weight >= sum(on_bridge) + waiting[0]:
            on_bridge.append(waiting.pop(0))
            passing.append(bridge_length)
            print(passing)
        answer += 1
    return answer