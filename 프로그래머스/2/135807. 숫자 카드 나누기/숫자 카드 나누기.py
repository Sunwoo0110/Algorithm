def solution(arrayA, arrayB):
    
    answer = 0
    
    def gcd(a, b):
        ## 최대 공약수
        while b != 0:
            tmp = a%b
            a = b
            b = tmp
        return a

    def get_gcd(arr):
        ## 배열 전체 최대 공약수
        res = arr[0]
        for x in arr[1:]:
            res = gcd(res, x)
        return res

    def check(gcd, other):
        for x in other:
            if x%gcd == 0:
                return False
        return True
    
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)

    if gcdA>1 and check(gcdA, arrayB):
        answer = max(answer, gcdA)
    if gcdB>1 and check(gcdB, arrayA):
        answer = max(answer, gcdB)
        
    return answer
