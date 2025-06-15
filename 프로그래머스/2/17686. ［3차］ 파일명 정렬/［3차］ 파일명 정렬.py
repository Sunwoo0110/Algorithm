def solution(files):
    answer = []
    
    file_arr = []
    
    for f_idx, file in enumerate(files):
        idx = 0
        head = ""
        number = ""
        while idx < len(file):
            if file[idx] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            
            head += file[idx]
            idx += 1
            
        while idx < len(file):
            if file[idx] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            
            number += file[idx]
            idx += 1 
        
        file_arr.append((head.upper(), int(number), f_idx))
    
    file_arr.sort()
    answer = [files[i[2]] for i in file_arr]
        
    return answer