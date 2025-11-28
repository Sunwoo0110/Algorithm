def solution(elements):
    answer = 0
    
    sub_elem_set = set()
    n = len(elements)
    
    line_elements = elements*2
    
    for i in range(1, n+1):
        for j in range(n):
            sub_elem_set.add(sum(line_elements[j:j+i]))
    answer = len(sub_elem_set)
    return answer