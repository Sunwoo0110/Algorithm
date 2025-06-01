def solution(a):
    answer = len(a)
    
    left_min_arr = []
    right_min_arr = []
    
    tmp = a[0]
    for num in a:
        if tmp > num:
            tmp = num
        left_min_arr.append(tmp)
        
    tmp = a[-1]
    for num in a[::-1]:
        if tmp > num:
            tmp = num
        right_min_arr.append(tmp)
    
    right_min_arr = right_min_arr[::-1]
    
    for idx in range(len(a)):
        if idx == 0 or idx == len(a)-1:
            ## 첫번째, 마지막 인덱스는 무조건 살아남음
            continue
        
        else:
            ## 오른쪽, 왼쪽의 최솟값을 구함
            left = left_min_arr[idx-1]
            right = right_min_arr[idx+1]
            
            if a[idx] > left and a[idx] > right:
                answer -= 1
    
    return answer