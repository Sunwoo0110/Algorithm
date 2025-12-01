from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix = 0
        n = len(nums)

        ## 해당 누적합이 몇 번 나타나는지
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for num in nums:
            prefix += num
            answer += prefix_cnt[prefix-k]
            prefix_cnt[prefix] += 1

        
        return answer
        
        