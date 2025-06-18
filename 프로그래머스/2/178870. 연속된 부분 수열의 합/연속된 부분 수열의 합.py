def solution(sequence, k):
    n = len(sequence)
    start = 0
    end = 0
    total = sequence[0]

    answer = [0, n - 1]
    min_len = n 

    while start < n and end < n:
        if total < k:
            end += 1
            if end < n:
                total += sequence[end]
        elif total > k:
            total -= sequence[start]
            start += 1
        else:
            # total == k
            if end - start < min_len:
                answer = [start, end]
                min_len = end - start
            # 다음 윈도우로 이동
            total -= sequence[start]
            start += 1

    return answer


## 만약 정렬 안된 경우 -> 누적합+해시맵

def solution(sequence, k):
    prefix_sum = 0 ## 누적합
    sum_idx_map = {0: -1}  # 누적합: 인덱스
    min_len = len(sequence) + 1
    result = []

    for i, num in enumerate(sequence):
        prefix_sum += num
        
        ## prefix_sum - k 였던 인덱스+1 ~ 현재 인덱스까지 합이 K
        if prefix_sum - k in sum_idx_map:
            start = sum_idx_map[prefix_sum - k] + 1
            end = i
            ## 최단 길이 갱신
            if end - start + 1 < min_len:
                min_len = end - start + 1
                result = [start, end]

        # sum_idx_map에는 가장 빠른 인덱스만 기록해야 짧은 수열이 생김(해당 누적합이 처음 등장한 인덱스만 저장)
        if prefix_sum not in sum_idx_map:
            sum_idx_map[prefix_sum] = i

    return result

