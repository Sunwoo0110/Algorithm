from collections import Counter

def solution(str1, str2):
    answer = 0
    str1_arr = []
    str2_arr = []
    
    for i in range(len(str1)-1):
        if ord(str1[i]) < 65 or (ord(str1[i]) > 90 and ord(str1[i]) < 97) or ord(str1[i]) > 122:
            continue
        if ord(str1[i+1]) < 65 or (ord(str1[i+1]) > 90 and ord(str1[i+1]) < 97) or ord(str1[i+1]) > 122:
            continue
        
        new_str = str1[i].upper()+str1[i+1].upper()
        str1_arr.append(new_str)

    for i in range(len(str2)-1):
        if ord(str2[i]) < 65 or (ord(str2[i]) > 90 and ord(str2[i]) < 97) or ord(str2[i]) > 122:
            continue
        if ord(str2[i+1]) < 65 or (ord(str2[i+1]) > 90 and ord(str2[i+1]) < 97) or ord(str2[i+1]) > 122:
            continue
        
        new_str = str2[i].upper()+str2[i+1].upper()
        str2_arr.append(new_str)
        
    str1_counter = Counter(str1_arr)
    str2_counter = Counter(str2_arr)
    
    inter_cnt = sum((str1_counter & str2_counter).values())
    union_cnt = sum((str1_counter | str2_counter).values())
    
    answer = int((inter_cnt / union_cnt) *65536) if union_cnt > 0 else 65536
    return answer