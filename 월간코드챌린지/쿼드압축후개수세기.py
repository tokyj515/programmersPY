def solution(arr):
    result = [0, 0]


    # 한 변의 길이, 시작 좌표
    def quad(n, x, y):
        start = arr[x][y]
        # print('x, y: ', x, y)

        for i in range(x, x + n):
            for j in range(y, y + n):
                if start != arr[i][j]:
                    n //= 2
                    quad(n, x, y)
                    quad(n, x, y + n)
                    quad(n, x + n , y)
                    quad(n, x + n, y + n)
                    return

        result[start] += 1



    quad(len(arr), 0, 0)

    return result






print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))