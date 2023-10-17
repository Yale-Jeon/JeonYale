from collections import defaultdict
import bisect
import re

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for data in info:
        x = data.split(' ')
        for a in [x[0], '-']:
            for b in [x[1], '-']:
                for c in [x[2], '-']:
                    for d in [x[3], '-']:
                        dic[a + b + c + d].append(int(x[4]))
    for key in dic:
        dic[key].sort()

    for q in query:
        y = re.sub(' and ', '', q)
        y, score = y.split()
        answer.append(len(dic[y]) - bisect.bisect_left(dic[y], int(score)))

    return answer