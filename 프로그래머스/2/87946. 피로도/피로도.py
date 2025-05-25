def solution(k, dungeons):
    answer = -1
    num_arr = []
    
    def search(cur_k, dun, num):
        if not dun or cur_k < min(a for a, b in dun):
            num_arr.append(num)
            
        for idx in range(len(dun)):
            if dun[idx][0] <= cur_k:
                search(cur_k-dun[idx][1], dun[:idx]+dun[idx+1:], num+1)
        
    
    search(k, dungeons, 0)
    answer = max(num_arr)
    
    return answer