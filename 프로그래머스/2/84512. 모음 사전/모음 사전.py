def solution(word):
    answer = 0
    alph = ['A', 'E', 'I', 'O', 'U']
    
    ## DFS
    for a in alph:
        
        stack = [a]
        visited = set()
        
        while stack:
            cur_word = stack.pop()
            answer += 1

            if cur_word == word:
                return answer

            if cur_word:
                visited.add(cur_word)

            for a in alph[::-1]:
                if cur_word+a not in visited and len(cur_word+a) <= 5:
                    stack.append(cur_word+a)
                
    return answer