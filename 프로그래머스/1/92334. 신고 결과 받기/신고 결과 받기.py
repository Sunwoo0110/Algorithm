from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    reported_dict = defaultdict(set) ## {유저 아이디: 유저를 신고한 아이디 리스트}
    mail_count_dict = defaultdict(int) ## {유저 아이디: 정지 메일 수}
    
    for rep in report:
        user_id, report_id = rep.split(" ")
        
        reported_dict[report_id].add(user_id)
    
    for key, value in reported_dict.items():
        if len(value) >= k:
            for v in value:
                mail_count_dict[v] += 1
    
    for i in id_list:
        answer.append(mail_count_dict[i])
    
    return answer