from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        genre_songs[g].append((p, i))
    
    sorted_genres = sorted(genre_total.items(), key=lambda x: -x[1]) ## 내림차순
    
    for gen in sorted_genres:
        songs = genre_songs[gen[0]]
        songs.sort(key=lambda x: -x[0])
        
        if len(songs) >= 2:
            answer.append(songs[0][1])
            answer.append(songs[1][1])
        elif len(songs) == 1:
            answer.append(songs[0][1])
    
    return answer
