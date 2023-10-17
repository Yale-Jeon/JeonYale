def solution(distance, rocks, n):
    low = 0
    high = distance
    rocks.sort()
    dist = [rocks[0]] + [rocks[i + 1] - rocks[i] for i in range(len(rocks) - 1)] + [distance - rocks[-1]]
    m = len(dist)
    while True:
        if abs(high - low) <= 1:
            break
        mid = (low + high) // 2
        c = 0
        cnt = 0
        for i in range(m):
            c += dist[i]
            if c < mid:
                cnt += 1
            else:
                c = 0
        if cnt <= n:
            low = mid
        else:
            high = mid
    # high is answer?
    c = 0
    cnt = 0
    for i in range(m):
        c += dist[i]
        if c < high:
            cnt += 1
        else:
            c = 0
    if cnt == n:
        return high
    else:
        return low