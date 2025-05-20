def solution(places):
    answer = []
    
    isFail = False
    
    for place in places:
        isFail = False
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    for mx, my in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        if i+mx < 5 and i+mx >= 0 and j+my < 5 and j+my >= 0 and place[i+mx][j+my] == 'P' and isFail == False:
                            answer.append(0)
                            isFail = True
                            break
                    
                    for mx, my in [[-1, 1], [1, 1], [1, -1], [-1, -1]]:
                        if i+mx < 5 and i+mx >= 0 and j+my < 5 and j+my >= 0 and place[i+mx][j+my] == 'P' and isFail == False:
                             if place[i][j+my] != 'X' or place[i+mx][j] != 'X':
                                    answer.append(0)
                                    isFail = True
                                    break
                    
                    for mx, my in [[-2, 0], [2, 0], [0, 2], [0, -2]]:
                        if i+mx < 5 and i+mx >= 0 and j+my < 5 and j+my >= 0 and place[i+mx][j+my] == 'P' and isFail == False:
                            if place[i+(mx//2)][j+(my//2)] != 'X':
                                answer.append(0)
                                isFail = True
                                break
                            
                            
                if isFail == True:
                    break
            if isFail == True:
                break
        
        if isFail == False:
            answer.append(1)
            
                            
        
    return answer