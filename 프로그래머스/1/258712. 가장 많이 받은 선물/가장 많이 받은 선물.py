from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    n = len(friends)
    
    friend_index = defaultdict(int)
    gift_arr = [[0 for _ in range(n)] for _ in range(n)] ## 주고 받은 선물 기록
    gift_rate = [0 for _ in range(n)] ## 선물 지수
    nxt_gift = [0 for _ in range(n)] ## 다음달 받을 선물
    
    for i in range(n):
        friend_index[friends[i]] = i
        
    for g in gifts:
        sender, receiver = g.split(" ")
        sender_idx, receiver_idx = friend_index[sender], friend_index[receiver]
        
        gift_arr[sender_idx][receiver_idx] += 1
        gift_rate[sender_idx] += 1
        gift_rate[receiver_idx] -= 1
        
    for i in range(n):
        for j in range(i+1, n):
            if gift_arr[i][j] > gift_arr[j][i]:
                nxt_gift[i] += 1
            elif gift_arr[i][j] < gift_arr[j][i]:
                nxt_gift[j] += 1
            else:
                if gift_rate[i] > gift_rate[j]:
                    nxt_gift[i] += 1
                elif gift_rate[i] < gift_rate[j]:
                    nxt_gift[j] += 1
                else:
                    pass
    
    answer = max(nxt_gift)
    return answer