def num_to_bit(num):
    ans = []
    
    while num > 0:
        if num%2 == 0:
            ans.append("0")
        else:
            ans.append("1")
        num //= 2
    
    return ''.join(ans[::-1])
            
        
def solution(numbers):
    answer = []
    
    for num in numbers:
        bit_num = num_to_bit(num)
        idx = len(bit_num)-1
        len_one = 0
        
        while idx >= 0:
            if bit_num[idx] == "0":
                break
                
            len_one += 1
            idx -= 1
        
        if len_one == 0:
            answer.append(num+1)
        else:
            answer.append(num+(2**(len_one-1)))
    
    return answer