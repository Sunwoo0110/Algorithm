from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 1

    town_dic = defaultdict(list)

    for a, b, c in road:
        town_dic[a].append((b, c))
        town_dic[b].append((a, c))  # 양방향이기 때문에 반대 방향도 추가

    # 다익스트라
    heap = [(0, 1)]  # (현재까지 걸린 시간, 현재 마을 번호)

    # 최단 거리(배달 시간) 저장
    distance = [float('inf')] * (N + 1)
    distance[1] = 0 

    while heap:
        cur_time, cur_pos = heapq.heappop(heap)

        # 이미 더 빠른 시간으로 방문한 적 있으면 스킵
        if cur_time > distance[cur_pos]:
            continue

        # 현재 마을에서 갈 수 있는 이웃 마을들 검사
        for next_pos, time in town_dic[cur_pos]:
            next_time = cur_time + time  # 현재까지 시간 + 다음 마을까지 시간

            # 더 빠르게 도달할 수 있는 경우 갱신
            if next_time < distance[next_pos]:
                distance[next_pos] = next_time
                heapq.heappush(heap, (next_time, next_pos))  # 우선순위 큐에 추가

    # K 이하 시간 내 배달 가능한 마을의 수 세기
    answer = sum(1 for t in distance if t <= K)

    return answer
