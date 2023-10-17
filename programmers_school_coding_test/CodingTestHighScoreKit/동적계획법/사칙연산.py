def dp_max(arr):
    n = len(arr)
    if n==1:
        return int(arr[0])
    answer = []
    for i in range(1,n,2):
        if arr[i] == '+':
            answer.append(dp_max(arr[:i])+dp_max(arr[i+1:]))
        else:
            answer.append(dp_max(arr[:i])-dp_min(arr[i+1:]))
    return max(answer)

def dp_min(arr):
    n = len(arr)
    if n==1:
        return int(arr[0])
    answer = []
    for i in range(1,n,2):
        if arr[i] == '+':
            answer.append(dp_min(arr[:i])+dp_min(arr[i+1:]))
        else:
            answer.append(dp_min(arr[:i])-dp_max(arr[i+1:]))
    return min(answer)

def solution(arr):
    n = len(arr)
    if n==1:
        return int(arr[0])
    answer = []
    for i in range(1,n,2):
        if arr[i] == '+':
            answer.append(dp_max(arr[:i])+dp_max(arr[i+1:]))
        else:
            answer.append(dp_max(arr[:i])-dp_min(arr[i+1:]))
    return max(answer)