def solution(arr):
    answer = 0
    
    ## 최대공약수
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    
    num1 = arr[0]
    for i in range(1, len(arr)):
        num2 = arr[i]
        
        num1 = num1*num2 // gcd(num1, num2)
        
    answer = num1
    
    return answer