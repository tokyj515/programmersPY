def solution(n, computers):
    
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    
    
    for v, element in enumerate(computers):
        print(v, element)
        for i, e in enumerate(element):
            if e ==1 and v != i:
                graph[v+1].append(i+1)
    
    for row in graph:
        print(row)
    
    
    def dfs(v):
        visited[v] = 1
        print(v)
        
        for next in graph[v]:
            if not visited[next]:
                dfs(next)
            

        
    # dfs(1)
        
    for i in range(1, n+1):
        print("for문 시작지점!", i)
        if not visited[i]:
            dfs(i)
            answer += 1
    
    
    print("답: ", answer)
    
    
    return answer