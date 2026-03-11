from collections import defaultdict

def solution(message, spoiler_ranges):
    answer = 0
    
    spoiler_words = []
    important_words = set()
    total_words = defaultdict(int)
    processed_word_ranges = set()   ## 이미 spoiler 단어로 처리한 실제 단어 구간
    revealed_word_ranges = []       ## 공개 순서 기록 (중복 없는 실제 단어 구간 순서대로)
    
    ## 전체 단어 개수
    for msg in message.split():
        total_words[msg] += 1
    
    for s, e in spoiler_ranges:
        start, end = s, e
        
        while start > 0 and message[start] != " ":
            start -= 1
        
        while end < len(message) - 1 and message[end] != " ":
            end += 1
        
        ## 구간 안에서 실제 단어들 하나씩 뽑기
        i = start
        while i <= end:
            if message[i] == " ":
                i += 1
                continue
            
            ws = i
            while i <= end and message[i] != " ":
                i += 1
            we = i-1
            word = message[ws:we+1]
            
            ## 이 등장 위치의 단어를 처음 spoiler로 처리하는 경우만 차감
            if (ws, we) not in processed_word_ranges:
                processed_word_ranges.add((ws, we))
                revealed_word_ranges.append((ws, we, word))
                total_words[word] -= 1
    
    seen = set()
    for _, _, sw in revealed_word_ranges:
        if total_words[sw] == 0 and sw not in seen:
            important_words.add(sw)
        seen.add(sw)
    
    answer = len(important_words)
    return answer