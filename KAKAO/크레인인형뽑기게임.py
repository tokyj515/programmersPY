from collections import deque


def solution(board, moves):
    # 바구니 크기
    n = len(board[0])

    # 행 <-> 열
    lines = list(zip(*board))
    lines_list = []
    for line in lines:
        lines_list.append(deque(line))

    # moves 0 시작을 변경
    moves = [x - 1 for x in moves]

    # 바구니
    stack = []
    result = 0

    # 0 제거
    for line in lines_list:
        while True:
            if 0 in line:
                line.popleft()
            else:
                break

    for m in moves:
        line = lines_list[m]

        # board에서 line이 비어있지 않으면 pop
        if line:
            e = line.popleft()
        else:
            continue

        # 바구니 처리
        if len(stack) > 0 and stack[-1] == e:
            stack.pop()
            result += 2
        else:
            stack.append(e)

    return result

