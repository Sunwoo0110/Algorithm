def solution(s):
    answer = []
    
    set_list = [i[2:] for i in s.split("}")[:-2:]]
    set_list.sort(key=lambda x: len(x))
    
    for sl in set_list:
        sl_list = [int(j) for j in sl.split(",")]
        
        for sll in sl_list:
            if sll not in answer:
                answer.append(sll)
                break
    
    return answer