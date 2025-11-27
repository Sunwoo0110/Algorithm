from collections import defaultdict

def solution(record):
    answer = []
    
    uid_nickname_dict = defaultdict(str)
    
    for rec in record:
        rec_split = rec.split(" ")
        typ, uid = rec_split[0], rec_split[1]
        if typ == "Enter" or typ == "Change":
            uid_nickname_dict[uid] = rec_split[2]
            
    for rec in record:
        rec_split = rec.split(" ")
        typ, uid = rec_split[0], rec_split[1]
        
        result = ""
        
        if typ == "Enter":
            result = f"{uid_nickname_dict[uid]}님이 들어왔습니다."
            answer.append(result)
        elif typ == "Leave":
            result = f"{uid_nickname_dict[uid]}님이 나갔습니다."
            answer.append(result)
    
    return answer