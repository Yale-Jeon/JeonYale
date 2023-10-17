from collections import defaultdict

def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = []
    distance = defaultdict(lambda: 9999)
    q = [(0, 0, 0)]
    while q:
        dist, y, x = q.pop(0)
        if y > n - 1 or y < 0 or x > m - 1 or x < 0:
            continue
        if maps[y][x] == 0:
            continue
        if y == n - 1 and x == m - 1:
            answer.append(dist + 1)
            continue
        if distance[(y, x)] <= dist + 1:
            continue
        else:
            distance[(y, x)] = dist + 1
        q.append((dist + 1, y + 1, x))
        q.append((dist + 1, y - 1, x))
        q.append((dist + 1, y, x + 1))
        q.append((dist + 1, y, x - 1))

    return -1 if len(answer) == 0 else min(answer)