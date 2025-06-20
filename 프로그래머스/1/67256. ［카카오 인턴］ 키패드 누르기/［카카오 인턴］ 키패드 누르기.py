def solution(numbers, hand):
    key_pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    left_pos = key_pos['*']
    right_pos = key_pos['#']
    answer = ''

    for num in numbers:
        pos = key_pos[num]
        if num in [1, 4, 7]:
            answer += 'L'
            left_pos = pos
        elif num in [3, 6, 9]:
            answer += 'R'
            right_pos = pos
        else:
            l_dist = abs(pos[0]-left_pos[0]) + abs(pos[1]-left_pos[1])
            r_dist = abs(pos[0]-right_pos[0]) + abs(pos[1]-right_pos[1])
            if l_dist < r_dist:
                answer += 'L'
                left_pos = pos
            elif r_dist < l_dist:
                answer += 'R'
                right_pos = pos
            else:
                if hand == 'right':
                    answer += 'R'
                    right_pos = pos
                else:
                    answer += 'L'
                    left_pos = pos

    return answer
