def solution(numbers):
    answer = 0
    num_set= set()
    
    ## 만들 수 있는 모든 숫자 DFS
    stack = [("", [False]*len(numbers))]

    while stack:
        cur_num, visited = stack.pop()

        if cur_num:
            num_set.add(int(cur_num))

        for idx in range(len(numbers)):
            if visited[idx] == False:
                new_visited = visited[:]
                new_visited[idx] = True
                stack.append((cur_num+numbers[idx], new_visited))
        
    def is_prime(num):
        if num < 2:
            return False
            
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
            
        return True
    
    answer = sum(1 for num in num_set if is_prime(num))
    return answer