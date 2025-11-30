from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        sorted_nums = sorted(num_dict.items(), key=lambda x: -x[1])
        answer = [num for num, freq in sorted_nums[:k]]

        return answer

    def topKFrequent2 (self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for num, f in num_dict.items():
            buckets[f].append(num) ## 해당 빈도 수인 숫자 리스트

        ## 높은 빈도부터 내려가면서 숫자 채우기
        for f in range(n, 0, -1):
            if not buckets[f]:
                continue
            for num in buckets[f]:
                answer.append(num)
                if len(answer) == k:
                    return answer

        return answer
    
    def topKFrequent3 (self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        heap = []
        for num, f in num_dict.items():
            heapq.heappush(heap, (f, num))  ## 빈도 기준 min-heap
            if len(heap) > k:
                heapq.heappop(heap)

        answer = [num for f, num in heap]
        return answer