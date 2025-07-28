def solution(relation):
    answer = 0
    n = len(relation)
    attrLen = len(relation[0])
    candidateKeys = []
    
    for bit in range(1, 1<<attrLen):
        tuple_set = set()
        
        for i in range(n):
            st = ""
            for j in range(attrLen):
                if bit&(1<<j) != 0:
                    st += relation[i][j]
            tuple_set.add(st)
            
        if len(tuple_set) != n:
            continue
        
        isMinimal = True
        for ck in candidateKeys:
            if ck & bit == ck:
                isMinimal = False
                break
        
        if isMinimal:
            candidateKeys.append(bit)
    
    return len(candidateKeys)