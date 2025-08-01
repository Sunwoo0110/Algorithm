def solution(m, musicinfos):
    answer = ''
    
    poss_list = []
    
    new_m = ""
    
    for i in range(len(m)):
        if m[i] == "#":
            new_m = new_m[:-1]
            new_m += m[i-1].lower()
        else:
            new_m += m[i]
    
    for idx, musicinfo in enumerate(musicinfos):
        mi = musicinfo.split(",")
        play_len = (int(mi[1].split(":")[0])*60+int(mi[1].split(":")[1])) - (int(mi[0].split(":")[0])*60+int(mi[0].split(":")[1]))
        music_name = mi[2]
        melody = ""
        
        for i in range(len(mi[3])):
            if mi[3][i] == "#":
                melody = melody[:-1]
                melody += mi[3][i-1].lower()
            else:
                melody += mi[3][i]
        
        melody_len = len(melody)
        
        play_melody = melody*(play_len//melody_len) + melody[:play_len%melody_len] if play_len >= melody_len else melody[:play_len]
        
        print(new_m, melody, play_melody)
        
        if new_m in play_melody:
            poss_list.append([play_len, -idx, music_name])
            
    if len(poss_list) == 0:
        return "(None)"
    
    poss_list.sort(reverse=True)
    
    answer = poss_list[0][2]
    
    return answer