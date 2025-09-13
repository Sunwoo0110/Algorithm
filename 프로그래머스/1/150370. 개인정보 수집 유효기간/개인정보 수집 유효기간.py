from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    term_dict = defaultdict(int)
    
    t_year, t_mon, t_day = today.split(".")
    t_year, t_mon, t_day = int(t_year), int(t_mon), int(t_day)
    t_total = t_year*12*28 + t_mon*28 + t_day
    
    for term in terms:
        a, b = term.split(" ")
        term_dict[a] = int(b)*28
    
    for idx, (privacy) in enumerate(privacies):
        date, term = privacy.split(" ")
        
        p_year, p_mon, p_day = date.split(".")
        p_year, p_mon, p_day = int(p_year), int(p_mon), int(p_day)
        
        p_total = p_year*12*28 + p_mon*28 + p_day
        
        if term_dict[term] <= t_total-p_total:
            answer.append(idx+1)
        
    return answer