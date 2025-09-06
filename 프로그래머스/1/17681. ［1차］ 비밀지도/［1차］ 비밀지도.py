def solution(n, arr1, arr2):
    answer = []
    
    def to_bin(num):
        res = ""
        
        while num>0:
            res += str(num%2)
            num //= 2
            
        return res
    
    for i in range(n):
        n1 = to_bin(arr1[i])
        n2 = to_bin(arr2[i])
        res = ""
        
        for j in range(n):
            if (len(n1) <= j or n1[j] == "0") and (len(n2) <= j or n2[j] == "0"):
                res += " "
            else:
                res += "#"
                
        answer.append(res[::-1])
        
    return answer