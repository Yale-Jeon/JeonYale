def solution(money):
    n = len(money)
    money1 = [0] + money[::][1:]
    money2 = [0] + money[::][:-1]
    dp1 = [0, money1[1]]
    dp2 = [0, money2[1]]
    for i in range(2, n):
        if money1[i] + dp1[i - 2] >= dp1[i - 1]:
            dp1.append(money1[i] + dp1[i - 2])
        else:
            dp1.append(dp1[i - 1])

    for i in range(2, n):
        if money2[i] + dp2[i - 2] >= dp2[i - 1]:
            dp2.append(money2[i] + dp2[i - 2])
        else:
            dp2.append(dp2[i - 1])
    return max(dp1[-1], dp2[-1])