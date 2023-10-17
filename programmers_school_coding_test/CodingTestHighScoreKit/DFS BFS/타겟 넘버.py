def dp(numbers, target):
    if len(numbers) == 0:
        return 0
    if 2 * numbers[0] > target:
        return dp(numbers[1:], target)
    elif 2 * numbers[0] == target:
        return 1 + dp(numbers[1:], target)
    else:
        return dp(numbers[1:], target) + dp(numbers[1:], target - 2 * numbers[0])


def solution(numbers, target):
    new_target = target + sum(numbers)
    return dp(numbers, new_target)