from collections import defaultdict

def solution(record):
    answer = []
    
    idName = defaultdict(str)
    
    for rec in record:
        recArr = rec.split(" ")
        id = recArr[1]
        
        if recArr[0] == "Enter" or recArr[0] == "Change":
            idName[id] = recArr[2]
            
    for rec in record:
        recArr = rec.split(" ")
        id = recArr[1]
        
        if recArr[0] == "Enter": 
            answer.append(idName[id] + "님이 들어왔습니다.")
        elif recArr[0] == "Leave": 
            answer.append(idName[id] + "님이 나갔습니다.")
    
    return answer