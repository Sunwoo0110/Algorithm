def solution(order):
    answer = 0
    idx = 1
    l = len(order)
    sub_container = [] ## stack
    
    for o in order:
        if (idx > l and idx != o) and (sub_container and sub_container[-1] != o):
            ## 방법이 없는 경우
            break
            
        while True:
            if o == idx:
                ## 바로 트럭에 싣는 경우
                answer += 1
                idx += 1
                break
            elif (sub_container and sub_container[-1] == o):
                ## 보조 컨테이너 벨트에서 싣는 경우
                sub_container.pop()
                answer += 1
                break
            elif idx <= l:
                ## 보조 컨테이너 벨트에 보관하는 경우
                sub_container.append(idx)
                idx += 1
            else:
                break
    
    return answer