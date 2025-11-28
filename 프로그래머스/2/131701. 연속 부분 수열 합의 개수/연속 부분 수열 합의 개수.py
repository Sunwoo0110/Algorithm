def solution(elements):
    answer = 0
    
    sub_elem_set = set()
    n = len(elements)
    
    line_elements = elements*2
    
    for length in range(1, n+1):
        total = sum(line_elements[:length])
        
        for i in range(n):
            total = total-line_elements[i]+line_elements[i+length]
            sub_elem_set.add(total)
        
    answer = len(sub_elem_set)
    return answer