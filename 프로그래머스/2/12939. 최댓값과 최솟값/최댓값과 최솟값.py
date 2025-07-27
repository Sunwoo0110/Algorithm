def solution(s):
    answer = ''
    str_arr = s.split(" ")
    int_arr = [int(sa) for sa in str_arr]
    int_arr.sort()
    
    answer = str(int_arr[0]) + " " + str(int_arr[-1])
     
    return answer