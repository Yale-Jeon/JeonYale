def convert(word1, word2):
    c = 0
    for i, w in enumerate(word1):
        if w != word2[i]:
            c += 1
    return True if c < 2 else False


def solution(begin, target, words):
    if target not in words:
        return 0
    n = len(words)
    index = words.index(target)
    graph = {}
    for i in range(n):
        graph[i] = []
    distance = [999 for i in range(n)]
    q = []
    for i in range(n):
        if convert(begin, words[i]):
            q.append((0, i))
        for j in range(i + 1, n):
            if convert(words[i], words[j]):
                graph[i].append(j)
                graph[j].append(i)
    while q:
        dist, now = q.pop(0)
        if distance[now] <= dist + 1:
            continue
        distance[now] = dist + 1
        for w in graph[now]:
            q.append((dist + 1, w))

    return 0 if distance[index] == 999 else distance[index]