def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    dic = {}
    for i, name in enumerate(enroll):
        dic[name] = referral[i], i
    for name, money in zip(seller, amount):
        money *= 100
        ref, i = dic[name]
        while True:
            answer[i] += money - int(0.1 * money)
            if ref == "-" or money <= 9:
                break
            money = int(0.1 * money)
            ref, i = dic[ref]

    return answer