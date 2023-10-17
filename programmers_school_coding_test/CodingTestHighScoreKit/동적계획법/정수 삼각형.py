def solution(triangle):
    score = {}
    n = len(triangle)
    if n == 1:
        return triangle[0][0]
    for i in range(n):
        score[(n - 1, i)] = triangle[n - 1][i]

    for y in range(n - 2, -1, -1):
        for x in range(y + 1):
            score[(y, x)] = max(score[(y + 1, x)], score[(y + 1, x + 1)]) + triangle[y][x]
    return score[(0, 0)]
