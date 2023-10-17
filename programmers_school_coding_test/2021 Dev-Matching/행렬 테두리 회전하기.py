def solution(rows, columns, queries):
    matrix = [[j+1+i*columns for j in range(columns)] for i in range(rows)]
    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        next_num = matrix[x1][y1]
        min_num = 9999
        for i in range(y2-y1):
            temp = matrix[x1][y1+i+1]
            matrix[x1][y1+i+1] = next_num
            next_num = temp
            min_num = min(min_num,next_num)
        for i in range(x2-x1):
            temp = matrix[x1+i+1][y2]
            matrix[x1+i+1][y2] = next_num
            next_num = temp
            min_num = min(min_num,next_num)
        for i in range(y2-y1):
            temp = matrix[x2][y2-i-1]
            matrix[x2][y2-i-1] = next_num
            next_num = temp
            min_num = min(min_num,next_num)
        for i in range(x2-x1):
            temp = matrix[x2-i-1][y1]
            matrix[x2-i-1][y1] = next_num
            next_num = temp
            min_num = min(min_num,next_num)
        answer.append(min_num)
    return answer