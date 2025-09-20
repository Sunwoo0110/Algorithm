def solution(wallet, bill):
    answer = 0
    x, y = min(wallet), max(wallet)
    bx, by = min(bill), max(bill)
    
    while bx > x or by > y:
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        bx, by = min(bill), max(bill)
    
    return answer