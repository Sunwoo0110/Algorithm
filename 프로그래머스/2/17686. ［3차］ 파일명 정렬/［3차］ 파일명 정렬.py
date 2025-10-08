def solution(files):
    answer = []
    
    sort_files = []
    
    for idx, file in enumerate(files):
        head, number = "", ""
        i = 0
        l = len(file)
        
        while i < l:
            if file[i].isdigit():
                break 
            head += file[i]
            i += 1
        
        while i < l: 
            if not file[i].isdigit():
                break
            
            number += file[i]
            i += 1
        
        head = head.upper()
        sort_files.append((head, int(number), idx))
        
    sort_files.sort()
    
    for h, n, i in sort_files:
        answer.append(files[i])
        
    return answer