from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    
    term_dic = defaultdict(int) ## 일 기준으로 저장
    
    for term in terms:
        a, b = term.split(" ")
        term_dic[a] = int(b)*28
    
    y, m, d = map(int, today.split("."))
    today_d = y*12*28 + m*28 + d ## 일 기준으로 저장
    
    for idx, privacy in enumerate(privacies):
        date, p = privacy.split(" ")
        y, m, d = map(int, date.split("."))
        
        privacy_d = y*12*28 + m*28 + d
        
        if term_dic[p] <= today_d-privacy_d:
            answer.append(idx+1)
        
    return answer