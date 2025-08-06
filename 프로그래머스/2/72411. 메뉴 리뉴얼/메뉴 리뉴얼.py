
def solution(orders, course):
    answer = []
    
    combination = []
    total_comb = set()
    
    for order in orders:
        n = len(order)
        comb = []
        for bit in range(1, 1<<n):
            menu = ""
            for i in range(n):
                if (bit&(1<<i)) != 0:
                    menu += order[i]
            if len(menu) in course:
                menu = "".join(sorted(menu))
                comb.append(menu)
                total_comb.add(menu)
        combination.append(comb)
    
    for crs in course:
        max_num = 0
        max_tc = []
        for tc in total_comb:
            if crs == len(tc):
                cnt = 0
                for comb in combination:
                    if tc in comb:
                        cnt += 1

                if max_num < cnt and cnt >= 2:
                    max_num = cnt
                    max_tc = []
                    max_tc.append(tc)
                elif max_num == cnt and cnt >= 2:
                    max_tc.append(tc)
                    
        for mt in max_tc:
            answer.append(mt)
            
    answer.sort()
    
    return answer