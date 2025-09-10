from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    point = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    personality_point = defaultdict(int)
    category = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    personality = [[0 for _ in range(2)] for _ in range(4)]
    
    for sur, cho in zip(survey, choices):
        if cho < 4:
            personality_point[sur[0]] += point[cho]
        elif cho > 4:
            personality_point[sur[1]] += point[cho]
        else: 
            pass
    
    for a, b in category:
        if personality_point[a] >= personality_point[b]:
            answer += a
        elif personality_point[a] < personality_point[b]:
            answer += b
    
    return answer