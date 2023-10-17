import copy

def dp(d, airport,course,i,n):
    course.append(airport)
    if i==n+1:
        return [course]
    ret = []
    if airport not in d:
        return ret
    for x in d[airport]:
        dd = copy.deepcopy(d)
        dd[airport].remove(x)
        ret += dp(dd,x,course[::],i+1,n) 
    return ret

def solution(tickets):
    d = {}
    n = len(tickets)
    for ticket in tickets:
        if ticket[0] not in d:
            d[ticket[0]] = [ticket[1]]
        else:
            d[ticket[0]].append(ticket[1])
            d[ticket[0]].sort()

    return dp(d, 'ICN', [], 1, n)[0]