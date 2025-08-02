def solution(n):
    answer = n+1
    
    def count_one(num):
        bin_num = ""
        one_num = 0
        
        while num > 0:
            if num%2 == 1:
                one_num += 1
            bin_num += str(num%2)
            num //= 2
            
        return one_num
    
    n_one_num = count_one(n)
    
    while True:
        if n_one_num == count_one(answer):
            break
            
        answer += 1
    
    return answer