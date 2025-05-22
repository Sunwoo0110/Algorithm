def solution(numbers):
    answer = ''
    
    str_nums = [str(num) for num in numbers]
    str_nums = sorted(str_nums, key=lambda x: x*3, reverse=True)
    
    answer = answer.join(str_nums)
    if answer[0] == '0':
        answer = '0'
        
    return answer