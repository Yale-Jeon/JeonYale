def solution(n, stations, w):
    answer = 0
    stations.insert(0, (-1) * w)
    stations.append(n + w + 1)
    N = len(stations)
    i = 0
    now = stations[0]
    while i < N - 1:
        if stations[i + 1] - now > 2 * w + 1:
            now += 2 * w + 1
            answer += 1
        else:
            i += 1
            now = stations[i]

    return answer