# answer = 0  # 중간에 3이 되는지
# visited = [0 for _i in range(len(number))]
# result = 0  # 삼총사 개수
#


from itertools import combinations

number = [-2, 3, 0, 2, -5]

result = 0
com_list = list(combinations(number, 3))
print(com_list)

for e in com_list:
    if sum(e) == 3:
        result += 1

print(result)








# def dfs(i, answer):
#     # 현재 인덱스 방문하고 그 값을 answer에 더해
#     visited[i] = 1
#     answer += number[i]
#
#     # answer가 되면 삼총사 개수에 추가
#     if answer == 3:
#         result += 1
#         answer = 0
#
#     if visited[i + 1] == 0:
#         dfs(i + 1)
#
#
# #     print(number)
# #     print(visited)
#
#
# dfs(0, 0)  # 시작 인덱스0, answer가 3이 되는지

