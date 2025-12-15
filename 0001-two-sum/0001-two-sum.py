from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [0, 0]
        n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i]+nums[j] == target:
        #             answer[0], answer[1] = i, j
        #             return answer

        idx_dict = defaultdict(int)
        num_set = set()

        for i in range(n):
            curr = nums[i]

            if num_set and target-curr in num_set:
                answer[0], answer[1] = idx_dict[target-curr], i
                break
            
            num_set.add(curr)
            idx_dict[curr] = i
        
        return answer