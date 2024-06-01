from collections import Counter


def solution(N, stages):

    # 변수 선언
    percent = []
    result = []
    people = len(stages)
    counter = Counter(stages)
    counter = sorted(counter.items())


    # (스테이지 번호, 인원) 리스트
    counter_list = []
    num = [x for x in range(N+1)]
    round  = [x[0] for x in counter]

    for n in num:
        if n not in round:
            counter_list.append((n, 0))
    for c in counter:
        counter_list.append(c)

    counter_list.sort(key=lambda x : x[0])
    counter_list.pop(0)



    # 각 스테이지의 실패율
    for count in counter_list:
        if people != 0:
            percent.append((count[0], count[1] / people))
        else:
            percent.append((count[0], 0.0))
        people -= count[1]
    if len(percent) == N + 1:
        percent.pop()


    # 실패율 내림차순 정리
    percent.sort(key=lambda x: -x[1])
    for p in percent:
        result.append(p[0])
    return result

print(solution(6, [2, 2, 2, 2, 2, 2, 2, 2, 2]))


#
# N = 6
# stages = [2, 2, 2, 2, 2, 2, 2, 2, 2]
# Return = [2, 1, 3, 4, 5, 6]