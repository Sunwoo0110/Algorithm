import heapq

def to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(book_time):
    times = []
    for s, e in book_time:
        start = to_min(s)
        end = to_min(e) + 10
        times.append((start, end))
    times.sort() ## start 기준 정렬

    ## min-heap : 각 방이 언제까지 사용 불가인지 (다시 사용 가능한 시각)
    heap = []

    for start, end in times:
        if heap and heap[0] <= start:
            # 가장 빨리 비는 방이 이번 예약 시작 전에 비면 방 재사용
            heapq.heappop(heap)
        # 이번 예약으로 방(새거나 재사용한거)의 새 end 시간 push
        heapq.heappush(heap, end)

    return len(heap)
