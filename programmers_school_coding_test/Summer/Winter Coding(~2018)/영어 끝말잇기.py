def solution(n, words):
    answer = -1
    last = words[0][0]
    for i, word in enumerate(words):
        if word[0] != last or words.index(word) != i:
            answer = i
            break
        last = word[-1]
    if answer == -1:
        return [0,0]
    return [answer%n+1, answer//n+1]