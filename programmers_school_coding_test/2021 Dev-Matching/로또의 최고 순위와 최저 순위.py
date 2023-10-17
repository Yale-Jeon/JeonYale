def solution(lottos, win_nums):
    a = 0
    b = lottos.count(0)
    for x in lottos:
        if x in win_nums:
            a += 1
    dic = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    return [dic[a+b],dic[a]]