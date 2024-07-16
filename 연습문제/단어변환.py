from collections import deque

def solution(begin, target, words):
    
    # 타겟이 워드 안에 존재하지 않는 경우
    if target not in words:
        return 0
    
    def change(word1, word2):
        possible = 0
        
        if len(word1) != len(word2):
            return False
        
        for a, b in zip(word1, word2):
            # print(a, b, possible)
            if a != b:
                possible += 1
        
        if possible == 1:
            return True
        else:
            return False
        
    
    visited = [0 for _ in range(len(words))]
    max_dep = len(words)
    answer = 0
    
    temp = []

    
    # print(change("hot", "dot"))
    
    def bfs(start, dep):
        nonlocal begin, target, answer
        
        # start와 타겟이 같으면 종료
        if start == target:
            answer = dep
            return
        
        # start가 최하위까지 내려가도 종료 -> 더이상 탐색할 게 없어서
        if start == max_dep:
            return
        
        print("start: ", start, " dep: ", dep)
        
        
        for i, word in enumerate(words):
            if visited[i] == 1:
                continue
    
            if change(start, word):
                visited[i] = 1
                bfs(word, dep+1)
                visited[i] = 0
                
        print("fin")
            
    bfs(begin, 0)
        
        
    return answer