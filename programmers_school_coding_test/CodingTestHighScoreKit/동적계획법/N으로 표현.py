def calc(A, B):
    lst = set()
    for a in A:
        for b in B:
            lst.add(a+b)
            lst.add(a-b)
            lst.add(a*b)
            if b != 0:
                lst.add(a//b)
    return lst

def solution(N, number):
    dic = {}
    dic[1] = {N}
    if N == number:
        return 1
    for i in range(2,9):
        lst = {int(str(N)*i)}
        for j in range(1,i):
            lst.update(calc(dic[j],dic[i-j]))
        if number in lst:
            return i
        dic[i] = lst
    return -1