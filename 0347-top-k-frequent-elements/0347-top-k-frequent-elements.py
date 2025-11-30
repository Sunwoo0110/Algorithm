from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        sorted_nums = sorted(num_dict.items(), key=lambda x: -x[1])
        answer = [num for num, freq in sorted_nums[:k]]

        return answer
        