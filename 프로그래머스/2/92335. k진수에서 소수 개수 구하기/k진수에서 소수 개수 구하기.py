def solution(n, k):
    answer = 0
    
    k_num = ""
    
    ## k진수 변환
    while n>0:
        k_num += str(n%k)
        n//=k
        
    k_num = k_num[::-1]
    
    def is_prime(n):
        if n<2: return False
        
        for i in range(2, (int)(n**(1/2))+1):
            if n%i == 0: return False
        
        return True
    
    prime = ""
    for s in k_num:
        if s == '0':
            if prime != "" and is_prime(int(prime)):
                answer += 1
            prime = ""
        else:
            prime += s
            
    if prime != "" and is_prime(int(prime)): answer += 1
    
    return answer