def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0:
            q = [i]
            while q:
                x = q.pop(0)
                if visited[x] == 0:
                    for j in range(n):
                        if computers[x][j] == 1:
                            q.append(j)
                    visited[x] = 1
            answer += 1

    return answer